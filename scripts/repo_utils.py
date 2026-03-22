#!/usr/bin/env python3
from __future__ import annotations

import re
from hashlib import sha1
from pathlib import Path
from typing import Iterable

import frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent

GENERATED_MARKDOWN_FILES = {
    "meta/latest-ai-validation-report.md",
}

GENERATED_DATA_FILES = {
    "meta/chunk-manifest.jsonl",
    "meta/chunk-manifest-summary.json",
    "meta/fetch-log.jsonl",
    "meta/freshness-manifest.json",
}

REF_PATTERN = re.compile(
    r"""
    (?:
        `(?P<code>[^`\n]+\.(?:md|py|json|jsonl))`
        |
        \[[^\]]+\]\((?P<link>[^)\s]+\.(?:md|py|json|jsonl))\)
    )
    """,
    re.VERBOSE,
)
SC_PATTERN = re.compile(r"\bSC\s+(\d+\.\d+\.\d+)\b", re.IGNORECASE)
LEVEL_PATTERN = re.compile(r"\bLevel\s+(AAA|AA|A)\b")


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def iter_markdown_files(
    *,
    include_fetched: bool = True,
    include_generated: bool = False,
) -> Iterable[Path]:
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        rel_path = repo_relative(path)
        if not include_fetched and rel_path.endswith("-fetched.md"):
            continue
        if not include_generated and rel_path in GENERATED_MARKDOWN_FILES:
            continue
        yield path


def load_markdown(path: Path) -> tuple[dict, str]:
    post = frontmatter.load(path)
    return post.metadata, post.content


def platform_from_path(rel_path: str) -> str | None:
    path = Path(rel_path)
    parts = path.parts
    if len(parts) >= 5 and parts[:3] == ("domains", "social-media", "platforms"):
        return parts[3]
    return None


def content_kind(rel_path: str) -> str:
    if rel_path.endswith("-full-fetched.md"):
        return "raw-full-capture"
    if rel_path.endswith("-fetched.md"):
        return "raw-capture"
    if rel_path in GENERATED_MARKDOWN_FILES:
        return "generated-markdown"
    return "canonical"


def content_family(rel_path: str) -> str:
    path = Path(rel_path)
    if len(path.parts) == 1:
        return "root"
    return path.parts[0]


def make_chunk_id(rel_path: str, heading_path: str, chunk_text: str) -> str:
    payload = f"{rel_path}\n{heading_path}\n{chunk_text}".encode("utf-8")
    return sha1(payload).hexdigest()[:16]


def freshness_signal(metadata: dict) -> tuple[str | None, str | None]:
    for key in ("last_reviewed", "last_verified", "last_fetched", "last_updated"):
        value = metadata.get(key)
        if value:
            return key, str(value)
    return None, None


def token_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def extract_sc_number(text: str) -> str | None:
    match = SC_PATTERN.search(text)
    return match.group(1) if match else None


def extract_level(text: str) -> str | None:
    match = LEVEL_PATTERN.search(text)
    return match.group(1) if match else None


def extract_internal_refs(text: str) -> list[str]:
    refs: list[str] = []
    for match in REF_PATTERN.finditer(text):
        candidate = match.group("code") or match.group("link")
        if not candidate:
            continue
        if candidate.startswith(("http://", "https://", "/", "#", "mailto:")):
            continue
        if any(char in candidate for char in "[]<>"):
            continue
        refs.append(candidate)
    return refs


def split_h2_sections(content: str, fallback_heading: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+)$", content))
    if not matches:
        body = content.strip()
        return [(fallback_heading, body)] if body else []

    sections: list[tuple[str, str]] = []
    preamble = content[: matches[0].start()].strip()
    if preamble:
        sections.append(("Overview", preamble))

    for index, match in enumerate(matches):
        title = match.group(1).strip()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        body = content[match.start() : end].strip()
        if body:
            sections.append((title, body))
    return sections


def _overlap_words(text: str, overlap_tokens: int) -> str:
    if overlap_tokens <= 0:
        return ""
    words = re.findall(r"\S+", text)
    if not words:
        return ""
    return " ".join(words[-overlap_tokens:])


def split_section_into_chunks(
    text: str,
    *,
    min_tokens: int,
    max_tokens: int,
    overlap_tokens: int,
) -> list[str]:
    if token_count(text) <= max_tokens:
        return [text.strip()]

    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    if not paragraphs:
        return [text.strip()]

    chunks: list[str] = []
    current_parts: list[str] = []

    for paragraph in paragraphs:
        candidate = "\n\n".join(current_parts + [paragraph]).strip()
        if current_parts and token_count(candidate) > max_tokens:
            chunk_text = "\n\n".join(current_parts).strip()
            chunks.append(chunk_text)
            overlap_text = _overlap_words(chunk_text, overlap_tokens)
            current_parts = [overlap_text, paragraph] if overlap_text else [paragraph]
        else:
            current_parts.append(paragraph)

    if current_parts:
        chunks.append("\n\n".join(current_parts).strip())

    if len(chunks) > 1 and token_count(chunks[-1]) < min_tokens:
        chunks[-2] = f"{chunks[-2]}\n\n{chunks[-1]}".strip()
        chunks.pop()

    return chunks


def chunk_markdown_file(
    path: Path,
    *,
    min_tokens: int = 100,
    max_tokens: int = 512,
    overlap_tokens: int = 50,
) -> list[dict]:
    metadata, content = load_markdown(path)
    rel_path = repo_relative(path)
    fallback_heading = str(metadata.get("title") or path.stem)
    h1_match = re.search(r"(?m)^#\s+(.+)$", content)
    top_heading = h1_match.group(1).strip() if h1_match else fallback_heading
    sections = split_h2_sections(content, fallback_heading)

    chunks: list[dict] = []
    for section_title, section_body in sections:
        chunk_texts = split_section_into_chunks(
            section_body,
            min_tokens=min_tokens,
            max_tokens=max_tokens,
            overlap_tokens=overlap_tokens,
        )
        for index, chunk_text in enumerate(chunk_texts, start=1):
            heading_path = top_heading if section_title == top_heading else f"{top_heading} > {section_title}"
            if len(chunk_texts) > 1:
                heading_path = f"{heading_path} [part {index}]"
            freshness_key, freshness_value = freshness_signal(metadata)
            chunks.append(
                {
                    "chunk_id": make_chunk_id(rel_path, heading_path, chunk_text),
                    "source_file": rel_path,
                    "title": metadata.get("title", fallback_heading),
                    "heading_path": heading_path,
                    "standard": metadata.get("standard", ""),
                    "domain": metadata.get("domain", []),
                    "tags": metadata.get("tags", []),
                    "status": metadata.get("status", ""),
                    "type": metadata.get("type", ""),
                    "source_url": metadata.get("source_url", ""),
                    "platform": platform_from_path(rel_path),
                    "content_family": content_family(rel_path),
                    "content_kind": content_kind(rel_path),
                    "last_fetched": metadata.get("last_fetched"),
                    "last_verified": metadata.get("last_verified"),
                    "last_reviewed": metadata.get("last_reviewed"),
                    "last_updated": metadata.get("last_updated"),
                    "stale": bool(metadata.get("stale", False)),
                    "sc_number": extract_sc_number(chunk_text) or extract_sc_number(section_title),
                    "level": extract_level(chunk_text),
                    "freshness_field": freshness_key,
                    "freshness_value": freshness_value,
                    "token_count": token_count(chunk_text),
                    "text": chunk_text.strip(),
                }
            )
    return chunks
