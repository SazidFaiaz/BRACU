from itertools import count


class TaxiLagbe:
    def __init__(self , number , area) :
        self.number = number
        self.area = area

    def addPassenger(self , *name):
        self.count = 0
        self.name_lst = []
        self.fair_lst2 = []
        for i in name:
            self.count += 1
            new_list = i.split('_')
            self.name_lst.append(new_list[0])
            self.fair_lst2.append(new_list[1])
        if self.count < 4:
            for i in self.name_lst:
                print(f'Dear {i}! Welcome to TaxiLagbe.')
        else:
            print('Taxi Full! No more passengers can be added.')

    def printDetails(self):
        fair_tup = tuple(self.fair_lst2)
        print(f'Trip info for Taxi number: {self.number}')
        print(f'This taxi can cover only {self.area}.')
        print(f'Total passengers: {self.count}')
        print(f'Passenger lists: \n{self.name_lst}')
        print(f'Total collected fare: {sum(fair_tup)} Taka')


        

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()