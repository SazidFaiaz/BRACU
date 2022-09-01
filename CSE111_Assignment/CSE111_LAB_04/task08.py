class ParcelKoro:
    def __init__(self , name='No name set' , weight= 0):
        self.name = name
        # self.weight = weight
        self.product_weight = weight

    # def product_weight(self , new_weight):
    #     self.weight = new_weight
    
    def calculateFee(self , location = None):
        self.location = location
        if self.product_weight != 0:
            if self.location != None:
                self.total_fee = (self.product_weight*20)+100
            else:
                self.total_fee = (self.product_weight*20)+50
        else:
            self.total_fee = 0

    def printDetails(self):
        print(f'Customer Name: {self.name} \nProduct Weight: {self.product_weight} \nTotal fee: {self.total_fee}')


print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()