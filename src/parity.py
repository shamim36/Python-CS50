# num = int(input("Enter a number: "))
#
# if num % 2 == 0:
#     print(f"{num} Number is even")
# else:
#     print(f"{num} Number is odd")

"""
def main():
    num = int(input("Enter a number: "))
    print(is_even(num))


def is_even(num):
    if num % 2 == 0:
        return f"{num} Number is even"
    else:
        return f"{num} Number is odd"

main()
"""


def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} Number is even")
    else:
        print(f"{num} Number is odd")


def is_even(num):
    """
    if num % 2 == 0:
        return True
    else:
        return False
    """
    # return True if num % 2 == 0 else False
    return num % 2 == 0

main()



