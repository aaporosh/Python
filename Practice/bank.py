class InsufficientBalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance= balance
    def withdraw(self, amount):
        if self.balance<amount:
            raise InsufficientBalanceException
        print(self.balance - amount)
try:
    b = BankAccount(5000)
    b.withdraw(10000)
except InsufficientBalanceException:
    print("Error occured")
