def main():
    x = float(input("Enter a number: "))
    print("The square of", x, "is", square(x))


def square(x):
    return x * x


# def square(x):
#     return x ** x
#
#
# def square(x):
#     return pow(x,2)

main()