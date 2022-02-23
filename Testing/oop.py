class BankAcc:

    def __init__(self, name,balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name is", self.name)
        print("balance is", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("remaining balance is=",self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("current balance is=",self.balance)


b1 = BankAcc("ajay",5000)
b1.display()
b1.withdraw(2000)
b1.display()
b1.deposit(1000)
b1.display()
