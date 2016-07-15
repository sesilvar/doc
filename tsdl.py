def skip_header(r):
    '''Skip the header in reader r,and return the first real piece of data.'''
    # Read the description line and then the comment lines.
    line = r.readline()
    while line.startswith("#"):
        line = r.readline()
    return line