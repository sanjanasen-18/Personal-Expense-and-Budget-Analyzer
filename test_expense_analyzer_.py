import unittest
import tempfile
import os

from expense_analyzer import (
    calculate_total,
    calculate_remaining_budget,
    calculate_category_totals,
    highest_spending_category,
    save_expense,
    load_expenses
)


class ExpenseAnalyzerTests(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"date": "2026-11-18", "amount": 500, "category": "Food", "description": "Lunch"},
            {"date": "2026-11-18", "amount": 1200, "category": "Travel", "description": "Cab"},
            {"date": "2026-11-18", "amount": 300, "category": "Food", "description": "Snacks"}
        ]

    def test_total_of_multiple_expenses(self):
        self.assertEqual(calculate_total(self.expenses), 2000)

    def test_remaining_budget_normal_case(self):
        self.assertEqual(calculate_remaining_budget(10000, self.expenses), 8000)

    def test_budget_boundary_equal_to_expenses(self):
        self.assertEqual(calculate_remaining_budget(2000, self.expenses), 0)

    def test_budget_exceeded(self):
        self.assertEqual(calculate_remaining_budget(1500, self.expenses), -500)

    def test_category_totals(self):
        totals = calculate_category_totals(self.expenses)
        self.assertEqual(totals["Food"], 800)
        self.assertEqual(totals["Travel"], 1200)

    def test_highest_spending_category(self):
        self.assertEqual(highest_spending_category(self.expenses), ("Travel", 1200))

    def test_empty_expenses(self):
        self.assertEqual(calculate_total([]), 0)
        self.assertEqual(highest_spending_category([]), (None, 0.0))

    def test_csv_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test_expenses.csv")
            item = self.expenses[0]
            self.assertTrue(save_expense(item, path))
            loaded = load_expenses(path)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]["category"], "Food")
            self.assertEqual(loaded[0]["amount"], 500)


if __name__ == "__main__":
    unittest.main()
