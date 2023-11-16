from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        yield line.rstrip().split(' ,')


values = read_mapper_output(sys.stdin)
for currentSet, friendsList in groupby(values, itemgetter(0)):
     for currentSet, friends in friendsList:
          print(currentSet,friends)
