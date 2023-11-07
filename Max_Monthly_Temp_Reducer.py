import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

maxTemp_year = list()

for line in reader:
    year = line[0]
    month = line[1][0]
    temp = line[1][1]
    
    if len(maxtemp_year) = 0:
        maxTemp_year.append((year,(month,temp))
    else:
        for value in maxTemp_year:
            if value[0] == year:
                if value[1][1] < temp:
                    value[1][0] = month
                    value[1][1] = temp
                    
    
        
#print the maxPower and the date
for value in maxTemp_year:
    print str(value[0] + value[1][0]), "\t" value[1][1]
