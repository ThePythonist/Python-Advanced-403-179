class Account:
    def __init__(self, name, id, bank, balance):
        self.name = name
        self.id = id
        self.bank = bank
        self.balance = balance

    def show_balance(self):
        # Karmozd daryaft mojodi
        if self.balance > 0.20:
            print(f"Your current account balance is {self.balance}$")
        else:
            print("Transaction Failed")

    def deposit(self, value):
        if value > 0:
            self.balance += value
            print(f"Deposit to {self.id} : {value}$")
            self.show_balance()
        else:
            print("Transaction Failed : Value must be greater than 0")

    def withdraw(self, value):
        if self.balance > value:
            self.balance -= value
            print(f"Withdraw from {self.id} : {value}$")
            self.show_balance()
        else:
            print("Transaction Failed : You don't have enough money 😂👍")


mamad = Account("Mohammad Razavi", 101021, "Pasargad", 0)
mamad.deposit(500)
mamad.withdraw(499)
