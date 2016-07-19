import sys
from tsdl import skip_header

def find_largest(line):
    '''Return the largest value in line, which is a whitespace-delimited string of integers.'''
    #the largest value seen so far.
    largest = -1

    for value in line.split():
        # Remove the trailing period (去除结尾句点)
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v
    return largest

