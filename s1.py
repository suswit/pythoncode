# # import tkinter
# # m=tkinter .Tk()
# # '''
# # widgets are added here 
# # '''
# # m.mainloop()

# # import tkinter as tk

# # main=tk.Tk(className="emi calculator")
# # main.geometry("600x600")

# # label1=tk.Label(main,text="python")
# # txt1=tk.Entry(main)
# # btn1=tk.Button(main,text="submit")

# # label1.grid(row=0,column=0)
# # txt1.grid(row=0,column=1)
# # btn1.grid(row=1,column=1)

# # main.mainloop()

# # def my_function():
# #     '''Demonstrate triple double quotes
# #     docstrings and does nothing really.'''

# #     return None

# # print("Using_Doc_:")
# # print(my_function.__doc__)

# # print("Using help:")
# # help(my_function)

# # def cube(y):
# #     return y*y*y

# # lambda_cube = lambda y: y*y*y

# # # using function defined
# # # using def keyword
# # print ("Using function defined with 'def' keyword,cube:",cube(5))

# # # using the lambda function
# # print("Using lambda function, cube:",lambda_cube(5))

# # def add(y):
# #     return y+y+y

# # lambda_cube = lambda y: y+y+y

# # # using function defined
# # # using def keyword
# # print ("Using function defined with 'def' keyword,cube:",add(5))

# # # using the lambda function
# # print("Using lambda function, cube:",lambda_cube(5))

# # mytuple = ("alpha","beta","gamma")
# # myit = iter(mytuple)

# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))


# import tkinter as tk
# main=tk.Tk(className="student id card")
# main.configure(bg="black")
# main.geometry("1000x1000")

# label1=tk.Label(main,text="CHRISTIANO RONALDO").grid(row=0,column=0)
# txt1=tk.Entry(main).grid(row=0,column=1)  

# label1=tk.Label(main,text="LIONEL MESSI").grid(row=1,column=0)
# txt1=tk.Entry(main).grid(row=1,column=1)  


# label=tk.Label(main,text="NEYMAR JR").grid(row=2,column=0)
# txt1=tk.Entry(main).grid(row=2,column=1)

# label=tk.Label(main,text="IBRAHIMOVIC").grid(row=3,column=0)
# txt1=tk.Entry(main).grid(row=3,column=1)

# label=tk.Label(main,text="PAUL POGBA").grid(row=4,column=0)
# txt1=tk.Entry(main).grid(row=4,column=1)

# label=tk.Label(main,text="PELE").grid(row=5,column=0)
# txt1=tk.Entry(main).grid(row=5,column=1)

# label=tk.Label(main,text="MBAPPE").grid(row=6,column=0)
# txt1=tk.Entry(main).grid(row=6,column=1)

# label=tk.Label(main,text="JOO_7").grid(row=7,column=0)
# txt1=tk.Entry(main).grid(row=6,column=1)




# main.mainloop()

class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawn Successfully!")

    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)


accounts = {}

def create_account():
    name = input("Enter Name: ")
    acc_no = input("Enter Account Number: ")
    
    if acc_no in accounts:
        print("Account already exists!")
    else:
        accounts[acc_no] = BankAccount(name, acc_no)
        print("Account Created Successfully!")

def deposit_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no].deposit(amount)
    else:
        print("Account not found!")

def withdraw_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[acc_no].withdraw(amount)
    else:
        print("Account not found!")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        accounts[acc_no].display()
    else:
        print("Account not found!")

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        withdraw_money()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

