# Create a budget class that can instantiate an object based on Food, clothing and entertainment
class budget:
    def __init__(self, name, amount):
        self.name=name    
        self.amount=amount

# Withdrawing funds from each category
    def withdrawal(self, amount):
        amount=int(input("Enter the amount you want to Withdraw: "))
        if amount>self.amount:
            return f"Insufficient funds, your balance for {self.name} is {self.amount}"
        else:
            self.amount=self.amount-amount
            return f"you have withdrawn {amount}, you have {self.amount} remaining for {self.name}"

# Depositing funds to each of the categories
    def deposit(self, amount):
        amount=int(input("Enter the amount you want to Deposit: "))
        self.amount=self.amount+amount
        return f"you have deposited {amount}, your current balance for {self.name} is {self.amount}"

# Computing category balance
    def balance (self):
        current_balance= f"Your current balance for {self.name} is {self.amount} "
        return current_balance

    # Transferring Balance amounts between categories
    def balance_transfer(self,amount,recipient):
        amount=int(input("Enter the amount you want to Transfer: "))
        if amount>self.amount:
            return f"Insufficient funds, your balance for {self.name} is {self.amount}"
        else:
            self.amount=self.amount-amount
            recipient.amount=recipient.amount+amount
            transaction= f'You transferred {amount} from {self.name} to {recipient.name}\n'
            transaction+= f'Your current balance for {self.name} is {self.amount}\n'
            transaction+= f'Your current balance for {recipient.name} is {recipient.amount}'

            return transaction


def food():
    food_budget=budget("Food",0)
    available_option=int(input("Select '1' to Deposit\nSelect '2' to Withdraw\nSelect '3' to Transfer\nSelect '4' to Check balance\n"))
    if available_option==1:
        print(food_budget.deposit(0))
        budget_app()
    elif available_option==2:
        print(food_budget.withdrawal(0))
        budget_app()
    elif available_option==3:
        print(food_budget.balance_transfer(0,""))
        budget_app()
    elif available_option==4:
        print(food_budget.balance())
    else:
        print("Invalid option selected")

def clothing():
    clothing_budget=budget("clothings", 0)
    available_option=int(input("Select '1' to Deposit\nSelect '2' to Withdraw\nSelect '3' to Transfer\nSelect '4' to Check balance\n"))
    if available_option==1:
        print(clothing_budget.deposit(0))
        budget_app()
    elif available_option==2:
        print(clothing_budget.withdrawal(0))
        budget_app()
    elif available_option==3:
        print(clothing_budget.balance_transfer(0,""))
        budget_app()
    elif available_option==4:
        print(clothing_budget.balance())
    else:
        print("Invalid option selected")

def entertainment():
    entertainment_budget=budget("entertainment", 0)
    available_option=int(input("Select '1' to Deposit\nSelect '2' to Withdraw\nSelect '3' to Transfer\nSelect '4' to Check balance\n"))
    if available_option==1:
        print(entertainment_budget.deposit(0))
        budget_app()
    elif available_option==2:
        print(entertainment_budget.withdrawal(0))
        budget_app()
    elif available_option==3:
        print(entertainment_budget.balance_transfer(0,""))
        budget_app()
    elif available_option==4:
        print(entertainment_budget.balance())
    else:
        print("Invalid option selected")

def budget_app():
    selected_option=int(input("You can perform the following budget transactions:\nSelect '1' for Food Budget\nSelect '2' for Clothing budget\nSelect '3' for Entertainment Budget\nSelect '4' to exit\n"))
    if selected_option==1:
        food()
    elif selected_option==2:
        clothing()
    elif selected_option==3:
        entertainment()
    elif selected_option==4:
        exit()
    else:
        print('invalid option selected')
        budget_app()




food_budget=budget("Food",10000)
clothing_budget=budget("clothings", 5000)
# entertainment_budget=budget("entertainment", 2000)
# # print(food_budget.balance())
# print(clothing_budget.balance())
# print(entertainment_budget.balance())
# print(food_budget.withdrawal(4000))
# print (food_budget.deposit(0))
print(food_budget.balance_transfer(2000,clothing_budget))