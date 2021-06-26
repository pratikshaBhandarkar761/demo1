import sys


class Customer:
    bank_name = "PythonByKiran Bank"

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"Hello {self.name} Your bank balance is {self.balance}")
        print("-" * 70)

    def deposite(self, amt):
        self.balance = self.balance + amt
        print(f'After Deposite your bank balance is : {self.balance}')
        print("-" * 70)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Sorry can not Process your bank balance is not sufficient...")
            sys.exit()

        else:
            self.balance = self.balance - amt
            print(f'After withdraw your bank balance is : {self.balance}')
            print("-" * 70)

    @classmethod
    def get_bank_name(cls):
        print("=" * 70)
        print(f'                         Welcome To {cls.bank_name}')
        print("=" * 70)
obj =Customer(input("Enter name"))
while True:

    print("""
        D- Deposite
        W- Withdraw
        B- Check Balance
        E- Exit
    """)
    print("-" * 70)

    choice = input("Enter your choice: ")

    if choice.lower() == "d":
        amt = eval(input("Enter The amount to deposite: "))
        obj.deposite(amt)

    elif choice.lower() == "w":
        amt = eval(input("Enter The amount to withdraw: "))
        obj.withdraw(amt)

    elif choice.lower() == "b":
        obj.check_balance()

    elif choice.lower() == "e":
        sys.exit()

    else:
        print("Please enter valid choice")