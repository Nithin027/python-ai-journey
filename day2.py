age = 20

if  age >= 18:
    print("you are an adult")
else:
    print("you ar a minor")

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

x = 10
y = 20

print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= 10:", x >= 10)
print("x <= 10:", x <= 10)

age = 25
gpa = 4.5

if age > 18 and gpa > 4.0:
    print("Eligible for schlorship")

if age < 18 and gpa > 4.8:
    print("special case")

if not age > 30:
    print("you are young!")

marks = 60
attendence = 75

if marks >= 80:
    if attendence >= 75:
        print("pass with distinction")
    else:
        print("good marks but low attendence")
else:
    print("need to improve marks")

# ========== Part 3 - Exercises ==========

number = 27
if number > 0: 
  print("positive number")
elif number  < 0:
  print("negetive number")
else:
    print("it is zero")


age = 27
if age <= 18:
   print("Minor")
elif age <= 60:
    print("Adult")
else:
    print("Senior")

username = "admin"
password = "1234"

if username == "admin" and  password == "1234":
    print("Login successful")
else:
    print("Invalid Credentials")

name = input("Enter your name:")
age = int(input("Enter your age:"))

if age >= 18:
    print(f"welcome {name} you are an adult")
else:
    print(f"sorry {name} you are too young")


