"""
* while loop
->  i=0
    while i<3:
        print("Hello")
        i=i+1
* for loop
->  for i in range(3):
        print("Hello")
* for loop with list
->  for i in [0,1,2]:
        print("Hello")
* for loop with string
->  for i in "Hello":
        print("Hello")
* for loop with tuple
->  for i in (0,1,2):
        print("Hello")
* for loop with set
->  for i in {0,1,2}:
        print("Hello")
* for loop with dictionary
->  for i in {0:"Hello",1:"World",2:"Python"}:
        print("Hello")
* for loop with dictionary keys 
->  for i in {0:"Hello",1:"World",2:"Python"}.keys():
        print("Hello")
* for loop with dictionary values
->  for i in {0:"Hello",1:"World",2:"Python"}.values():
        print("Hello")
* for loop with dictionary items
->  for i in {0:"Hello",1:"World",2:"Python"}.items():
        print("Hello")
"""

'''
i = 0
while i < 3:
    print("Hello")
    i += 1
'''
'''
# for loop with list
for i in [0,0,2]:
    print(i) #print 0 0 2
    
list1 = [0,'Sja',2]
for i in list1:
    print(i) #print 0 1 2
'''
# for _ in range(3):
#     print(_) #print 0 1 2

# print("meow\n" * 3, end="")  # print meow 3 times

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         print("n is positive.")
#         continue
#     else:
#         break

