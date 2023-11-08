import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

prevDate=None
maxDate = ''
maxTemp = 0

for line in reader:
    date = line[0]
    #are we in the same year
    if date[0:5] == prevDate[0:5]:
        #if we are in the same year is the current line's temp greater than the current maxTemp
        if maxTemp < line[1]:
            maxDate = line[0]
            maxTemp = line[1]
    else:
        if not prevDate == None:
            print prevDate, "\t", str(maxTemp)
        maxDate = line[0]
        maxTemp = line[1]
    prevDate = date
