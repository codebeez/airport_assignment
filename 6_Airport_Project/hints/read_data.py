"""
Here we are reading one line from a file: f.
We can repeatitly call `.readline()` to get the next line.
Or we can us for loop in combination with `readlines()`, see:
https://tutorial.eyehunts.com/python/python-read-file-line-by-line-readlines/
"""

with open("../data/routes.dat") as f_readline:
    print(f_readline.readline())

# or using the readlines for-loop iterator

with open("../data/routes.dat") as f_readlines:
    for index, line in enumerate(f_readlines.readlines()):
        print(line)
        if index > 5:
            break
