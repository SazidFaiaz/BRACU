# Task 10
class UberEats:
    def __init__(self , name , number , location):
        self.name = name 
        self.number = number
        self.location = location
        print(f'{self.name}, welcome to UberEats!')
    def add_items(self, food1 , food2, price1 , price2 ):
        self.food1 = food1
        self.food2 = food2
        self.price1 = price1
        self.price2 = price2
        self.total = self.price1 + self.price2
    
    def print_order_detail(self):
        dict = {self.food1:self.price1 , self.food2:self.price2}
        return (f'User details: Name: {self.name}, Phone:{self.number},Address: {self.location} Orders: {dict} Total Paid Amount: {self.total}')

        

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
# order1.print_order_detail()
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())