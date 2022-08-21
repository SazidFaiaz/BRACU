class StudentDatabase:
    def __init__( self , name , id ):
        self.name = name
        self.id = id

    def calculateGPA(self, lst = [] , sem = None):
        self.lst = lst
        self.sem = sem
        point = 0
        count = 0
        for i in lst:
            new_lst = i.split(': ')
            point += new_lst[1]
            count += 1
        gpa = (point*3)/(count*3)

    def printDetails(self):
        # dict_of = {{self.sem}}
        print(f'Grades for {self.name} \n"{"{self.sem}"}"')





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