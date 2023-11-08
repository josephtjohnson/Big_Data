#import the sys module
import sys

#read each line from the input
for line in sys.stdin:
    kvp = {}
    try:
        #strip white spaces
        val = line.strip()
        
        #split at the comma
        vals = val.split(",")
        kvp[vals[0]] = (vals[1],vals[2])
        print(kvp)        
    except:
        continue

#cat sample.txt | python SMA_Mapper.py | python SMA_Reducer.py
