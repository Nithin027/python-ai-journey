class Student:
    def __init__(self,name,subject,marks):
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
        print(f"Yo! my name is {self.name}")
        print(f"My subject is {self.subject}")
        print(f"My marks are {self.marks} and so my grade is {self.get_grade()}")


student1 = Student("Nithin","Math", 93)
student2 = Student("Leo","Python",88)

student1.introduce()
student2.introduce()

