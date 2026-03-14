---
title: "Accessible Data Table Pattern"
standard: "WCAG 2.2 + HTML"
source_url: "https://www.w3.org/WAI/tutorials/tables/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["table", "data-table", "thead", "th", "scope", "aria", "component-pattern"]
ai_context: "Accessible data table patterns. Covers simple tables, complex headers, sortable columns, and responsive tables. Load when generating HTML tables."
---

# Accessible Data Table Pattern

---

## Core Table Accessibility Rules

1. **Use `<table>` for tabular data** — not for layout
2. **Mark column headers** with `<th scope="col">`
3. **Mark row headers** with `<th scope="row">`
4. **Provide a caption** with `<caption>` or `aria-label` / `aria-labelledby`
5. **Complex tables** — use `id` + `headers` attributes to associate cells with headers

---

## Simple Table (Column Headers Only)

```html
<table>
  <caption>Q4 2025 Sales by Region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Q4 Revenue</th>
      <th scope="col">Growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>North America</td>
      <td>$4.2M</td>
      <td>+12%</td>
    </tr>
    <tr>
      <td>Europe</td>
      <td>$2.9M</td>
      <td>+28%</td>
    </tr>
    <tr>
      <td>APAC</td>
      <td>$0.8M</td>
      <td>+3%</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>$7.9M</td>
      <td>+18%</td>
    </tr>
  </tfoot>
</table>
```

---

## Table With Row and Column Headers

```html
<table>
  <caption>Employee schedule — Week of March 13, 2026</caption>
  <thead>
    <tr>
      <td></td> <!-- Empty cell at intersection -->
      <th scope="col">Monday</th>
      <th scope="col">Tuesday</th>
      <th scope="col">Wednesday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Alice</th>
      <td>On-site</td>
      <td>Remote</td>
      <td>On-site</td>
    </tr>
    <tr>
      <th scope="row">Bob</th>
      <td>Remote</td>
      <td>On-site</td>
      <td>Off</td>
    </tr>
  </tbody>
</table>
```

---

## Complex Tables (Multi-level Headers)

Use `id` on headers and `headers` attribute on cells when columns or rows span multiple header levels.

```html
<table>
  <caption>Quarterly revenue by product and region</caption>
  <thead>
    <tr>
      <td rowspan="2"></td>
      <th colspan="2" scope="colgroup" id="h-na">North America</th>
      <th colspan="2" scope="colgroup" id="h-eu">Europe</th>
    </tr>
    <tr>
      <th scope="col" id="h-na-q1">Q1</th>
      <th scope="col" id="h-na-q2">Q2</th>
      <th scope="col" id="h-eu-q1">Q1</th>
      <th scope="col" id="h-eu-q2">Q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" id="h-prod-a">Product A</th>
      <td headers="h-na h-na-q1 h-prod-a">$1.1M</td>
      <td headers="h-na h-na-q2 h-prod-a">$1.3M</td>
      <td headers="h-eu h-eu-q1 h-prod-a">$0.5M</td>
      <td headers="h-eu h-eu-q2 h-prod-a">$0.7M</td>
    </tr>
  </tbody>
</table>
```

---

## Sortable Columns

```html
<table aria-label="Products">
  <thead>
    <tr>
      <th scope="col">
        <button type="button" aria-sort="none">
          Name
          <span aria-hidden="true">↕</span>
        </button>
      </th>
      <th scope="col" aria-sort="ascending">
        <button type="button" aria-sort="ascending">
          Price
          <span aria-hidden="true">↑</span>
        </button>
      </th>
      <th scope="col">
        <button type="button" aria-sort="none">
          Rating
          <span aria-hidden="true">↕</span>
        </button>
      </th>
    </tr>
  </thead>
  <tbody>
    <!-- rows -->
  </tbody>
</table>
```

**`aria-sort` values:**
- `ascending` — sorted A→Z or 1→9
- `descending` — sorted Z→A or 9→1
- `none` — not currently sorted
- `other` — sorted by custom algorithm

The `aria-sort` attribute goes on the `<th>`, not the button inside it. When using a button inside `<th>`, also set `aria-sort` on the button itself for better SR support.

