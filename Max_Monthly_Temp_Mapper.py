import sys
import csv

reader = csv.reader(syst.stdin, delimiter=':')

year = list()
month_temp = list()

for line in reader:
    #try to store power as a float
    try:
        values = line.split(',')
        year = values[0][0:4]
        month_temp = (values[0][4:6],values[1])
    except:
        continue
        
    #store the key as the date and the value as power
    print year, "\t", month_temp
