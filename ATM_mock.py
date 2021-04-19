import random
import datetime

"""
This program is an update on the aATM mock project

1. Use functions

2. Include register, and login

3. Generate Account Number

4. Any other improvement you can think of (extra point)
"""

now = datetime.datetime.now()
current = now.strftime("%Y-%m-%d, %H:%M:%S")

database = dict()


def init():
    print("***WELCOME TO BANK RUBY***")
    print("The current date and time is: ", current)

    have_account = int(input(
        "Do you have an account with us? \nPress '1' for Yes\nPress '2' for No\nPress '3' to exit\nEnter your answer: "))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    elif have_account == 3:
        exit()
    else:
        print("Invalid Option Selected")
        init()


def login():
    print("***LOGIN to your account***")

    user_account = int(input('Enter your account number: '))

    if user_account in database.keys():
        print('Account number recognized')
        user_password = input('Enter your secret password: ')
        for details in database.values():
            pass
        if user_password == database[user_account][3]:
            print("Login successful")
            banking_operations(details)
        else:
            print("Invalid password")
            login()
    else:
        print("Invalid Account Number")
        login()


def register():
    print("***** Registration Portal*****")

    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    e_mail = input("Enter your Email address:")
    password = input("Create your password: ")

    account_number = (generate_account_number())
    card_number = cards()
    database[account_number] = [first_name, last_name, e_mail, password, card_number]
    print(account_number)
    print("Your account has been successfully created")

    login()


def banking_operations(user):
    print(f'Welcome {user[0]} {user[1]}')

    print('What would you like to do?')
    options = int(input(
        "Press '1' for deposit\nPress '2' for withdrawal\nPress '3' for Customer care \nPress '4' to logout\nPress "
        "'5' to exit\nEnter your answer: "))
    if options == 1:
        deposit()
    elif options == 2:
        withdrawal()
    elif options == 3:
        customer_care()
    elif options == 4:
        logout()
    elif options == 5:
        exit()
    else:
        print("Invalid option selected")
        banking_operations(user)


def withdrawal():
    print("***Withdrawal***")
    amount = int(input("How much would you like to withdraw?\n"))
    print(f"Take your cash {amount}")
    for details in database.values():
        banking_operations(details)


def deposit():
    print("***Deposit***")
    amount = int(input("How much would you like to deposit?\n"))
    print(f"Your deposit of {amount} has been confirmed.")
    for details in database.values():
        banking_operations(details)


def customer_care():
    print('This is the Customer Care Unit')
    complaint = input("What issue would you like to report?\n")
    print("Thank you for contacting us")
    for details in database.values():
        banking_operations(details)


def logout():
    virtual_card()


def generate_account_number():
    print("This is your account number")
    return random.randrange(0000000000, 9999999999)


def virtual_card():
    card = int(
        input('Do you want a virtual ATM card number?\nPress (1) for Yes\nPress (2) for No\nEnter your answer: '))
    if card == 1:
        user_account = int(input('Enter your account number: '))
        if user_account in database.keys():
            print('Account number recognized')
            print('This is your virtual ATM card number')
            print("It can be used to perform online transactions")
            print(database[user_account][4])
        init()
    elif card == 2:
        init()
    else:
        print("Invalid Option selected")
        virtual_card()


def cards():
    card_no = random.randrange(0000000000000000, 9999999999999999)
    return card_no


"""
THis is the actual banking operation
"""
init()

