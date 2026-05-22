for i in range(5):
  print(i)

for i in range(1, 6):
  print(i)

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
   print(fruit)

for letter in "Nithin":
   print(letter)
for i in range(0, 20, 2):
   print(i)


count = 0
while count < 5:
   print(count)
   count += 1

count = 1
while count <= 10:
   print(count)
   count += 1

for i in range(1, 21):
   if i % 2 == 1:
      print(i) 

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
       print("Fizz")
    elif i % 5 == 0:
       print("buzz")
    else:
       print(i)

fruit = ["apple", "banana", "mango", "grapes"]
for fruit in fruits:
   if fruit == "mango":
      print("found mango!")
      break
   print(f"not mago:{fruit}")



      
