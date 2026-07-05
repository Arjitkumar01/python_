# Q3.  Create a class BankAccount with a private attribute __balance.
#      Add methods:
#        deposit(amount)   → adds to balance
#        withdraw(amount)  → deducts if sufficient, else prints error
#        get_balance()     → returns balance
#      Do NOT allow direct access to __balance from outside.

class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
        
    def set_updateBalance(self,amount):
        self.__balance+=amount
    def set_withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            return self.__balance-amount
        else :
            return f"insufficient balance"
    def get_balance(self):
        return self.__balance
    
a1 = BankAccount()
print(a1.get_balance())
a1.set_updateBalance(1000)
print(a1.get_balance())
a1.set_withdraw(200)
print(a1.get_balance())

        
        