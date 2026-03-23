#In OOPs, we have 3 types of methods:
#Instance method, class method and static method

class Bank:
    #class variable
    bank_name = "SBI"
    branch = "Hesaragatta"
    total_accounts = 0

    def __init__(self, name, email, phone, address, type_of_account):
        #instance variables
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.type_of_account = type_of_account
        self.balance = 0

    #instance method
    def createAccount(self):
        import random
        print(f"Thank you for creating in {Bank.bank_name} bank, Check your account details given below: \n")

        ac_number = random.randint(1000000000, 9999999999)

        print(f"Name: {self.name}\n Email: {self.email}\n Phone: {self.phone}\n Address: {self.address}\n Type of Account: {self.type_of_account}\n")
        Bank.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited {amount} in your account")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You have withdrawn {amount} from your account")
        else:
            print("Insufficient balance")

    def checkBalance(self):
        print(f"Your current balance : Rs.{self.balance}/-")

    #class method
    #decorator is a special symbol used for some purpose

    @classmethod
    def number_of_accounts(cls):
        print(f"Total number of accounts in {cls.bank_name} bank is {cls.total_accounts}")

    #static method:
    #Static method does not require any default parameter, if given it accepts any parametr
    @staticmethod
    def enquiry():
        print("For any enquiry, please contact us at 1800-123-456 or email us at support@sbi.com")


#New Account - object Creation
cust1 = Bank(name = "Dhari", email = "dhari@sbi.com", phone = "9876543210", address = "Bangalore", type_of_account = "Savings")

cust2 = Bank(name = "Preetham", email = "preetham@sbi.com", phone = "9876543211", address = "Mysore", type_of_account = "Current")

cust1.createAccount()
cust1.deposit(5000)
cust1.withdraw(2000)
cust1.checkBalance()

print("\n")

cust2.createAccount()
cust2.deposit(10000)
cust2.withdraw(5000)
cust2.checkBalance()

Bank.number_of_accounts()
Bank.enquiry()
