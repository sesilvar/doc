import sys

# Count all the birds.
count = {}
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    for line in infile:
        name = line.strip()
        if name in count:
            count[name] = count[name] + 1
        else:
            count[name] = 1
    infile.close()

# Print.
for b in count:
    print b, count[b]


##  下面通过使用 dic.get 方法使代码更简洁

import sys

# Count all the birds.
count = {}
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    for line in infile:
        name = line.strip()
        count[name] = count.get(name, 0) + 1
    infile.close()

# Print.
keys = count.keys()
keys.sort()
for b in keys:
    print b, count[b]