from youtube import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

# Dave.getBalance()
# Sarah.getBalance()

# Sarah.deposit(500)

# Dave.withdraw(1200)
# Sarah.deposit(500)

# Dave.transfer(10000, Sarah)
# Dave.transfer(1000, Sarah)

# Jim = InterestRewardsAcct(1000, "Jim")

# Jim.getBalance()    

# Jim.deposit(100)

# Jim.transfer(100, Dave)

# Dave.getBalance()
# Jim.getBalance()

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, "Sarah")
