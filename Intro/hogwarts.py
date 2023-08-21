#loops on lists
students = ["Hermione", "Harry", "Ron"]
"""
for student in students:
    print(student)
"""

for i in range(len(students)):
    print(i + 1, students[i]) #1 Hermione 2 Harry 3 Ron


# loops on dictionaries
students = {
            "Hermione":"Gryffindor",
            "Harry":"Gryffindor", 
            "Ron":"Gryffindor", 
            "Draco":"Slytherin"
            }

for student in students:
    print(students, students[student], sep=",")

# having more data
students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus": None}
]

for student in students:
    print(student["name"],student["house"], student["patronus"], sep=",")
