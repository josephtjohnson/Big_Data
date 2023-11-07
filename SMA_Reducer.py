#import the sys module
import sys

#create three lists to hold the data we receive from the mapper
lstStock = list()
lstDate = list()
lstPrice = list()

#the moving average interval
smaInterval = 3

#read each line from the input
for line in sys.stdin:
    
    #add the values from line to their respective lists
    lstStock.append(line[0])
    lstDate.append(line[1])
    lstPrice.append(float(line[2]))
    
    #if we have accrued three stock prices then proceed
    if len(lstVals) == smaInterval:
    
        #verify the moving average is being calculated based on the same stock, if so proceed
        if lstStock[0] == lstStock[2]:
            sumVal = 0
            
            #add the stock prices together
            for v in lstPrice:
                sumVal += v
                
            #calculate the moving average
            sumVal = sumVal / smaInterval
            
            #print the result
            print '%s\t%s\t%.2f' % (lstStock[2], lstDate[2], sumVal)
            
            #remove the oldest value from each list
            del lstVal[0]
            del lstDate[0]
            del lstPrice[0]
            
        #we have a mixed list for the stock so we need to remove the oldest value from each list and read the next line
        else:
            del lstVal[0]
            del lstDate[0]
            del lstPrice[0]
