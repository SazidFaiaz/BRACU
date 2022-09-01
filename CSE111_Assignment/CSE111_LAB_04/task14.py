from multiprocessing.sharedctypes import Value
from pyparsing import dict_of
class StudentDatabase:
    def __init__( self , name , id):
        self.name = name
        self.id = id
        self.gpa=0
        self.dict2 = {}
        self.grades = self.dict2

    def calculateGPA(self, lst = [] , sem = None):
        self.lst = lst
        self.sem = sem
        point = 0
        count = 0
        self.lst2 = []
        for i in lst:
            new_lst = i.split(': ')
            x=float(new_lst[1])
            (self.lst2.append(new_lst[0]))
            self.new_tuple = tuple(self.lst2)
            point += x
            count += 1
        self.gpa = round((point*3)/(count*3),2)
        
        self.dict1 = {}
        key_dict1  = self.new_tuple
        dict1_Value = self.gpa
        self.dict1[key_dict1] = dict1_Value

        key_dict2 = self.sem
        dict2_value = self.dict1
        self.dict2[key_dict2] = dict2_value

    def printDetails(self):
        print(f'Name: {self.name} \nID: {self.id}')
        for key , value in self.grades.items():
           print(f'Courses taken in {key}')
           for a , b in value.items():
                for i in a:
                   print(i)
                print(b)


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()