import os

def main():
    load_from_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Save and Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# List to store expenses
expenses = []

# Load expenses from file (if exists)
def load_from_file():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                description, amount = line.strip().split(" - $")
                expenses.append((description, float(amount)))

# Save expenses to a file
def save_to_file():
    with open("expenses.txt", "w") as file:
        for description, amount in expenses:
            file.write(f"{description} - ${amount:.2f}\n")
    print("Expenses saved successfully!")

# Add a new expense
def add_expense():
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: $"))
        expenses.append((description, amount))
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nList of Expenses:")
    for i, (description, amount) in enumerate(expenses, 1):
        print(f"{i}. {description} - ${amount:.2f}")
    print()

# Calculate total expenses
def calculate_total():
    total = sum(amount for _, amount in expenses)
    print(f"Total expenses: ${total:.2f}")

# Main menu

# Run the application
if __name__ == "__main__":
    main()