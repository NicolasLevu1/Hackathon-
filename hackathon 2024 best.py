import matplotlib.pyplot as plt

# Function to add a new transaction
def add_transaction(transactions, categories):
    category = input("Enter transaction category: ")
    # Check if this category is new; if so, add it to the categories set
    if category not in categories:
        print("New category detected, adding to your list of categories.")
        categories.add(category)
    amount = float(input("Enter transaction amount: $"))
    transactions.append((category, amount))
    print("Transaction added successfully!")

# Function to show all recorded transactions
def show_transactions(transactions):
    print("\nYour transactions:")
    for category, amount in transactions:
        print(f"{category}: ${amount}")

# Function to plot spending by category using a bar chart
def plot_spending(transactions):
    categories = {}
    # Aggregate spending by category
    for category, amount in transactions:
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    
    # Plotting the aggregated data
    plt.figure(figsize=(10, 6))
    plt.bar(categories.keys(), categories.values())
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.title('Spending by Category')
    plt.xticks(rotation=45)  # Rotate category names for better visibility
    plt.show()

# The main function where the program starts
def main():
    daily_limit = float(input("Enter your daily spending limit: $"))
    total_spent_today = 0.0
    transactions = []  # List to store transactions
    categories = set()  # Set to store unique categories

    while True:
        print("\nOptions:")
        print("  1. Log a new expense")
        print("  2. Show daily summary")
        print("  3. Show transactions")
        print("  4. Plot spending by category")
        print("  5. Exit")
        action = input("Choose an action: ")

        if action == '1':
            # Add a new transaction
            add_transaction(transactions, categories)
            expense_amount = transactions[-1][1]  # Get the last entered amount
            total_spent_today += expense_amount

            # Alerts based on the spending limit
            if total_spent_today > daily_limit:
                print("Alert: You've exceeded your daily limit!")
            elif total_spent_today / daily_limit >= 0.9:
                print("Warning: You're close to reaching your daily limit.")

        elif action == '2':
            # Show a summary of today's spending
            print(f"\nDaily Limit: ${daily_limit}")
            print(f"Total Spent Today: ${total_spent_today}")
            if total_spent_today > daily_limit:
                print("You have exceeded your daily limit.")
            elif total_spent_today / daily_limit >= 0.9:
                print("You are close to reaching your daily limit.")

        elif action == '3':
            # Display all transactions
            show_transactions(transactions)
        
        elif action == '4':
            # Plot spending by category
            plot_spending(transactions)

        elif action == '5':
            # Exit the program
            print("Exiting program.")
            break

        else:
            # Handle invalid menu option entries
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()500