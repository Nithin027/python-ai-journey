def greet():
    print("hello! welcome to AI Journey")

greet()
greet()
greet()


def greet_person(name):
    print(f"Hello {name}! Welcome to AI Journey!")

greet_person("Nithin")
greet_person("Leo")
greet_person("Das")

def add_numbers(a, b):
    result = a+b
    return result
    
answer = add_numbers(10,5)
print(answer)

print(add_numbers(20, 30))


def greet_user(name, message="Welcome to AI Journey"):
    print(f"Hello {name}! {message}")

greet_user("Nithin")

greet_user("Leo", "You are going to be an AI engineer")


def get_student_info(name, marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    else:
        grade = "C"
    return name, grade

student_name, student_grade = get_student_info("Nithin", 95)
print(f"{student_name} got grade {student_grade}")


def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(5))

add = lambda a, b: a + b
print(add(10 , 20))

def biggest_number(a,b):
    if a > b:
        return a
    else:
        return b
result = biggest_number(5, 9)
print(result)


def greet_user(name, age=25):
    print(f"Hello {name} you are {age} years old")

greet_user("leo")
greet_user("Nithin",27)

multiply = lambda a, b: a * b
print(multiply(10,4))


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number 
    return total
my_numbers = [1,2,3,4,5]
result = calculate_sum(my_numbers)
print(result)

def greet_person(name, message="is going to be AI engineer"):
    print(f"{name}, {message}")

greet_person("leo") 

def square(x):
    return  x * x
square_lambda = lambda x: x * x

print(square(6))
print(square_lambda(6))