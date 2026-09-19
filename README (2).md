# CodeAlpha_TaskAutomation

**CodeAlpha Python Programming Internship — Task 3**

Automates a real-life repetitive task: extracting all email addresses from
a `.txt` file and saving them to another file.

## How to run
```bash
python email_extractor.py
```
When prompted, enter the path to a `.txt` file (or press Enter to use the
included `sample_input.txt`). The script finds all unique email addresses
and writes them to an output file (default: `extracted_emails.txt`).

## Features
- Regex-based email detection
- Removes duplicates and sorts results
- Handles missing files gracefully
- Includes a sample input file for quick testing

## Concepts used
`os`, `re`, file handling.
