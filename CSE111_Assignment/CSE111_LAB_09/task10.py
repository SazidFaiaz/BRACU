class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"

class CSEStudent(Student):
    def __init__(self, name, id, sem):
        super().__init__(name, id)
        self.sem = sem
    def Details(self):
        return "Name: " + self.name + "\n" + "ID: " + self.ID + "\nCurrent semester:"+self.sem

    def addCourseWithMarks(self, *courses):
        mainlist = list(courses)
        num_course = (len(mainlist)/2)
        self.courselist = []
        self.numlist = []
        print(f'{self.name} has taken {int(num_course)} courses.')
        for i in range(0,len(mainlist),1):
            self.courselist.append(mainlist[i])
        # for i in range(2,len(mainlist),1):
        #     self.numlist.append(mainlist[i])
        for i, j in zip(self.courselist, self.numlist):
            print(i, j)
        print(self.courselist)
        print(self.numlist)
    def showGPA(self):
        cgpa = sum(self.numlist)/len(self.numlist)
        print(f'GPA of {self.name} is: {cgpa}')

Bob = CSEStudent("Bob","20301018",'Fall 2020')
Carol = CSEStudent("Carol","16301814",'Fall 2020')
Anny = CSEStudent("Anny","18201234",'Fall 2020')
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()
