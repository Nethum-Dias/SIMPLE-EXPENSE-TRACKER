print("========================")
print("PERSONAL FINANCE TRACKER")
print("========================")

balance = 0
transactions = []

while True:
    print("\n=== MENU ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")
    
    choice = input("choose an option:").strip()

    if choice == "5":
        print("Goodbye! Stay financially smart")
        break

    if choice == "1":
       amount = float(input("Enter income amount: "))
       balance = balance + amount
       transactions.append("Income:" + str(amount))
       print("Income added sucessfully")
       print("------------------------")
    elif choice == "2":
        try:
           amount = float(input("Enter expense amount: "))
           balance = balance - amount
           transactions.append("Expense: " + str(amount))
           print("Expense added sucessfully")
           print("-------------------------")
        except ValueError:
            print("Please enter a valid number")
    elif choice == "3":
        print("Current Balance:", balance)
        print("-------------------------")
    elif choice == "4":
        print("\n=== TRANSACTIONS ===")
        for item in transactions:
             print(item)
             print("------------")
    elif choice == "4":
        print("\n=== TRANSACTIONS ===")
        
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for iteam in transactions:
                print("-", item)
    else:
         print("Invalid option. Please choose 1-5")