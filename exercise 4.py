hours= input('Enter hours: ')
rate= input('Enter rate: ')
ihours= int(hours)
irate= int(rate)
if ihours > 40 :
    extrahours= ihours-40
    extrarate= irate * 1.5
    pay= (40 * irate) + (extrahours * extrarate)
    print ('your pay is: ', pay)
else :
    pay= ihours * irate
    print ('your pay is: ', pay)    