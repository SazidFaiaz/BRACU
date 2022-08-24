
class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self, real, com):
        super().__init__(int(str(real)))
        self.com = com

    def __add__(self, other):
        real = super().__add__(other)
        com = self.com + other.com
        return ComplexNumber(real, com)

    def __sub__(self, other):
        real = super().__sub__(other)
        com = self.com - other.com
        return ComplexNumber(real, com)

    def __str__(self):

        if self.com < 0:
            return str(self.number)+" - "+str(self.com*-1)+"i"
        else:
            return str(self.number)+" + "+ str(self.com)+"i"


r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)