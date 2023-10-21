
hours= input('Enter hours: ')
rate= input('Enter rate: ')
hours= float(hours)
rate= float(rate)

def computepay (hours, rate):
    if hours > 40 :
        
        pay=(hours-40) * (rate*1.5) + (40*rate)

    else :
        pay= hours * rate

    return pay   

x= computepay (hours, rate)
print ('Your pay is: ', x)
    



# hours= input('Enter hours: ')
# rate= input('Enter rate: ')
# try :
#     ihours= float(hours)
#     try :
#         irate= float(rate)
#         if ihours > 40 :
    
#             extrahours= ihours-40
#             extrarate= irate * 1.5

#             regular= 40 * irate
#             overtime= extrahours * extrarate
#             print ('your regular pay is: ', regular, 'your overtime pay is: ', overtime)
#             total= regular + overtime
#             print ('Your total pay is: ', total)
#         else :
#             pay= ihours * irate
#             print ('your pay is: ', pay)
#     except : 
#         irate==-1    
#         print ('Error, please enter numeric input')          
# except :
#     ihours= -1
#     print ('Error, please enter numeric input')


    
    