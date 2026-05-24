fruits = ["apple", "banana", "mango", "grapes"]
print(fruits[0])
print(fruits[-1])

print(len(fruits))

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

print(fruits[1:3])


numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

fruits = ["apple", "banana", "apple", "mango"]
print(fruits.count("apple"))

print(fruits.index("banana"))

fruits.insert(1, "grapes")
print(fruits)

fruits.pop()
print(fruits)

coordinates = (10, 20,30)

print(coordinates[0])
print(coordinates[-1])

print(len(coordinates))

for item in coordinates:
    print(item)

# creating dictionary
person = {
    "name": "Nithin",
    "age": 25,
    "city": "USA",
    "goal": "AI Engnieer"
}

# Accessing values
print(person["name"])
print(person["goal"])

# Adding new key
person["course"] = "MSITM"
print(person)

# Updating a value
person["age"] = 26
print(person["age"])

# Removing a key
del person ["city"]
print(person)

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

 # Check if key exists
print("name" in person)
print("salary" in person)

number = {1, 2, 3, 4, 5}

fruits = {"apple", "banana", "apple", "mango", "banana" }
print(fruits)

fruits.add("sugars")
print(fruits)

fruits.remove("banana")
print(fruits)

print("apple" in fruits)

movies = ["Avengers", "Peaky Blinders", "Dark", "Black Panther", "Sherlock Homes"]
print(movies[0])
print(movies[-1])

movies.append("Naruto")
print(movies)

movies.pop(1)
print(movies)

print(movies)


person =  {

    "name": "Leo",
    "age": 25,
    "degree": "MSITM",
    "goal": "AI Engineer",
    "city": "USA"
}

person["hobby"] = "Valorant"
print(person)

for key, value in person.items():
    print(f"{key} : {value}")

numbers = {1,2,2,3,3,4, 5,5}
print(numbers)

numbers.add(6)
print(numbers)

print(3 in numbers)

Students = {
    "student1": {
    "name": "Nithin",
    "marks": 95,
    "grade": "A"   

    },
    "student2": {
        "name": "Leo",
        "marks":92,
        "grade": "A"
    },
    "student3": {
        "name": "Das",
        "marks": 85,
        "grade": "B"
    }
   
}

for student, details in Students.items():
     print(f"\n{student}")
     for key, value in details.items():
         print(f"  {key}: {value}")