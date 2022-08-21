class Calculator:
    def __init__(self ):

     def calculate(self , num1 , num2 , met): 
        if self.met == '+':
            return (self.num1 + self.num2)
        elif self.met == '-':
            return(self.num1 - self.num2)
        elif self.met == '*':
            return(self.num1 * self.num2)
        elif self.met == '/':
            return (self.num1 / self.num2)
    

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()