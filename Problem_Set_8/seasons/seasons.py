from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = [int(x) for x in input("Date of Birth: ").split("-")]
        dob = check_birthdate(year, month, day)  # This will raise ValueError if invalid
        diff_minutes = calculate_diff(dob)
        words = p.number_to_words(diff_minutes, andword="")
        print(words.capitalize() + " minutes")
    except ValueError:
        sys.exit("Invalid Date")

def check_birthdate(year, month, day):
    """Check if a valid birthdate is provided, else raise ValueError"""
    try:
        return date(year, month, day)  # This will raise ValueError for invalid dates
    except ValueError:
        raise ValueError("Invalid Date")  # Raise an exception instead of returning a string

def calculate_diff(dob):
    """Calculate the difference in minutes"""
    return str(((date.today() - dob).days) * 24 * 60)

if __name__ == "__main__":
    main()
