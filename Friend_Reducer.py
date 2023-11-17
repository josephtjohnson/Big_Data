from itertools import groupby
from operator import itemgetter
import re
import sys

def read_mapper_output(file):
    """Return the line from the mapper."""
    for line in file:
        yield line.rstrip().split('\t')

#store the sorted result from the read_mapper_output function
#if the script doesn't include sort, this will guarantee we sort input before processing
values = sorted(read_mapper_output(sys.stdin))

for currentSet, friendsList in groupby(values,key=itemgetter(0)):
    #used for storing the individual friends lists
    friends = []
    #used for storing the individual friendIDs
    friendIDs = []
    
    #add each list in friendsList to a new list
    for f in friendsList:
        friends.append(f[1])   
    
    #string regression for slicing out the friendIDs
    r = '012'
    #add each individual friendID from the individual lists to a new list
    for x in friends:
        friendIDs.append(re.findall(r'\d+',x)) 
        
    #find the intersection between the two friend lists    
    list3 = [value for value in friendIDs[0] if value in friendIDs[1]]
    
    #strip off all unneeded characters from the userID,friendID pair
    currentSet = currentSet.replace('(','').replace('\'','').replace(')','')
   
    #print the userID,friendID pair and their mutual friends
    print('{} {}'.format(currentSet,list3))

    
