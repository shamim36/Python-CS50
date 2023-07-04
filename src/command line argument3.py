import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")  # exit program

# input: abid asif farha -> output: abid asif
for arg in sys.argv[1:-1]:   # -1 means last element deleted
    print("Hello, my name is", arg)  # print name tags


# input: abid asif farha -> output: abid asif farha
for arg in sys.argv[1:len(sys.argv)]:
    print("Hello, my name is", arg)  # print name tags