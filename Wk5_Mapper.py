import sys
import csv

reader = csv.reader(syst.stdin, delimiter=';')

power = 0.0

for line in reader:
    #try to store power as a float
    try:
        power = float(line[2])
    except:
        continue
        
    #store the key as the date and the value as power
    print line[0], "\t", power
