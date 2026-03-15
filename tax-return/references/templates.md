# Tax Return Templates

Use these templates to bootstrap a new tax workspace or normalize an existing one.

## Folder Structure

```text
00_INBOX
01_PERSONAL_1040
  01_W2
  02_HEALTH_HSA
  03_HOME_MORTGAGE_PROPERTY
  04_CHILDCARE
  05_VEHICLE_MILEAGE
  06_BANK_ACTIVITY
  07_INVESTMENTS_INTEREST_CRYPTO
02_<ENTITY_1>
  01_INCOME
  02_EXPENSES
  03_BANK_CARD_STATEMENTS
  04_MILEAGE
  05_WORKPAPERS
03_<ENTITY_2>
  01_INCOME_PLATFORMS
  02_BANK_STATEMENTS
  03_MORTGAGE_TAX_INSURANCE
  04_BOOKINGS_OCCUPANCY
  05_EXPENSES
  06_WORKPAPERS
04_SHARED_WORKPAPERS
  01_COMBINED_EXPORTS
99_REVIEW_HOLD
  02_NON_TAX_REFERENCE
```

Adjust the entity folder names to match the actual businesses or properties.

## File Naming

Use:

`[Year] - [Entity] - [Document Type] - [Detail].ext`

Examples:

- `2025 - Personal - W2 - Employer - Aaron.pdf`
- `2025 - Personal - 1099-INT - Bank.pdf`
- `2025 - Business - 1099-NEC - Client.pdf`
- `2025 - Rental - Occupancy Summary.md`
- `2025 - Business - Checking Activity Export.csv`

## Standard Workpapers

Create these only when they are useful:

- initial summary by entity
- investment and interest summary
- HSA activity summary
- checking activity summary
- card expense summary
- merchant summary
- occupancy summary
- mileage detail split by entity
- manual read queue
- CPA note for form conflicts or filing-treatment questions

## Master Memo Outline

Use one summary document at the end with sections like:

1. packet structure
2. household and entity snapshot
3. personal return documents on file
4. property and mortgage mapping
5. business facts on file
6. rental facts on file
7. key supporting workpapers
8. CPA review items
9. only-if-they-exist follow-up items

## End Checklist

Before calling the packet ready, confirm:

- all known W-2s and 1099s are filed
- personal, business, and rental items are separated
- large income amounts tie to forms, deposits, or platform summaries
- major expenses have statements, invoices, or documented notes
- rental occupancy and personal-use facts are recorded
- image-only forms are transcribed into the manual read queue
- unresolved treatment questions are explicitly flagged for CPA review
- only one master memo remains in the CPA-facing packet
- the upload package is readable in Google Drive when requested
