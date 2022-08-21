class Data:
	def __init__(self, x):
		self.x = x
		
	def __add__(self, other):
		return self.x + other.x
	
num1 = Data(10)
num2 = Data(20)
str1 = Data("CSE")
str2 = Data("111")	

print(num1 + num2)
print(str1 + str2)
         
        
        