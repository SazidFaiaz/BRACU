# Task05

class Student:
    def __init__(self , name , id , dep = 'CSE'):
        self.dep = dep
        self.name = name
        self.id = id

    def dailyEffort(self , hour):
        self.hour = hour

    def printDetails(self):
        if self.hour <= 2 :
            print(f'Name:{self.name} \nID: {self.id} \nDepartment: {self.dep} \nDaily Effort: {self.hour} hours(s) \nSuggestion: Should give more effort!')
        elif self.hour <= 4 :
            print(f'Name:{self.name} \nID: {self.id} \nDepartment: {self.dep} \nDaily Effort: {self.hour} hours(s) \nSuggestion: Keep up the good work!')
        else:
            print(f'Name:{self.name} \nID: {self.id} \nDepartment: {self.dep} \nDaily Effort: {self.hour} hours(s) \nSuggestion: Excellent! Now motivate others.')



harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()