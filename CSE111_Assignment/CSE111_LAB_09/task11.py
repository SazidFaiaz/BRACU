class Transport:
    total_traveller = 0

    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare

    def __str__(self):
        s = 'Name: ' + self.name + ", Base fare: " + str(self.baseFare)
        return s

class Bus(Transport):
    passenger = 0

    def __init__(self, name, fair):
        super().__init__(name, fair)
        self.totalfair = 0
        Transport.total_traveller += 1
        Bus.passenger += 1
        print(f'Base-fare of {self.name} is {self.baseFare} Taka ')

    def addPassengerWithBags(self, *info):

        bagfair = 0
        for i in range(0, len(info), 2):
            bag = info[i + 1]
            if bag <= 2:
                bagfair = 0
            elif 3 <= bag <= 5:
                bagfair = 60
            elif bag > 5:
                bagfair = 150

            self.totalfair = self.baseFare + bagfair

    def __str__(self):
        s = super().__str__() + '\nTotal Passenger(s):' + str(Bus.passenger) + '\nPassenger details:'+'name:'+str(self.name)+'Fair:'+str(self.totalfair)
        return s

class Train(Transport):
    passenger = 0

    def __init__(self, name, fair):
        super().__init__(name, fair)
        self.totalfair = 0
        Transport.total_traveller += 1
        Bus.passenger += 1
        print(f'Base-fare of {self.name} is {self.baseFare} Taka ')

    def addPassengerWithBags(self, *info):

        bagfair = 0
        for i in range(0, len(info), 2):
            bag = info[i + 1]
            if bag <= 2:
                bagfair = 0
            elif 3 <= bag <= 5:
                bagfair = 60
            elif bag > 5:
                bagfair = 150

            self.totalfair = self.baseFare + bagfair

    def __str__(self):
        s = super().__str__() + '\nTotal Passenger(s):' + str(Bus.passenger) + '\nPassenger details:'+'name:'+str(self.name)+'Fair:'+str(self.totalfair)
        return s

t1 = Bus('Volvo', 950)
print("=================================")
t1.addPassengerWithBags('David', 6, 'Mike', 1, 'Carol', 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train('SilkCity', 850)
print("=================================")
t2.addPassengerWithBags('Bob', 2, 'Simon', 4)
print("=================================")
print(t2)
print("=================================")
print('Total Passengers in Transport:', Transport.total_traveller)
