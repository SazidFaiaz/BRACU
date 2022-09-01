class Student:
    count = 0
    csecount = 0
    bba = 0

    def __init__(self, name, dep):
        self.name = name
        self.dep = dep
        Student.count += 1
        if dep == 'CSE':
            Student.csecount += 1
        elif dep == 'BBA':
            Student.bba += 1
        print(f'Creating Student Number: {Student.count}')

    def individualInfo(self):
        if self.dep == "CSE":
            print(f'{self.name} is from {self.dep} department')
            print(f'serial of {self.name} among all students is: {Student.count}')
            print(f'serial of {self.name} among all students is: {Student.csecount}')
        elif self.dep == "BBA":
            print(f'{self.name} is from {self.dep} department')
            print(f'serial of {self.name} among all students is: {Student.count}')
            print(f'serial of {self.name} among all students is: {Student.bba}')

    def totalInfo(self):
        print(f'Total Number of Student:{Student.count}')
        print(f'Total Number of CSE Student: {Student.csecount}')
        print(f'Total Number of BBA Student: {Student.bba}')


s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')

s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')

s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')

s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()
