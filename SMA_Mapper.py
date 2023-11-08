#import the sys module
import sys

prevDate = None

#read each line from the input
for line in sys.stdin:
    try:
        #strip white spaces
        val = line.strip()
        
        #split at the comma
        vals = val.split(",")

        #exclude duplicate data by checking the date
        if not prevDate == vals[1]:
            prevDate = vals[1]

            #emit the processed line
            print(vals[0],"\t",vals[1],"\t",vals[2])           
    except:
        continue
