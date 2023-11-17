from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        yield line.rstrip().split('\t')


values = sorted(read_mapper_output(sys.stdin))
for currentSet, friendsList in groupby(values,key=itemgetter(0)):
     print(currentSet, friendsList)
