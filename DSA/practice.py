class Teacher:
    def __init__(self, name, dept) -> None:
        self.name = name
        self.dept = dept
        self._course = []

    def addCourse(self, other):
        self._course.append(other.course)

    def printDetail(self):
        print("=============")
        print(f"Name:{self.name} \nDep: {self.dept}\nList")
        print("========")
        for i in self.course:
            print(i)
        print("======")

class Course:
    def __init__(self, title) -> None:
        self.title = title

t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")                          
c1 = Course("CSE 110 Programming Language I")                           
c2 = Course("CSE 111 Programming Language-II")                           
c3 = Course("CSE 220 Data Structures")                           
c4 = Course("CSE 221 Algorithms")                           
c5 = Course("CCSE 230 Discrete Mathematics")                           
c6 = Course("CSE 310 Object Oriented Programming")                           
c7 = Course("CSE 320 Data Communications")                          
c8 = Course("CSE 340 Computer Architecture") 
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

