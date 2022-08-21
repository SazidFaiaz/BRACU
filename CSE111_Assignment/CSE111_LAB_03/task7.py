# Task 7
class Student:
    def __init__(self , name , id, dep, gpa ):
        self.name = name
        self.id = id
        self.dep = dep
        self.gpa = gpa
    
    def calculate_CGPA(self):
        sum = 0
        for i in self.gpa:
            sum+=i*3
        self.cgpa = sum/(len(self.gpa)*3)
#         print(self.cgpa)
    
    def print_details(self):
        if self.cgpa > 3.80:
            print(f'Name: {self.name},  ID; {self.id} \nDepartment: {self.dep}\nCGPA: {self.cgpa}\nYour academic standing is "Highest Distinction"')
        elif self.cgpa >3.65:
            print(f'Name: {self.name}, ID; {self.id} Department: {self.dep} CGPA: {self.cgpa} Your academic standing is "High Distinction"')
        elif self.cgpa > 3.50:
            print(f'Name: {self.name}, ID; {self.id} Department: {self.dep} CGPA: {self.cgpa} Your academic standing is "Distinction"')
        elif self.cgpa > 2.00 :
            print(f'Name: {self.name}, ID; {self.id} Department: {self.dep} CGPA: {self.cgpa} Your academic standing is "Satisfactory,"')
        elif self.cgpa < 2.00:
            print(f'Name: {self.name}, ID; {self.id} Department: {self.dep} CGPA: {self.cgpa} Sorry, you cannot graduate')
            
        

s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()