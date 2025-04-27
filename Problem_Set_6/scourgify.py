import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        sys.exit("Error: Both files must have a .csv extension")

    try:
        process_csv(input_file, output_file)
    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' not found")

def process_csv(input_file, output_file):
    """Reads an input CSV file, processes the names, and writes a cleaned CSV file."""
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

if __name__ == "__main__":
    main()
