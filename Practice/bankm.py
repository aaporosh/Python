from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class BankAccount(ABC):
    def _init_(self, account_number, account_holder, balance):
        self.__account_number = account_number  # Private attribute
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for balance (Encapsulation)
    def get_balance(self):
        return self.__balance

    # Setter for balance (Encapsulation)
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance amount!")

    # Getter for account details
    def get_account_details(self):
        return self._account_number, self._account_holder

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_balance(self):
        pass


# Derived class for Savings Account (Polymorphism)
class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance, interest_rate):
        super()._init_(account_number, account_holder, balance)
        self.__interest_rate = interest_rate  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"{amount} deposited successfully. New balance: {self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"{amount} withdrawn successfully. New balance: {self.get_balance()}")
        else:
            print("Insufficient balance or invalid withdrawal amount!")

    def display_balance(self):
        account_number, account_holder = self.get_account_details()
        print(f"Account Number: {account_number}, Account Holder: {account_holder}, Balance: {self.get_balance()}")

    def calculate_interest(self):
        interest = self.get_balance() * (self.__interest_rate / 100)
        print(f"Interest Amount: {interest}")
        return interest


# Derived class for Current Account (Polymorphism)
class CurrentAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance, overdraft_limit):
        super()._init_(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"{amount} deposited successfully. New balance: {self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() - amount >= -self.__overdraft_limit:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"{amount} withdrawn successfully. New balance: {self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit or invalid amount!")

    def display_balance(self):
        account_number, account_holder = self.get_account_details()
        print(f"Account Number: {account_number}, Account Holder: {account_holder}, Balance: {self.get_balance()}")


# Main program
def main():
    print("Welcome to the Bank Management System")

    # Create a Savings Account
    savings = SavingsAccount("SA123", "Md. Rakibul Hasan", 10000, 3.5)
    savings.deposit(2000)
    savings.withdraw(500)
    savings.display_balance()
    savings.calculate_interest()

    print("\n")

    # Create a Current Account
    current = CurrentAccount("CA456", "Md. Rakibul Hasan", 5000, 2000)
    current.deposit(1000)
    current.withdraw(6000)
    current.display_balance()


if _name_ == "_main_":
    main()