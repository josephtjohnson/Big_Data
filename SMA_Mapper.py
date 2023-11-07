#import the sys module
import sys

#read each line from the input
for line in sys.stdin:

    #strip white spaces
    val = line.strip()
    
    #split at the comma
    vals = val.split(",")
    
    #return the individual values from the split - stock code, date, and price
    yield (vals[0], vals[1], vals[2])

#cat sample.txt | python SMA_Mapper.py | python SMA_Reducer.py