```javascript
function sortTable(columnIndex, button) {
  const currentSort = button.getAttribute('aria-sort');
  const newSort = currentSort === 'ascending' ? 'descending' : 'ascending';

  // Reset all sort buttons
  document.querySelectorAll('th[aria-sort]').forEach(th => {
    th.setAttribute('aria-sort', 'none');
    th.querySelector('button').setAttribute('aria-sort', 'none');
  });

  // Set new sort
  const th = button.closest('th');
  th.setAttribute('aria-sort', newSort);
  button.setAttribute('aria-sort', newSort);

  // Perform sort...
  // After sort, announce to screen readers
  const liveRegion = document.getElementById('table-status');
  liveRegion.textContent = `Table sorted by ${button.textContent.trim()}, ${newSort}`;
}
```

---

## Row Selection

```html
<table aria-label="Inbox messages" aria-multiselectable="true">
  <thead>
    <tr>
      <th scope="col">
        <input
          type="checkbox"
          id="select-all"
          aria-label="Select all messages"
          aria-checked="false"
        >
      </th>
      <th scope="col">From</th>
      <th scope="col">Subject</th>
    </tr>
  </thead>
  <tbody>
    <tr aria-selected="false">
      <td>
        <input type="checkbox" aria-label="Select message from Alice">
      </td>
      <td>Alice</td>
      <td>Q4 report</td>
    </tr>
    <tr aria-selected="true">
      <td>
        <input type="checkbox" aria-label="Select message from Bob" checked>
      </td>
      <td>Bob</td>
      <td>Meeting notes</td>
    </tr>
  </tbody>
</table>
```

---

## Responsive Tables

Large tables on small screens require special handling.

### Option 1: Horizontal Scroll with Keyboard Access

```html
<div
  role="region"
  aria-label="Q4 Sales Data table — scroll horizontally to see all columns"
  tabindex="0"
  style="overflow-x: auto;"
>
  <table>
    <!-- table content -->
  </table>
</div>
```

`tabindex="0"` makes the scroll container keyboard focusable, so keyboard users can scroll horizontally.

### Option 2: Stacked Cards at Small Breakpoints

```css
@media (max-width: 600px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }

  thead tr {
    position: absolute;
    top: -9999px;
    left: -9999px;
    /* Visually hide the header row */
  }

  tr {
    border: 1px solid #ccc;
    margin-bottom: 16px;
    padding: 8px;
  }

  td {
    padding: 4px 8px 4px 50%;
    position: relative;
  }

  /* Use data-label attribute to show column header as a pseudo-element */
  td::before {
    content: attr(data-label);
    position: absolute;
    left: 8px;
    font-weight: bold;
  }
}
```

```html
<tr>
  <td data-label="Region">North America</td>
  <td data-label="Revenue">$4.2M</td>
  <td data-label="Growth">+12%</td>
</tr>
```

**Note:** Stacked card approach hides the `<thead>` visually but it still exists in the DOM for screen readers.

---

## Table with Expandable Rows

```html
<table aria-label="Order details">
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col">Order ID</th>
      <th scope="col">Date</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <button
          type="button"
          aria-expanded="false"
          aria-controls="order-123-details"
          aria-label="Show details for order 123"
        >
          ▶
        </button>
      </td>
      <td>123</td>
      <td>Mar 10</td>
      <td>$45.00</td>
    </tr>
    <tr id="order-123-details" hidden>
      <td colspan="4">
        <dl>
          <dt>Items:</dt>
          <dd>Widget A × 2, Widget B × 1</dd>
          <dt>Shipping:</dt>
          <dd>Standard (3-5 days)</dd>
        </dl>
      </td>
    </tr>
  </tbody>
</table>
```

---

## Common Table Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| `<td>` used for headers | Cells not recognized as headers | Use `<th scope="col|row">` |
| No caption | Table lacks accessible name | Add `<caption>` or `aria-label` |
| `scope` on data cells | Invalid | Only use `scope` on `<th>` |
| Layout table with `role="table"` | Confusing table semantics | Use `role="presentation"` on layout tables |
| Merged cells without `id/headers` | AT can't associate cell with headers | Use `id` on each header, `headers` on cells |
| No `aria-sort` on sorted column | Sort state not announced | Add `aria-sort` to sorted `<th>` |
| Zebra striping only to distinguish rows | Color-only distinction | Add row headers or visible row separators |
