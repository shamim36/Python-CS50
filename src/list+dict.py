students = [
    {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']},
    {'name': 'Jane', 'age': 22, 'courses': ['CompSci', 'Physics']},
    {'name': 'Dave', 'age': 21, 'courses': ['Math', 'CompSci']},
    {'name': 'Dave', 'age': 21, 'courses': None}
]

# print(students[0])

for student in students:
    print(student["name"], student["age"], student["courses"], sep=" , ")
