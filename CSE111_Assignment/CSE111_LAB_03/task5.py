# Task 5
class Shape:
    def __init__(self , name , height , length ):
        self.name = name
        self.height = height
        self.length = length
    def area(self):
        if  self.name == 'Triangle' :
            print('Area:' , (self.height*self.length)/2)
        elif self.name == 'Square' :
            print('Area:' , self.length*self.height)
        elif self.name == 'Rhombus' :
            print('Area:' , (self.height*self.length)/2)
        elif self.name == 'Rectangle' :
            print('Area:' , self.length*self.height)
        else :
            print('Area: Shape unknown')
            

triangle = Shape("Triangle", 10, 25)
triangle.area()
print("==========================")
square = Shape("Square", 10, 10)
square.area()
print("==========================")
rhombus = Shape("Rhombus", 18, 25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle", 15, 30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium", 15, 30)
trapezium.area()