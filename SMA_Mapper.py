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
        
        if not prevDate == vals[1]:
            prevDate == vals[1]
            print(vals[0],"\t",vals[1],"\t",vals[2])           
    except:
        continue

#cat sample.txt | python SMA_Mapper.py | python SMA_Reducer.py
