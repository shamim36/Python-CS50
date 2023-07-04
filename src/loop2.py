def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n


def meow(n):
    for i in range(n):
        print(f"{i+1}.meow")


main()
