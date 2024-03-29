import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values) :
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else : 
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings, winning_lines        

def get_spin(rows, cols, symbols) :
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)   
            current_symbols.remove(value) 
            column.append(value)   

        columns.append(column) 

    return columns     

def print_slot_machine(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end= "")    
        print()        

    

def deposit():
    while True :
        amount = input("Enter the amount you want to deposit: $")
        try :
            amount = float(amount)
            if amount > 0 :
                break
            else :
                print("Amount must be greater than 0.")
        except ValueError :
            print("Please enter amount in numerical form.")
        
    return amount   

def get_number_of_lines() :
       
    while True :
        lines = input("What is he number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        try :
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print("Enter a valid number of lines.")
        except ValueError :
            print("Please enter number of lines in numerical form.")
        
    return lines 

def get_bet() :
    while True :
        bet_amount = input("Enter the amount you want to bet on each line: $")
        try :
            bet_amount = float(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET :
                break
            else :
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        except ValueError :
            print("Please enter amount in numerical form.")
        
    return bet_amount  

balance = 0 

def the_game() :
    lines = get_number_of_lines()
    while True :
        bet_amount = get_bet() 
        total_bet = bet_amount * lines 
        rem_balance = balance - total_bet
        if total_bet > balance :
            print(f"You have insufficient money for this operation. Your current balance is ${balance} ")
        else :
            break    
    print(f"You are betting ${bet_amount} on {lines} lines. Total bet is equal to ${total_bet} and your remaining money is ${rem_balance}")   
    
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet_amount, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main() :
    balance = deposit()
    while True :
        print(f"Your current balance is ${balance}")
        spin = input("Press enter to spin (q to quit).")
        if spin == "q" :
            break
   

main ()    

