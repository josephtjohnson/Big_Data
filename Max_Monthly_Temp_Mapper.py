import sys
import csv

reader = csv.reader(syst.stdin)

temp = 0

for line in reader:
    #try to store temp as an integer
    try:
        temp = int(line[1])
    except:
        continue
        
    #store the key as the date and the value as temp
    print line[0], "\t", temp
