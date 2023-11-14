import sys

def read_mapper_input(stdin):
"""
Generator to limit memory usage while reading input.
"""
for line in stdin:
    yield line
    
def main():
    for line in read_mapper_input(sys.stdin):
    userID = line.split(",")[0]
    friendIDs = list(line.split(",")[1])
    friendIDs.sort()
    for f in friendIDs:
    
        if userId > f:
            key = (f,userID)
        else :
            key = (userID,f) 
            
        value = friendIDs
        
        yield key,value