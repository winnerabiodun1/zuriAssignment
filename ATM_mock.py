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

    try:
        have_account = int(input(
            "Do you have an account with us? \nPress '1' for Yes\n"
            "Press '2' for No\nPress '3' to exit\nEnter your answer: "))
    except ValueError:
        print("Invalid option selected")
        init()

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

    a_valid_account_number = account_number_validation(user_account)

    if a_valid_account_number:
        print('Account number recognized as valid')
        user_password = input('Enter your secret password: ')

        for details in database.values():

            if user_password == database[user_account][3]:
                print("Login successful")
                banking_operations(details)
            else:
                print("Invalid password")
                login()
    else:
        print("Invalid Account Number")
        login()


def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Account number must be integers")
                return False


        else:
            print("Account number must be 10 digits not more or less")
            return False
    else:
        print("THe account number field cannot be empty")
        return False


def register():
    print("***** Registration Portal*****")

    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    e_mail = input("Enter your Email address:")
    password = input("Create your password: ")

    try:
        account_number = (generate_account_number())
        card_number = cards()
    except EnvironmentError:
        print("Account number generation Failed")
        register()

    database[account_number] = [first_name, last_name, e_mail, password, card_number, 0]
    print(account_number)
    print("Your account has been successfully created")

    login()


def banking_operations(user):
    print(f'Welcome {user[0]} {user[1]}')

    print('What would you like to do?')
    try:
        options = int(input(
            "Press '1' for deposit\nPress '2' for withdrawal\nPress '3' for Customer care \nPress '4' to logout\nPress "
            "'5' to exit\nEnter your answer: "))
    except ValueError:
        print("Selected Option must an integer")
        banking_operations(user)
        
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
    try:
        amount = int(input("How much would you like to withdraw?\n"))
        print(f"Take your cash {amount}")
    except ValueError:
        print("invalid amount")
        withdrawal()

    for details in database.values():
        current_balance=details[5]
        if current_balance < amount:
            current_balance=amount-current_balance
            print(f"insufficient balance, deposit{current_balance} to withdraw{amount}")
            deposit()
        elif current_balance>amount:
            current_balance=current_balance-amount
            print(f"You have withdrawn {amount},\nYour current balance is{current_balance}")

        banking_operations(details)


def deposit():
    print("***Deposit***")
    try:
        amount = int(input("How much would you like to deposit?\n"))
        print(f"Your deposit of {amount} has been confirmed.")
    except ValueError:
        print("Invalid Amount inputed")
        deposit()

    for details in database.values():
        current_balance= get_balance(details)+amount
        print(f"Your current balance is{current_balance}")

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

def get_balance(user_details):
    return user_details[5]

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

