# private_access.py
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # Private
        self.__pin = 1234           # Private

    # Getter - to READ private data
    def get_balance(self):
        return f"Balance: ${self.__balance}"

    # Setter - to UPDATE private data
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
            print(f"Balance updated to ${self.__balance}")
        else:
            print("Invalid amount!")

    def check_pin(self, pin):
        if pin == self.__pin:
            print("✅ PIN correct!")
        else:
            print("❌ Wrong PIN!")

# Test
account = BankAccount("Ashok", 1000)

# ✅ Access through methods
print(account.get_balance())
account.set_balance(2000)
account.check_pin(1234)
account.check_pin(9999)

# ❌ Direct access - gives ERROR
# print(account.__balance)   # AttributeError!