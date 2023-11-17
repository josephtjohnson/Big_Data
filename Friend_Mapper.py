import sys

#read in line for sample_friends.txt
for line in sys.stdin:
    try:
        #split the line to get the userID and the list of friendIDs
        line = line.split(',')
        #userId
        key = line[0] 
        #list of friendIDs
        values = line[1].split() 
        #ensure the set that will be used as a key always has the smaller id in the 0 position
        #this guarantess we won't have situations like (101,102) and (102,101)
        for f in values:
            if int(key) > int(f):
                fset = (f,key)
            else :
                fset = (key,f) 
            #print the set and the associated friends list
            print('{}\t{}'.format(fset,values))
    except:
        continue
