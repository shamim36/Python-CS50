name = input("What is your name? ")

match name:
    case "Guido" | "Shamim" | "Stark":
        print("You are the creator of Python!")
    case "Raymond":
        print("You are the main developer of CPython!")
    case "Jake":
        print("You are a teacher of Python!")
    case _:
        print("I don't know you!")