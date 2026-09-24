class BankAccount :
    def __init__(self, acc_holder, acc_no, pin, balance):
        self.acc_holder=acc_holder
        self.acc_no=acc_no
        self.pin=pin
        self.balance=balance

    def check_balance(self):
        print(f"The balance is {self.balance}")

    def deposit(self,amount):
        if amount<=0 :
            print("The deposit amount is invalid")
        else :
            self.balance+=amount
            print(f"Amount {amount} successfully deposited")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance :
            self.balance-=amount
            print(f"Amount {amount} is successfully withdrawn")
        else :
            print("The entered withdrawal amount is invalid")



class ATM :
    def __init__(self):
        self.account=None

    def authenticate(self, obj_acc, pin_acc):
        if pin_acc==obj_acc.pin:
            self.account=obj_acc
            print("The atm is connected to the bank account")
        else :
            print("The pin entered is wrong")

    def check_balance(self) :
        if self.account==None:
            print("Authenticate first")
        else :
            self.account.check_balance()

    def withdraw(self,amount):
        if self.account==None:
            print("Authenticate first")
        else :
            self.account.withdraw(amount)

    def deposit(self,amount):
        if self.account==None:
            print("Authenticate first")
        else :
            self.account.deposit(amount)


    def logout(self):
        self.account=None
