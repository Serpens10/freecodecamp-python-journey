# try and except 

rawstr=input('enter a number different than -1: ')
try :
    ival = int(rawstr)
except :
    ival = -1
if ival !=-1 :    
    print ('nice work')    
else :
    print ('not a number')
