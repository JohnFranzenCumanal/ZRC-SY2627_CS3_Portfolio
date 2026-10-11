class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    # Setter for account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Setter for balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must not be a negative number.")

    # Getter for account number
    @property
    def account_number(self):
        return self.__account_number

    # Getter for balance
    @property
    def balance(self):
        return self.__balance


# Create an object of BankAccount
acc = BankAccount(12345, 1000)

print("Object of class BankAccount")
print()
print("Account 1")
print(f"Account Number: {acc.account_number}")
print(f"Balance: {acc.balance}")

print()
print("Update balance to -100")
acc.set_balance(-100)

print(f"Account Number: {acc.account_number}")
print(f"Balance: {acc.balance}")
