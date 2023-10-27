def deposit():
    while True :
        amount = input("Enter the amount you want to deposit $ ")
        try :
            amount = float(amount)
            if amount > 0 :
                break
            else :
                print("Amount must be greater than 0.")
        except ValueError :
            print("Please enter amount in numerical form.")
        
    return amount      

deposit() 
