class Student:
    id = 0
    def __init__(self , name , dep , age , cgpa):
        self.name = name
        self.dep = dep
        self.age = age
        self.cgpa = cgpa
        Student.id += 1

    def get_details(self):
        print(f'ID: {Student.id} Name: {self.name} \nDepartment: {self.dep} \nAge: {self.age} \nCGPA: {self.cgpa}')

    @classmethod
    def from_String(cls , detail):
        detail = detail.split('-')
        return cls(detail[0], detail[1], detail[2], detail[3])




s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()