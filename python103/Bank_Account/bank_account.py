#--------------------
#\\//\\//\\//\\//\\//
#|||| Importing |||||
#\\//\\//\\//\\//\\//
#--------------------
import random

import datetime



#--------------------
#\\//\\//\\//\\//\\//
#|||| Classes |||||||
#\\//\\//\\//\\//\\//
#--------------------

class BankAccount:

    #|=|=|=|=|=|=|
    # Constructor
    #|=|=|=|=|=|=|

    def __init__(self):

        account_number = random.randint(100000, 999999) 

        #private attributes
        self.__set_account_number(account_number)
        self.__owner_name = ""
        self.__balance = 0.0
        self.__pin = 1234
        


    
    #|=|=|=|=|=|=|
    # Setters
    #|=|=|=|=|=|=|

    def __set_account_number (self, account_number):
        if isinstance(account_number, int) and 100000 <= account_number <= 999999:
            self.__account_number = account_number
            return True
        return False
    

    def __set_owner_name(self, owner_name):
        if isinstance(owner_name, str) and owner_name.strip():
            self.__owner_name = owner_name
            return True
        return False
    

    def __set_balance(self, balance):
        try:
            balance = float(balance)
        
        except ValueError:
            return False
        
        self.__balance = balance
        return True

    




    #|=|=|=|=|=|=|
    # Getters
    #|=|=|=|=|=|=|

    def get_account_number(self):
        return self.__account_number
    
    
    def get_owner_name(self):
        return self.__owner_name
    
    def get_balance(self):
        return self.__balance
    
    def get_pin(self):
        return self.__pin
    


    #|=|=|=|=|=|=|
    # Input Method
    #|=|=|=|=|=|=|

    def input_info(self):
        while True:
            owner_name = input("Enter Owner name: ")
            if self.__set_owner_name(owner_name):
                break
            print("Invalid owner name. Please enter a valid name.")
        




    #|=|=|=|=|=|=|=|=|
    # Display Method
    #|=|=|=|=|=|=|=|=|

    def display_info(self):
        print("\n===================================") 
        print("      ACCOUNT INFORMATION")
        print("===================================")
        print(f"Account Number : {self.get_account_number()}")
        print(f"Owner Name     : {self.get_owner_name()}")
        print(f"Balance        : {self.get_balance()} SAR")
        print("===================================")


    #|=|=|=|=|=|=|=|=|
    # Deposit Method
    #|=|=|=|=|=|=|=|=|

    def deposit(self):
        amount = input("Enter the amount to deposit: ")
        now = datetime.datetime.now()

        try:
            amount = float(amount)
        
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        
        new_balance = self.get_balance() + amount
        self.__set_balance(new_balance)

        print(f"Deposited: {amount} SAR")
        print(f"Date: {now.strftime('%Y-%m-%d')}")
        print(f"Time: {now.strftime('%H:%M:%S')}")



    
    #|=|=|=|=|=|=|=|=|
    # Withdraw Method
    #|=|=|=|=|=|=|=|=|

    def withdraw(self):
        amount = input("Enter the amount to withdraw: ")
        now = datetime.datetime.now()

        try:
            amount = float(amount)
        
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        
        if amount > self.get_balance():
            print("Insufficient balance for this withdrawal.")
            return
        
        new_balance = self.get_balance() - amount
        self.__set_balance(new_balance)

        print(f"Withdrew: {amount} SAR")
        print(f"Date: {now.strftime('%Y-%m-%d')}")
        print(f"Time: {now.strftime('%H:%M:%S')}")
    

    #|=|=|=|=|=|=|=|=|
    # Login Method
    #|=|=|=|=|=|=|=|=|

    def login(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your PIN: ")

            if pin.isdigit() and int(pin) == self.get_pin():
                print("Login successful!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")

        print("Login failed.")
        return False



class SavingAccount(BankAccount):
    def display_info(self):
        print(f"\n{'=' * 10} SAVING ACCOUNT {'=' * 10}")
        super().display_info()


class CurrentAccount(BankAccount):
    def display_info(self):
        print(f"\n{'=' * 10} CURRENT ACCOUNT {'=' * 10}")
        super().display_info()










#--------------------
#\\//\\//\\//\\//\\//
#|||||| Main |||||||||
#\\//\\//\\//\\//\\//
#--------------------

print("===================================")
print("      WELCOME TO ATM SYSTEM")
print("===================================")

print("Choose Account Type")
print("1. Saving Account")
print("2. Current Account")

account_type = input("Enter your choice: ")

if account_type == "1":
    account1 = SavingAccount()
elif account_type == "2":
    account1 = CurrentAccount()
else:
    print("Invalid choice.")
    exit()

account1.input_info()

if account1.login():

    otp = random.randint(100000, 999999)

    print("\n===================================")
    print("      OTP VERIFICATION")
    print("===================================")
    print(f"Your OTP is: {otp}")

    otp_verified = False
    attempts_otp = 3

    while attempts_otp > 0:

        user_otp = input("Enter OTP: ")

        if user_otp.isdigit() and int(user_otp) == otp:
            print("OTP verification successful!")
            otp_verified = True
            break

        attempts_otp -= 1

        if attempts_otp == 0:
            print("OTP verification failed.")
            break

        print(f"Incorrect OTP. You have {attempts_otp} attempts left.")

    if otp_verified:

        while True:

            print("\n===================================")
            print("            ATM MENU")
            print("===================================")
            print("1. Display Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("===================================")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                account1.display_info()

            elif choice == "2":
                account1.deposit()

            elif choice == "3":
                account1.withdraw()

            elif choice == "4":
                print("Thank you for using our ATM.")
                break

            else:
                print("Invalid choice. Please try again.")



        
    




