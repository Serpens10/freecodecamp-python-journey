def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $ ")
        if amount.isdigit():
            amount = float(amount)
            if amount > 0 :
                break
            else :
                print("Amount must be greater than 0.")