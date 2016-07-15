import sys
def skip_header(r):
    '''Skip the header in reader r,and return the first real piece of data.'''
    # Read the description line and then the comment lines.
    line = r.readline()
    while line.startswith("#"):
        line = r.readline()
    return line

def process_file(r):
    '''Read and print open reader r.'''
    # Find the rest of the data.
    line = skip_header(r).strip()
    print line

    for line in r.readlines():
        line = line.strip()
        print line
if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    process_file(input_file)
    input_file.close()
