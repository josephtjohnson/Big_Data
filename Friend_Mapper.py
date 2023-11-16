import sys

for line in sys.stdin:
    try:
        values = line.split(',')
        userID = values[0]
        friendIDs = list(values[1].split()) 
        valueList = []
        for f in friendIDs:
            if int(userID) > int(f):
                key = (f,userID)
            else :
                key = (userID,f) 
            value = friendIDs
            print('{0} ,{1}'.format(key,value))
    except:
        continue
