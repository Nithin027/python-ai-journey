class Student:
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "F"
        
    def introduce(self):
        print(f"Hi I am {self.name}")
        print(f"My subject is {self.subject}")
        print(f"My marks are {self.marks} and my grade is {self.get_grade()}")


student1 = Student("Nithin", "Python", 95)
student2 = Student("Leo", "AI", 83)
student3 = Student("Das", "Math", 65)

student1.introduce()
student2.introduce()
student3.introduce()        