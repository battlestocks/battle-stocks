class Bank:
    def __init__(self, balance=10000):
        self.balance = balance 
        
    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance < amount:
            print('Not enough money, try another amount!')
        else:
            self.balance -= amount

    def get_balance(self):
        if self.balance >= 0:
            return self.balance
        elif self.balance < 0:
            return self.balance
