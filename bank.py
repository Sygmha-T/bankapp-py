# class BankAccount:

#     def __init__(self, name, account_number, balance=0):
#         self.name = name
#         self.account_number = account_number
#         self.__balance = balance
#         self.transactions = []

#     def deposit(self, amount):

#         if amount <= 0:
#             raise ValueError(
#                 "Deposit must be greater than zero."
#             )

#         self.__balance += amount

#         self.transactions.append(
#             f"Deposit: +₦{amount}"
#         )

#     def withdraw(self, amount):

#         if amount <= 0:
#             raise ValueError(
#                 "Withdrawal must be greater than zero."
#             )

#         if amount > self.__balance:
#             raise ValueError(
#                 "Insufficient funds."
#             )

#         self.__balance -= amount

#         self.transactions.append(
#             f"Withdrawal: -₦{amount}"
#         )

#     def get_balance(self):
#         return self.__balance



import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BankAccount:
    
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        logging.info(
            f"{self.name} deposited N{amount}"
        )
        
        if amount <= 0:
            raise ValueError(
                "Deposit must be greater than zero."
            )
        self.__balance += amount
        self.transactions.append(
            f"Deposit: +N{amount}"
        )
    
    def withdraw(self, amount):
        logging.info(
            f"{self.name} withdraw N{amount}"
        )
        
        if amount <= 0:
            logging.warning(
                f"{self.name} attempted to withdraw N{amount}"
            )
            raise ValueError(
                "Withdrawal must be greater than zero."
            )
        if amount > self.__balance:
            logging.warning(
            f"{self.name} attempted to withdraw N{amount}"
            )
            raise ValueError(
                "Insufficient funds."
            )
        self.__balance -= amount
        self.transactions.append(
            f"withdrawal: -N(amount)"
        )
    def get_balance(self):
        return self.__balance
    
#Account1 = BankAccount("Sheriff", 8133484122)
#Account2 = BankAccount("Tobi", 29334493)

#Account1.deposit(int(input("How much do you want to deposit: ")))
#Account2.deposit(int(input("How much do you want to deposit: ")))
#print()


#Account1.withdraw(int(input("How much do you want to withdraw: ")))
#Account2.withdraw(int(input("How much do you want to withdraw: ")))
#print()