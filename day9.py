file = open("Students.txt", "w")
file.write("Nithin\n")
file.write("Leo\n")
file.write("Das\n")
file.close()

print("File created!")

file = open("students.txt", "r")
content = file.read()
file.close()

print(content)


with open("students.txt", "w") as file:
    file.write("Nithin\n")
    file.write("Leo\n")
    file.write("Das\n")
with open("students.txt", "r") as file:
    content = file.read()
    print(content)
    

students = [
    {"name": "Nithin", "marks": 95},
    {"name": "Leo","marks": 83},
    {"name": "Das","marks": 65}
]

with open("grades.txt", "w") as file:
    for student in students:
        file.write(f"{student['name']},{student['marks']}\n")

print("Grades file")

with open("grades.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        print(f"students: {name}, Marks: {marks}")