"""
Create a bank account class that has attributes `owner`, `balance` and two methods `deposit` and `withdraw`. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
```python
class Account:
    pass
```
"""



class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money

owner = input("Enter your name: ")
balance = int(input("Enter your balance: "))
account1 = Account(owner, balance)
while True:
    n = int(input("Enter 1 to deposit, 2 to withdraw, 0 to exit: "))
    if n == 1:
        money = int(input("Enter your money: "))
        account1.deposit(money)
        print(account1.owner, account1.balance)
    elif n == 2:
        money = int(input("Enter your money: "))
        account1.withdraw(money)
        print(account1.owner, account1.balance)
    elif n == 0:
        break