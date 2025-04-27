import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regex pattern for a valid IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if match:
        # Extract matched numbers and check if they are in the range [0, 255]
        return all(0 <= int(num) <= 255 for num in match.groups())

    return False

if __name__ == "__main__":
    main()
