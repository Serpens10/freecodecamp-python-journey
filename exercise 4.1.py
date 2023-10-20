# try and except example 

rawstr=input('enter a number different than -1: ')
try :
    ival = int(rawstr)
except :
    ival = -1
if ival !=-1 :    
    print ('nice work')    
else :
    print ('not a number')

# implementing it in exercise 4

hours= input('Enter hours: ')
rate= input('Enter rate: ')
try :
    ihours= float(hours)
    try :
        irate= float(rate)
        if ihours > 40 :
    
            extrahours= ihours-40
            extrarate= irate * 1.5

            regular= 40 * irate
            overtime= extrahours * extrarate
            print ('your regular pay is: ', regular, 'your overtime pay is: ', overtime)
            total= regular + overtime
            print ('Your total pay is: ', total)
        else :
            pay= ihours * irate
            print ('your pay is: ', pay)
    except : 
        irate==-1    
        print ('Error, please enter numeric input')          
except :
    ihours= -1
    print ('Error, please enter numeric input')   

