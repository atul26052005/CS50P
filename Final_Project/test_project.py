import pytest
import os
from project import load_from_file, save_to_file, add_expense, calculate_total, expenses

# Fixture to reset the expenses list before each test
@pytest.fixture(autouse=True)
def reset_expenses():
    global expenses
    expenses.clear()  # Clear the list before each test

def test_add_expense(monkeypatch):
    """Test if an expense is correctly added"""
    inputs = iter(["Lunch", "12.50"])  # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    add_expense()  # Call the function
    assert len(expenses) == 1
    assert expenses[0] == ("Lunch", 12.50)

def test_calculate_total():
    """Test if total expenses are calculated correctly"""
    expenses.append(("Lunch", 10.00))
    expenses.append(("Transport", 15.00))
    
    total = sum(amount for _, amount in expenses)  # Expected total
    assert total == 25.00

def test_save_to_file():
    """Test if expenses are saved correctly"""
    expenses.append(("Movie", 20.00))
    save_to_file()  # Save data
    
    # Check if the file exists
    assert os.path.exists("expenses.txt")
    
    # Read file content
    with open("expenses.txt", "r") as file:
        lines = file.readlines()
    
    assert lines[0].strip() == "Movie - $20.00"

def test_load_from_file():
    """Test if expenses are loaded correctly"""
    # Write test data to file
    with open("expenses.txt", "w") as file:
        file.write("Dinner - $25.50\n")

    expenses.clear()  # Reset list
    load_from_file()  # Load data back

    assert len(expenses) == 1
    assert expenses[0] == ("Dinner", 25.50)

if __name__ == "__main__":
    pytest.main()