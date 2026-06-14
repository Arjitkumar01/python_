class ATM:
    def withdraw(self, amount):
        self.__check_balance(amount)
        print(f"₹{amount} withdrawn successfully")

    def __check_balance(self, amount):
        print("Checking balance...")

atm = ATM()
atm.withdraw(500)

