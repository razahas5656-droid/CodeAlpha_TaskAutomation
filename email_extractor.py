import os
import re

EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails_from_file(input_path):
    """Read a text file and return a sorted list of unique email addresses."""
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"No such file: {input_path}")

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    emails = EMAIL_PATTERN.findall(content)
    unique_sorted_emails = sorted(set(emails))
    return unique_sorted_emails


def save_emails(emails, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    print("=" * 45)
    print("Email Address Extractor")
    print("=" * 45)

    input_path = input("Enter path to the .txt file to scan: ").strip()
    if not input_path:
        input_path = "sample_input.txt"
        print(f"No path entered, using default: {input_path}")

    try:
        emails = extract_emails_from_file(input_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    if not emails:
        print("No email addresses found in the file.")
        return

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")

    output_path = input("\nEnter output file name (default: extracted_emails.txt): ").strip()
    if not output_path:
        output_path = "extracted_emails.txt"

    save_emails(emails, output_path)
    print(f"\nSaved {len(emails)} email(s) to {output_path}")


if __name__ == "__main__":
    main()
