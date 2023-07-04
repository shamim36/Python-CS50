import sys

# check errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")  # exit program
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")  # exit program

# print name tags
print("Hello, my name is", sys.argv[1])