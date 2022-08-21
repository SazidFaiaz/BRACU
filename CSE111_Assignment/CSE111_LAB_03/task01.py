
class Calculator:
    def __init__(self , first_value , operator , second_value):
        self.first_value = first_value
        self.operator = operator
        self.second_value = second_value
        
        print('Lets calculate')
        print('value 1:' , self.first_value)
        print('OPERATOR:' , self.operator )
        print('Value 2:' , self.second_value)
        
        
    def add( self):
            return( self.first_value + self.second_value)
    def subtract(self):
            return(self.first_value - self.second_value)
    def multiply (self):
            return( self.first_value * self.second_value)
    def divide (self):
            return( self.first_value/self.second_value)

first_value = int(input())
operator = input()
second_value = int(input())
        
c = Calculator(first_value , operator , second_value) 


if operator == '+' :
    print('Result:' , c.add())   
elif operator == '-':
    print('Result:' , c.subtract())
elif operator == '*':
    print('Result:' , c.multiply())
elif operator == '/':
    print('Result:' , c.divide()) 