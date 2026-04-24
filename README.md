# NexaCloud GRC Risk Register

A security risk register I built as part of my GRC learning project.
Mapped 10 security risks to NIST SP 800-53 Rev 5 controls.

## What it does
- Scores each risk using likelihood x impact (1-5 scale)
- Rates risks as CRITICAL, HIGH, MEDIUM or LOW
- Sorts highest risk first
- Exports results to CSV
- Builds a colour coded Excel spreadsheet

## Frameworks used
- NIST SP 800-53 Rev 5
- ISO 27001 risk methodology
- OWASP Top 10 (for application risks)

## Files
- risk_scorer.py — main scoring script
- build_excel.py — builds the formatted Excel file
- risk_register_output.csv — sample output

## About
Built by Uttam Yadav — 2nd year Cyber Security & Networks student at UEL
Aiming to become a Cloud Security Engineer
