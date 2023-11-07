#import the sys module
import sys

#create three lists to hold the data we receive from the mapper
lstStock = list()
lstInfo = list()

#the moving average interval
smaInterval = 3

#read each line from the input
for k, v in sys.stdin.items():
    
    #add the values from line to their respective lists
    lstStock.append(k)
    lstInfo.append(v)
    
    #if we have accrued three stock prices then proceed
    if len(lstStock) == smaInterval:
    
        #verify the moving average is being calculated based on the same stock, if so proceed
        if lstStock[0] == lstStock[2]:
            sumVal = 0
            
            #add the stock prices together
            for v in lstInfo:
                sumVal += v[1]
                
            #calculate the moving average
            sumVal = sumVal / smaInterval
            
            #print the result
            print '%s\t%s\t%.2f' % (lstStock[2], lstInfo[2][0], sumVal)
            
            #remove the oldest value from each list
            del lstStock[0]
            del lstInfo[0]
            
        #we have a mixed list for the stock so we need to remove the oldest value from each list and read the next line
        else:
            del lstStock[0]
            del lstInfo[0]
