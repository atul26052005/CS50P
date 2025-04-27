import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Error: File must have a .py extension")

    try:
        print(count_lines(filename))
    except FileNotFoundError:
        sys.exit("Error: File not found")

def count_lines(filename):
    """Counts lines of code excluding comments and blank lines."""
    loc = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                loc += 1

    return loc

if __name__ == "__main__":
    main()
