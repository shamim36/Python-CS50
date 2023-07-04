# while True:
#     try:
#         x = int(input("Enter a number: "))
#     except ValueError:
#         print("You did not enter a number")
#     else:
#         break
#
# print(f"Your number is {x}")

"""
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("You did not enter a number")

print(f"Your number is {x}")

# if we input 'cat' output will be:
Name Error: name 'x' is not defined
"""

"""
def main():
    x = get_int()
    print(f"Your number is {x}")
"""

# def get_int():
#     while True:
#         try:
#             return int(input("Enter a number: "))
#         except ValueError:
#             print("You did not enter a number")


"""
def get_int():
    while True:
        try:
            return int(input("Enter a number: ")) #if return value is not integer we get ValueError
        except ValueError:
            pass
"""


def main():
    x = get_int("Enter a number: ")
    print(f"Your number is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
