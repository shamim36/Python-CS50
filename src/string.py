# name = input("What is your name? ")
# print("Hello, ",end="")
# print(name)
# print("hello \"friend\"")
# print("hello \nfriend")
# print("hello \tfriend")
# print("hello \\friend")
# print("hello\bfriend")
# print("hello friend \rgood")

"""
* Removes whitespace from the beginning of a string
-> name = name.strip()
* Capitalizes the first letter of a string
-> name = name.capitalize()
-> name = name.title() # This is the best way to do it
* Capitalizes first letters of a string and removes whitespace from the beginning of a string
-> name = name.strip().capitalize()
-> name = name.strip().title() # This is the best way to do it
* Slips a string into a template
-> print(f"Hello, {name}")
* Split a string into a list of strings
-> name = name.split()
-> name = name.split(" ")
-> name = name.split(",")
* Assigns the first and last items in a list to variables
->first,last = name.split(" ")

"""
name = input("What is your name? ").strip().title()
# name = name.strip().title()
# name = name.capitalize()
#name = name.title()
first,last = name.split(" ")
print(f"Hello, {first}")

