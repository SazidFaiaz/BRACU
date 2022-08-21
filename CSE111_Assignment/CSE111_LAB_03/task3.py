# Task 3

class Patient:
    def __init__(self , name , age , weight , height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def printDetails(self):
        print('name:', self.name )
        print('age' , self.age)
        print('weight' , self.weight)
        print('Height' , self.height)
        print('bmi' , self.weight/(self.height/100)**2)
p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()