---
name: tax-return
description: Organize annual tax documents, split personal and entity records, build reconciliation workpapers, and prepare a CPA-ready packet. Use when a user asks to set up a tax workspace, sort or rename W-2/1099/HSA/mortgage/rental files, separate business and personal activity, reconcile statements and exports, write a handoff memo, or create a Drive-friendly upload package for a tax return.
---

# Tax Return

Organize a tax-prep workspace, turn raw statements and exports into filing buckets and workpapers, and leave one clear handoff memo for the CPA or taxpayer. Prefer documented facts over assumptions and flag unresolved tax-treatment questions instead of deciding them silently.

## Core Workflow

1. Build context first.
   - Inventory the files, tax year, people, entities, properties, accounts, and filing buckets.
   - Confirm which activity is personal, which belongs to each business, and which belongs to each rental.
   - If the workspace is not structured yet, create it using `references/templates.md`.

2. Route all incoming files through intake.
   - Use `00_INBOX` as the default landing zone for every new scan, export, or statement.
   - Rename files with `[Year] - [Entity] - [Document Type] - [Detail].ext`.
   - Move duplicates, wrong-year items, ambiguous items, and non-packet reference material to `99_REVIEW_HOLD`.

3. Classify by tax bucket, not by source.
   - Separate personal forms, business forms, rental support, statements, mileage, and shared exports.
   - Keep mixed exports in shared workpapers first, then split them into entity-specific support.
   - Do not leave bank exports, notes, and platform files disconnected from the filing logic.

4. Build workpapers from raw support.
   - Reconcile income first, then expenses.
   - Compare forms to deposits and known activity.
   - Separate true expenses from transfers, credit-card payments, reimbursements, owner draws, and wrong-year charges.
   - Create concise summaries for large exports, card activity, occupancy, mileage, and image-only form transcriptions.

5. Maintain one live summary.
   - Keep one master memo only.
   - Record ownership, filing assumptions, mortgage or property mapping, off-account expenses, form conflicts, and open CPA review items.
   - Archive older planning notes once the master memo absorbs their useful content.

6. Prepare the handoff packet.
   - Give the CPA a readable folder structure plus one summary memo.
   - Exclude `00_INBOX` and `99_REVIEW_HOLD` from the CPA-facing upload package unless explicitly requested.
   - When needed, convert notes and CSV workpapers into Drive-friendly `.docx` and `.xlsx` copies while preserving the originals.

## Non-Negotiables

- Prefer organization and documentation over tax advice.
- Verify tax-treatment questions with official sources when the user asks for an actual filing rule.
- Treat bank activity as support, not automatic classification.
- Use a manual transcription log for image-only or unreadable scans.
- Preserve source files and create derived workpapers instead of mutating originals.
- Flag uncertain classification or legal treatment for CPA review instead of guessing.

## References

- `references/workflow.md` for the detailed annual playbook.
- `references/templates.md` for the folder structure, naming convention, workpaper set, handoff memo outline, and final checklist.
