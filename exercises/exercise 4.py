hours= input('Enter hours: ')
rate= input('Enter rate: ')
ihours= float(hours)
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