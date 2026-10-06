from bank import BankAccount

accounts = {}

def create_account():
    name = input("Enter your name: ")
    
    account_number = str(100000 + len(accounts)
+ 1)
    account = BankAccount(
        name,
        account_number
    )
    
    accounts[account_number] = account
    
    print("\nAccount created successfully!")
    print(f"Account number: {account_number}")
    
def find_account():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return None
    return accounts[account_number]

while True:
    
    print("\n===== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transaction history")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        account = find_account()

        if account:
            try:
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        account = find_account()

        if account:
            try:
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        account = find_account()

        if account:
            account.get_balance()
            print()

    elif choice == "5":
        account = find_account()

        if account:
            account.show_transactions()

    elif choice == "6":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid option.")