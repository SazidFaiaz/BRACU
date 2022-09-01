class Transport:
    total_traveller = 0

    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare

    def __str__(self):
        s =  “Name: ”+self.name + ", Base fare: " + str(self.baseFare)
        return s


# Write your codes here.
# Do not change the following lines of code.
t1 = Bus(“Volvo”, 950)
print("=================================")
t1.addPassengerWithBags(“David”, 6,  “Mike”, 1, “Carol”, 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train(“SilkCity”, 850)
print("=================================")
t2.addPassengerWithBags(“Bob”, 2, “Simon”, 4)
print("=================================")
print(t2)
print("=================================")
print(“Total
Passengers in Transport: ”, Transport.total_traveller )
