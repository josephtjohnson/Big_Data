#import the sys module
import sys

#create a list to hold the data we receive from the mapper
lstStockRecords = list()

#create variable to hold current stock
currentStock=None

#the moving average interval
smaInterval = 3

#read each line from the input
for line in sys.stdin:
    vals = line.split('\t')
    
    #parse the values and add them to the list
    lstStockRecords.append([vals[0],[vals[1],vals[2]]])
    currentStock = vals[0]
    currentDate = vals[1]
    
    #if we have accrued three stock prices then proceed
    if len(lstStockRecords) == smaInterval:           
    
        #verify the moving average is being calculated based on the same stock, if so proceed
        continue = true
        for record in lstStockRecords:
            if record[0] != currentStock:
                continue = false
                break
                
        #we have verified we are calculating the moving average based on the same stock
        if(continue):
            sumVal = 0
            
            #add the stock prices together
            for record in lstStockRecords:
                sumVal += float(record[1][1])
                
            #calculate the moving average
            sumVal = round((sumVal / smaInterval),2)
            
            #print the result
            print (currentStock,"\t",sumVal,"\t",currentDate)

            del lstStockRecords[0]
            
        #remove the oldest value from each list and move on to the next line
        else:
            del lstStockRecords[0]
