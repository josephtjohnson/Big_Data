import sys

for line in sys.stdin:
    try:
        input = line.split(',')
        key = input[0] 
        values = input[1].split() 
        for f in values:
            if int(key) > int(f):
                fset = (f,key)
            else :
                fset = (key,f) 
            print('{}\t{}'.format(fset,values))
    except:
        continue
