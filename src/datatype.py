# x = int(input("x?: "))
# y = float(input("y?: "))
#
# z = x + y
#
# print(z)

"""
* go to nearest integer
-> print(round(z))
round(2.5) -> 2
round(2.6) -> 3
* go to nearest integer and number of decimal places
-> print(round(z,2))


"""
# x = float(input("x?: "))
# y = float(input("y?: "))
#
# z = round(x + y)
#
# print(f"{z:,}") # use comma as thousands separator
# print(f"{z:,}".replace(",",".") + "€")

x = float(input("x?: "))
y = float(input("y?: "))

# z = round(x + y,2)
z = x + y
print(z)
print(f"{z:.2f}")