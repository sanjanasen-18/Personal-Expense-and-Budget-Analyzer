"""
Personal Expense and Budget Analyzer
Course: 2026CSAE100 

"""

import csv
import os
from datetime import date

DATA_FILE = "expenses.csv"
CSV_FIELDS = ["date", "amount", "category", "description"]


def load_expenses(filename=DATA_FILE):
    """Load saved expense records from a CSV file."""
    expenses = []
    if not os.path.exists(filename):
        return expenses

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row["amount"])
                    if amount <= 0:
                        continue
                    expenses.append({
                        "date": row.get("date", ""),
                        "amount": amount,
                        "category": row.get("category", "").strip(),
                        "description": row.get("description", "").strip()
                    })
                except (ValueError, TypeError, KeyError):
                    continue
    except OSError as error:
        print("Could not read the expense file:", error)

    return expenses


def save_expense(expense, filename=DATA_FILE):
    """Append one expense to the CSV file."""
    file_exists = os.path.exists(filename)
    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()
            writer.writerow(expense)
        return True
    except OSError as error:
        print("Could not save the expense:", error)
        return False


def calculate_total(expenses):
    """Return the sum of all expense amounts."""
    total = 0.0
    for expense in expenses:
        total += float(expense["amount"])
    return total


def calculate_remaining_budget(budget, expenses):
    """Return monthly budget minus total expenses."""
    return float(budget) - calculate_total(expenses)


def calculate_category_totals(expenses):
    """Return a dictionary containing total spending in each category."""
    totals = {}
    for expense in expenses:
        category = expense["category"].strip().title()
        totals[category] = totals.get(category, 0.0) + float(expense["amount"])
    return totals


def highest_spending_category(expenses):
    """Return (category, amount), or (None, 0) when there are no expenses."""
    totals = calculate_category_totals(expenses)
    if not totals:
        return None, 0.0
    category = max(totals, key=totals.get)
    return category, totals[category]


def get_positive_amount(message):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            print("Please enter an amount greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense(expenses):
    """Take expense details, save them, and add them to the current list."""
    amount = get_positive_amount("Enter expense amount (Rs.): ")

    category = input("Enter category (Food/Travel/Shopping/Education etc.): ").strip()
    while category == "":
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()
    if description == "":
        description = "Not specified"

    expense = {
        "date": date.today().isoformat(),
        "amount": amount,
        "category": category.title(),
        "description": description
    }

    if save_expense(expense):
        expenses.append(expense)
        print("Expense added and saved successfully.")


def view_expenses(expenses):
    """Display all saved expenses."""
    print("\n---------- ALL EXPENSES ----------")
    if len(expenses) == 0:
        print("No expenses have been recorded.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['date']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['category']} | {expense['description']}"
        )


def show_summary(budget, expenses):
    """Display total, remaining budget, category totals and budget alert."""
    total = calculate_total(expenses)
    remaining = calculate_remaining_budget(budget, expenses)

    print("\n---------- EXPENSE SUMMARY ----------")
    print(f"Monthly Budget     : Rs. {budget:.2f}")
    print(f"Total Expenses     : Rs. {total:.2f}")
    print(f"Remaining Budget   : Rs. {remaining:.2f}")

    if total > budget:
        print("BUDGET ALERT: You have exceeded your monthly budget!")
    elif total == budget:
        print("You have used your complete monthly budget.")
    else:
        print("You are within your monthly budget.")

    category_totals = calculate_category_totals(expenses)
    if category_totals:
        print("\nCategory-wise Spending:")
        for category, amount in sorted(category_totals.items()):
            print(f"{category}: Rs. {amount:.2f}")

        category, amount = highest_spending_category(expenses)
        print(f"\nHighest Spending Category: {category} (Rs. {amount:.2f})")


def main():
    print("======================================")
    print(" PERSONAL EXPENSE AND BUDGET ANALYZER")
    print("======================================")

    budget = get_positive_amount("Enter your monthly budget (Rs.): ")
    expenses = load_expenses()
    print(f"{len(expenses)} previously saved expense(s) loaded.")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(budget, expenses)
        elif choice == "4":
            print("Thank you for using Expense Analyzer!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
