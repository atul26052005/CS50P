import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Error: File must have a .csv extension")

    try:
        print(read_and_format_csv(filename))
    except FileNotFoundError:
        sys.exit("Error: File not found")

def read_and_format_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        table = [row for row in reader]

    return tabulate(table, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()
