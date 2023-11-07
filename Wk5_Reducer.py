import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

#create our max power variable 
maxPower = 0.0
maxDate = ''

for line in reader:
    power = float(line[1])
    
    #if the current power value is greater than maxPower, set maxPower equal to current power value
    if power > maxPower:
        maxPower = power
        maxDate = line[0]
        
#print the maxPower and the date
print maxDate, '\t', maxPower
