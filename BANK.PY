from datetime import datetime



#users of the bank


class Account:
    def __init__(self, name, account_num,account_balance):
        self.name= name
        self.account_num = account_num
        self.account_balance = account_balance

    def show_menu(self):
          return f' welcome {self.name}\n account balance is: {self.account_balance}'

    def get_balance (self):
          return f'current balance is now {self.account_balance}'

    def deposit (self, amount):
        self.account_balance += amount
        return f'Deposit Successful and Current Balance is:{self.account_balance}'

    def withdraw(self,amount):
        if amount < self.account_balance:
            x = self.account_balance - amount
            return f'Withdrawal Successful and Current Balance:{x}'
        elif amount > self.account_balance:
            return "Insufficient funds"

    def transfer(self, account, amount:float):
        if self.account_balance > amount:
            self.account_balance -= amount
            account.account_balance += amount
            return f'Transfer Successfully made to \n your balance is {self.account_balance}'
        return f'Insufficient Funds add more money madam'


f = Account('faith', "1234567890",4000)
q = Account ("QUEEN","4567890123", 5000)

print (f.show_menu())
print (f.get_balance())
print (f.deposit(9000))
print (f.withdraw(7000))

