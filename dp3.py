import sys
import tsdl

def smallest_value(r):
    '''read and process reader r to find the smallest value after the TSDL header.'''

    line = tsdl.skip_header(r).strip()
    smallest = int(line)

    for line in r:
        line = line.strip()
        value = int(line)
        if value < smallest:
            smallest = value
    return smallest

if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    print smallest_value(input_file)
    input_file.close()