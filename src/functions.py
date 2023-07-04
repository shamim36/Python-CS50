def main():
    hello()
    name = input("What is your name? ")
    hello(name)



def hello(name="World"):
    print("Hello,", name)


main()