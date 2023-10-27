MAX_LINES = 3

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

def main() :
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main ()    
