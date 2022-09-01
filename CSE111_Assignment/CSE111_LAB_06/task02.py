class Assassin:
    num = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        Assassin.num += 1

    def printDetails(self):
        print(f'Name: {self.name} \nSuccess rate: {self.rate}% \nTotal number of Assassin: {Assassin.num}')

    @classmethod
    def failureRate(cls , name , frate):
        cls.name = name
        cls.frate = 100-frate
        # cls.rate = 100-cls.frate
        return Assassin(cls.name , cls.frate)

    @classmethod
    def failurePercentage(cls , name , fpercent):
        cls.name = name
        cls.rate = str(fpercent)
        return Assassin(cls.name , cls.rate)




john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()