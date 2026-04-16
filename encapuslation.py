# 3_encapsulation.py
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        return f"{self.owner}'s Balance: ${self.__balance}"

# Test
account = BankAccount("Ashok", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
account.withdraw(2000)