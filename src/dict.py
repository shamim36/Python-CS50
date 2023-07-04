students = {
    "Alice": {"id": 1, "age": 20, "grade": 90},
    "Bob": {"id": 2, "age": 21, "grade": 80},
    "Charlie": {"id": 3, "age": 22, "grade": 70},
    "David": {"id": 4, "age": 23, "grade": 60},
    "Eve": {"id": 5, "age": 24, "grade": 50},
}

print(students["Alice"]["age"])  # 20   # Alice's age
print(students["Bob"]) # {'id': 2, 'age': 21, 'grade': 80}   # Bob's info

for student in students:
    print(student)  # Alice, Bob, Charlie, David, Eve  # print keys

for student in students:
    print(student, students[student] , sep=" --> ")  # print nam & values