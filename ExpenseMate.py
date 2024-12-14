def expense_tracker():
    expenses = []

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense  2. View Expenses  3. Total Expenses  4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            expenses.append({"description": description, "amount": amount})
            print("Expense added successfully.")
        elif choice == '2':
            print("\nExpenses:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense['description']} - ${expense['amount']:.2f}")
        elif choice == '3':
            total = sum(expense['amount'] for expense in expenses)
            print(f"Total Expenses: ${total:.2f}")
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

expense_tracker()
