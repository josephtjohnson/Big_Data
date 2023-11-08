import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

#create variables for storing the values
prevDate=None
maxDate = ''
maxTemp = 0

#read in lines
for line in reader:
    date = line[0]
    #are we in the same year
    if not prevDate == None:
        if date[0:5] == prevDate[0:5]:
            #if we are in the same year is the current line's temp greater than the current maxTemp
            if maxTemp < line[1]:
                maxDate = line[0]
                maxTemp = line[1]
    else:
        #if the previous date is not empty
        if not prevDate == None:
            #we are looking at a new year so print the previous year's max values
            print(maxDate, "\t", str(maxTemp))
        #store the current years values as the new maxDate and maxTemp
        maxDate = line[0]
        maxTemp = line[1]
    prevDate = date
#prints the results of the final iteration
print(maxDate, "\t", str(maxTemp))
