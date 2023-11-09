
hours= input('Enter hours: ')
rate= input('Enter rate: ')
def computepay (hours, rate):
    if hours > 40 :
        
        pay=(hours-40) * (rate*1.5) + (40*rate)

    else :
        pay= hours * rate

    return pay   

try :
    hours= float(hours)
    try :
        rate= float(rate)
        x= computepay (hours, rate)
        print ('Your pay is: ', x)
    except :
        hours==-1    
        print ('Error, please enter numeric input') 
except :
    rate==-1
    print ('Error, please enter numeric input')   
    



    
    