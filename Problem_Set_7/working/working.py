import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regex to match time format
    pattern = re.fullmatch(r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)', s)

    if not pattern:
        raise ValueError("Invalid time format")

    # Extracting values from regex groups
    h1, m1, period1, h2, m2, period2 = pattern.groups()

    # Convert hour and minutes to int (default minutes to 00 if not present)
    h1, m1 = int(h1), int(m1) if m1 else 0
    h2, m2 = int(h2), int(m2) if m2 else 0

    # Validate hours and minutes
    if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid time value")

    # Convert to 24-hour format
    h1 = convert_to_24h(h1, period1)
    h2 = convert_to_24h(h2, period2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def convert_to_24h(hour, period):
    """Helper function to convert 12-hour format to 24-hour format"""
    if period == "AM":
        return 0 if hour == 12 else hour
    else:  # PM case
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
