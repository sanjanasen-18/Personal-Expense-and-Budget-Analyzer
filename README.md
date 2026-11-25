PERSONAL EXPENSE AND BUDGET ANALYZER

**Course:** Computational Thinking and Programming  
**Course code:** 2026CSAE100   
**Academic year:** 2026–27

## Project description
A Python program that records personal expenses, organizes them by category,
calculates total spending and remaining monthly budget, identifies the highest-spending
category, and displays an alert when spending exceeds the budget.

## Features
1. Add expenses with date, amount, category and description.
2. Save expenses permanently in a CSV file.
3. View all saved expenses.
4. Calculate total expenses and remaining budget.
5. Display category-wise spending.
6. Identify the highest-spending category.
7. Display an alert if expenses exceed the monthly budget.
8. Validate incorrect amounts and menu choices.

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   `python expense_analyzer_.py`

   On some Windows computers use:

   `py expense_analyzer_.py`

4. Enter your monthly budget and select an option from the menu.
5. The program creates `expenses.csv` automatically when the first expense is saved.

## How to run automated tests
Run:

`python -m unittest -v`

## Project files
- `expense_analyzer_.py` – main application.
- `test_expense_analyzer_.py` – automated unit tests.
- `README.md` – project details and instructions.
- `.gitignore` – files that should not be uploaded.
- `screenshots/` – add genuine screenshots of the program running.

## Example test data
For a budget of Rs. 10,000:
- Food: Rs. 500
- Travel: Rs. 1,200
- Expected total: Rs. 1,700
- Expected remaining budget: Rs. 8,300

## Team
- Sarthak (S26CSEU0409) – testing, integration and documentation.
- Riddhima Gupta (S26CSEU0300) – expense analysis and budget calculation.
- Sanjana Sen (S26CSEU0290) – user input and expense recording.

## Website link
Click here to visit our website:
[Personal Expense and Budget Tracker](./ expense_budget_analyzer_website.html)