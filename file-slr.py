import json
import os

# Default budget tracker file path
file_path = 'budget_tracker.json'


class Transaction:
    def __init__(self, category, amount, type):
        self.category = category
        self.amount = amount
        self.type = type


class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.budget = 0

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if transaction.type == 'income':
            self.budget += transaction.amount
        else:
            self.budget -= transaction.amount

    def calculate_budget(self):
        income = 0
        expenses = {}
        for transaction in self.transactions:
            if transaction.type == 'income':
                income += transaction.amount
            else:
                if transaction.category in expenses:
                    expenses[transaction.category] += transaction.amount
                else:
                    expenses[transaction.category] = transaction.amount
        for category, amount in expenses.items():
            print(f"{category}: {amount}")
        self.budget = income - sum(expenses.values())
        print(f"Remaining Budget: {self.budget}")

    def save_to_file(self):
        with open(file_path, 'w') as f:
            json.dump([transaction.__dict__ for transaction in self.transactions], f)

    def load_from_file(self):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    transaction = Transaction(item['category'], item['amount'], item['type'])
                    self.add_transaction(transaction)


def main():
    tracker = BudgetTracker()
    tracker.load_from_file()
    while True:
        print("\n1. Add Transaction")
        print("2. Calculate Budget")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))
            type = input("Enter Type (income/expense): ")
            transaction = Transaction(category, amount, type)
            tracker.add_transaction(transaction)
            tracker.save_to_file()
        elif choice == '2':
            tracker.calculate_budget()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()