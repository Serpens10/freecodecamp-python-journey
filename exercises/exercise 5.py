# loop counter

count = 0
for item in [6,234,567,9,563,67,80,0,98,65,34,2]:
    count = count + 1
    print(count, item)

# total count

total = 0
for item in [6,234,567,9,563,67,80,0,98,65,34,2]:
    total= total + item
    print(total, item)
print("the total is: ", total)   

count = 0
sum = 0
howmany = 0
for number in [6,234,567,9,463,67,80,0,98,65,134,2]:
    count = count + 1
    if number < 100 :
        howmany = howmany + 1
        sum = sum + number
        print("position:", count, "value:", number, "totaling to:", sum)
print(f"we have {howmany} small numbers. they add up to {sum}")        
        