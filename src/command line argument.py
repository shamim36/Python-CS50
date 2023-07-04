#sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# With the len(sys.argv) function you can count the number of arguments.
# If you are gonna work with command line arguments, you probably want to use sys.argv.
# To use sys.argv, you will first have to import the sys module.

import sys

# print("Hello, my name is", sys.argv[0])

"""
code must be run inside the terminal without the exeption in line 8
# python 'command line argument.py' Shamim #
->sys.argv[0] is the name of the interpreter. which is the location file of python
->interprete. which is 'command line argument.py'
->sys.argv[1] is the first argument. which is Shamim
"""

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")