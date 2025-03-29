import sys, re

# sys.argv -> list of command-line arguments
# sys.argv[0] -> name of the program itself
# sys.argv[1] -> regex specified at the command line

regex = sys.argv[1]

# for every line passed into the script

for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
        