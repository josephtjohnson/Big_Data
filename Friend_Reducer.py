from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator):
    for line in file:
    yield line.rstrip().split(separator, 1)
    
def main(separator=','):
    data = read_mapper_output(sys.stdin, separator)
    for line in data:
        outputKey = data[0]
        lstFriends = data[1]
        common = set.intersection(*map(set,lstFriends))
        yield outputKey, common