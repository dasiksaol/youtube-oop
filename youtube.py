class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.account = acctName
        print(f"\nAccount '{self.account}' created \nBalance: ${self.balance:.2f}")     

    def getBalance(self):
        print(f"\nAccount '{self.account}' \nBalance: ${self.balance:.2f}")     

    def deposit(self, amount):
        self.balance += amount
        print(f"\n${amount:.2f} Deposited.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nInsufficient Amount (${amount}) \nCurrent Balance = ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n${amount:.2f} withdrawn.")
            self.getBalance
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Completed ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer Interrupted.❌: {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit Completed.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")