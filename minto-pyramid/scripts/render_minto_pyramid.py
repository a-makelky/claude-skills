#!/usr/bin/env python3
"""Render a Minto Pyramid analysis JSON file as a standalone HTML artifact."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


VALID_STRENGTHS = {"strong", "weak", "missing"}


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "minto-pyramid"


def normalize_strength(value: Any) -> str:
    strength = str(value or "missing").lower().strip()
    return strength if strength in VALID_STRENGTHS else "missing"


def render(data: dict[str, Any]) -> str:
    topic = esc(data.get("topic_title") or "Untitled")
    answer = esc(data.get("level_1_answer") or "")
    arguments = data.get("arguments") or []
    plan = data.get("plan") or []

    if not answer:
        raise ValueError("level_1_answer is required")
    if not 2 <= len(arguments) <= 4:
        raise ValueError("arguments must contain 2 to 4 items")

    argument_cards = []
    evidence_cards = []
    for index, item in enumerate(arguments, start=1):
        claim = esc(item.get("claim") or "")
        evidence = esc(item.get("evidence") or "")
        strength = normalize_strength(item.get("strength"))
        argument_cards.append(
            f"""
            <section class="card argument">
              <span class="label">Argument {index}</span>
              <p>{claim}</p>
            </section>
            """
        )
        evidence_cards.append(
            f"""
            <section class="card evidence {strength}">
              <span class="label">Evidence {index}: {strength}</span>
              <p>{evidence}</p>
            </section>
            """
        )

    plan_items = []
    for index, item in enumerate(plan, start=1):
        headline = esc(item.get("headline") or f"Step {index}")
        body = esc(item.get("body") or "")
        example = esc(item.get("example") or "")
        example_html = f'<blockquote>{example}</blockquote>' if example else ""
        plan_items.append(
            f"""
            <li>
              <span class="step-number">{index}</span>
              <div>
                <h3>{headline}</h3>
                <p>{body}</p>
                {example_html}
              </div>
            </li>
            """
        )

    opener_context = esc(data.get("opener_context") or "")
    opener_quote = esc(data.get("opener_quote") or "")
    opener_note = esc(data.get("opener_note") or "")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Minto Pyramid: {topic}</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f7f4ee;
      --ink: #1f2933;
      --muted: #667085;
      --line: #d8d2c8;
      --paper: #ffffff;
      --answer: #111827;
      --argument: #eff6ff;
      --argument-border: #2f6fed;
      --strong: #e8f7ef;
      --strong-border: #148a55;
      --weak: #fff6db;
      --weak-border: #b7791f;
      --missing: #ffecec;
      --missing-border: #c2410c;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 40px 20px 56px;
    }}
    header {{
      margin-bottom: 28px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(32px, 5vw, 56px);
      line-height: 1;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 34px 0 14px;
      font-size: 22px;
      letter-spacing: 0;
    }}
    h3 {{
      margin: 0 0 6px;
      font-size: 16px;
      letter-spacing: 0;
    }}
    p {{
      margin: 0;
    }}
    .subtitle {{
      color: var(--muted);
      font-size: 16px;
    }}
    .pyramid {{
      display: grid;
      gap: 14px;
    }}
    .tier {{
      display: flex;
      gap: 14px;
      justify-content: center;
      flex-wrap: wrap;
    }}
    .card {{
      border: 1px solid var(--line);
      background: var(--paper);
      border-radius: 8px;
      padding: 18px;
    }}
    .answer {{
      max-width: 760px;
      margin: 0 auto;
      background: var(--answer);
      color: white;
      text-align: center;
    }}
    .argument {{
      flex: 1 1 240px;
      min-width: 220px;
      border-color: var(--argument-border);
      background: var(--argument);
    }}
    .evidence {{
      flex: 1 1 240px;
      min-width: 220px;
    }}
    .evidence.strong {{
      border-color: var(--strong-border);
      background: var(--strong);
    }}
    .evidence.weak {{
      border-color: var(--weak-border);
      background: var(--weak);
    }}
    .evidence.missing {{
      border-color: var(--missing-border);
      background: var(--missing);
    }}
    .label {{
      display: block;
      margin-bottom: 8px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}
    .opener {{
      display: grid;
      gap: 12px;
      border-left: 4px solid var(--argument-border);
    }}
    .quote {{
      font-size: 22px;
      font-weight: 700;
    }}
    ol.plan {{
      display: grid;
      gap: 12px;
      padding: 0;
      list-style: none;
      counter-reset: plan;
    }}
    .plan li {{
      display: grid;
      grid-template-columns: 44px minmax(0, 1fr);
      gap: 14px;
      align-items: start;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
    }}
    .step-number {{
      display: inline-grid;
      width: 34px;
      height: 34px;
      place-items: center;
      border-radius: 999px;
      background: var(--answer);
      color: white;
      font-weight: 700;
    }}
    blockquote {{
      margin: 10px 0 0;
      padding: 10px 12px;
      border-left: 3px solid var(--argument-border);
      background: rgba(47, 111, 237, .08);
    }}
    @media (max-width: 700px) {{
      main {{ padding: 28px 14px 40px; }}
      .tier {{ display: grid; }}
      .argument, .evidence {{ min-width: 0; }}
      .plan li {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Minto Pyramid: {topic}</h1>
      <p class="subtitle">Answer, support, evidence, and the repair plan in one view.</p>
    </header>

    <section class="pyramid" aria-label="Minto pyramid">
      <div class="tier">
        <section class="card answer">
          <span class="label">The Answer</span>
          <p>{answer}</p>
        </section>
      </div>
      <div class="tier">
        {''.join(argument_cards)}
      </div>
      <div class="tier">
        {''.join(evidence_cards)}
      </div>
    </section>

    <h2>Opener</h2>
    <section class="card opener">
      <p>{opener_context}</p>
      <p class="quote">"{opener_quote}"</p>
      <p>{opener_note}</p>
    </section>

    <h2>Restructuring Plan</h2>
    <ol class="plan">
      {''.join(plan_items)}
    </ol>
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_html", type=Path, nargs="?")
    args = parser.parse_args()

    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    output = args.output_html
    if output is None:
        title = data.get("topic_title") or "minto-pyramid"
        output = args.input_json.with_name(f"minto-pyramid-{slugify(str(title))}.html")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(data), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
