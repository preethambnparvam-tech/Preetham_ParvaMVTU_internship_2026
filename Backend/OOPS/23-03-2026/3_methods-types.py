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
        print("For any enquiry, please contact us at 1800-123-456 or email us at support@sbi.com \n")


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

# Employee
# name, dob, email, phone, education, skills[list]

# registration - generate id for employee and add to some dept

# assign some work

# employee work on that and mentions the time taken for work
def generate_employee_id():
    import random
    return random.randint(1000, 9999)

class Employee:
    def __init__(self, name, dob, email, phone, education, skills):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.education = education
        self.skills = skills

    def registration(self, department):
        self.employee_id = generate_employee_id()
        self.department = department
        print(f"Employee {self.name} has been registered in {self.department} department with employee ID: {self.employee_id}")

    def assignWork(self, work):
        self.work = work
        print(f"Employee {self.name} has been assigned the work: {self.work}")

    def workOnTask(self, time_taken):
        print(f"Employee {self.name} has completed the work: {self.work} in {time_taken} \n")

employee1 = Employee(name = "Dhari", dob = "01-01-1990", email = "dhari@company.com", phone = "9876543210", education = "B.Tech", skills = ["Python", "Java"])

employee2 = Employee(name = "Preetham", dob = "01-01-1992", email = "preetham@company.com", phone = "9876543211", education = "M.Tech", skills = ["Python", "C++"])

employee3 = Employee(name = "Ravi", dob = "01-01-1994", email = "ravi@company.com", phone = "9876543212", education = "B.Tech", skills = ["Python", "JavaScript"])

employee1.registration(department = "IT")
employee1.assignWork(work = "Develop a web application")
employee1.workOnTask(time_taken = "5 days") 


employee2.registration(department = "IT")
employee2.assignWork(work = "Debug the application")
employee2.workOnTask(time_taken = "3 days") 


employee3.registration(department = "HR")
employee3.assignWork(work = "Conduct interviews")
employee3.workOnTask(time_taken = "2 days") 

