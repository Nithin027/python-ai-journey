class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
            print(f"Hi! My name is {self.name} and I am {self.age} years old!")

person1 = Person("Nithin", 25)
person2 = Person("Leo", 22)

person1.introduce()
person2.introduce()

print(person1.name)
print(person2.age)


class Student:
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks

     def get_grade(self):
          if self.marks >= 90:
               return "A"
          elif self.marks >= 80:
               return "B"
          elif self.marks >=70:
               return "C"
          else:
               return "F"
    
     def introduce(self):
          print(f"I am {self.name}, I scored {self.marks} and got grade {self.get_grade()}")

student1 = Student("Nithin", 95)
student2 = Student("Leo", 83)
student3 = Student("Das", 65)

student1.introduce()
student2.introduce()
student3.introduce()



class BankAccount:
     def __init__(self,owner,balance):
         self.owner = owner
         self.balance = balance

     def deposit(self, amount):
          self.balance += amount
          print(f"Deposited {amount}, New balance: {self.balance}")

     def withdraw(self, amount):
          if amount > self.balance:
               print("insuficient funds!")
          else:
               self.balance -= amount
               print(f"Withdrawn {amount}, New balance: {self.balance}")

     def check_balance(self):
          print(f"{self.owner}'s balance: {self.balance}")


account = BankAccount("Nithin", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)


class Car:
     def __init__(self,brand,color,speed):
          self.brand = brand
          self.color = color
          self.speed = speed
     
     def accelerate(self):
          self.speed += 10
          print(f"Car speed is Increased! Now: {self.speed}")
               
     def brake(self):
          self.speed -= 10
          print(f"Car speed is Decreased! Now: {self.speed}")

     def show_info(self):
          print(f"Brand: {self.brand}, Color: {self.color}, Speed: {self.speed}")


car1 = Car("Toyota", "Blue", 60)
car1.show_info()
car1.accelerate()
car1.brake()
          
     

          
     
           