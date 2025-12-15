import random

MAX_LINES = 3 # This global constant will set the max number of lines constant.
MAX_BET = 500
MIN_BET = 10

ROWS = 3
COlS = 3

symbol_count = {
    "A" = 2,
    "B" = 5,
    "C" = 5,
    "D" = 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for col in range(cols):
        column = []
        for row in range(rows):
            value = random.choice(all_symbols)

def deposit(): # We use this function for collection of user input
    while True: #This while loop will ask the user to enter a valid amount
        amount = input("What would you like the stating deposit amount to be? ") # inside input we will put a prompt
        if amount.isdigit(): # isdigit will tell us if the number is a whole number, i.e won't take negative numbers or fractions.
            amount = int(amount) # this function will convert the number the user eneterd above into an int, i.e if a user inputs a string i.e Hey then it won't work as this is not a whole number.
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.") # This shows us that if amount is greater than 0 the for loop will break, for which we used break after if statement. Otherwise it will return the 
        else:    # This else is here because we are defining the first if statement that talks about the amount being a digit, if the number entered is not a whole number then this else statemnet will be triggered and the user will be told to enter a number again. 
            print("Please enter a number") 
    return amount # if all the conditions are met this function will return the amount.   

def get_number_of_lines(): # This function will help us define the users choice of number of lines.
    while True: #This while loop will ask the user to enter a valid number of lines
        lines = input("Enter the number of lines you want to bet on (1- "+ str(MAX_LINES) + ")? ") # we have added max lines in a string
        if lines.isdigit(): # isdigit will tell us if the number is a whole number, i.e won't take negative numbers or fractions.
            lines = int(lines) # this function will convert the number the user eneterd above into an int, i.e if a user inputs a string i.e Hey then it won't work as this is not a whole number.
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines") # This shows us that if amount is greater than equal to 1 and less than eqaul to MAX LINES the for loop will break, for which we used break after if statement. 
        else:    # This else is here because we are defining the first if statement that talks about the number of lines being a digit, if the number entered is not a whole number then this else statement will be triggered and the user will be told to enter a number again. 
            print("Please enter a number. ") 
    return lines # if all the conditions are met this function will return the lines. 

def get_bet():
    while True: #This while loop will ask the user to enter a valid number of lines
        amount = input("How much would you like to bet? $") # we have added max lines in a string
        if amount.isdigit(): 
            amount = int(amount) # this function will convert the number the user eneterd above into an int, i.e if a user inputs a string i.e Hey then it won't work as this is not a whole number.
            if 10<= amount <= 500:
                break
            else:
                print(f"Enter the valid amount between ${MIN_BET} - ${MAX_BET}") # The f at the start would help us in writing variables in a string, write the variable function in ${}
        else:    # This else is here because we are defining the first if statement that talks about the number of lines being a digit, if the number entered is not a whole number then this else statement will be triggered and the user will be told to enter a number again. 
            print("Please enter a number. ") 
    return amount # if all the conditions are met this function will return the lines. 

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True: # to make sure that the bet amount is less than or equal to the total balance in the account
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print (f"Not enough money in the account, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    #print(balance, lines)
main()
# we equalled deposit to balance because this would be our intital starting balance. 
# To make things easier we will put it under a new function main so that we just have to run it and the whole process above will be triggered.
