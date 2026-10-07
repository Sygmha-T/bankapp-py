class Bank_Account:
    # def creation(self):
    #     name = input("What is your name: ")
    #     age = input("How old are you: ")
    #     location = input("Where do you live: ")
    #     acct = input("Do you want a Savings or a Current account: ")
       
    #     print("Please confirm this details: ")
    #     print(f"Your name is {name}, you are {age} years old, you live in {location}, and you want to open a {acct} account")
        
    def __init__(self, name, account_number, 
balance=0):
        self.name = name
        self.account_no = account_number
        self.__balance = balance
        self.transactions =[]
        
    # def details(self):
    #     print(f"Your name is {self.name}\n"
    #           f"Your account number is {self.acct_no}\n",
    #           f"Your account balance is {self.acct_bal}")
    def deposit(self, amount):
        # self.amount = (amount)
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return
        else:
            self.acct_bal = (self.amount + self.acct_bal)
            print(f"Your new balance for {self.acct_no} is {self.acct_bal}")
            return
    def transfer(self, receiver, amount,):
        
        self.receiver = receiver
        self.amount = amount
        if amount <= 0:
            print("Transfer amount must be greater than zero")
        else:
            self.acct_bal = self.acct_bal - self.amount
            print(f"Your new balance for {self.acct_no} is {self.acct_bal}\n",
                  f"You have sent {self.amount} to {self.receiver}")
            return
    def check_balance(self, account_number):
        self.acct_no = account_number

Account1 = Bank_Account()
Account2 = Bank_Account()

Account1.creation()
print()

Account1.acct()

Account1.details()
Account2.details()
print()

Account1.deposit(int(input("How much do you want to deposit: ")))
Account2.deposit(int(input("How much do you want to deposit: ")))
#print()


Account1.transfer((input("Which account do you want to transfer to: ")),
                   int(input("How much do you want to transfer: \n"))) 

Account2.transfer((input("Which account do you want to transfer to: ")),
                   int(input("How much do you want to transfer: \n")))
print()