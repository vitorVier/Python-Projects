students = [
    {"name": "Vítor", "School": "University","grade": "2º Semester"},
    {"name": "Diego", "School": "University","grade": "4º Semester"},
    {"name": "Darles", "School": "University","grade": "2º Semester"},
    {"name": "Débora", "School": "School","grade": "8º grade"},
    {"name": "Merice", "School": "Teacher","grade": "no grade"}
]

for student in students:
    print(  student["name"], student["School"], student["grade"], sep=", ")