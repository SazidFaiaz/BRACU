class Smartphone:
    def __init__(self, string=''):
        self.name = string
        self.display = ''
        self.dis_size = ''
        self.ram = ''
        self.ram_size = ''
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def addFeature(self, dis, size):
        if self.name == '':
            print('Feature can not be added without phone name')
        if dis == 'Display':
            self.display = dis
            self.dis_size = self.dis_size+','+size
        elif dis == 'Ram':
            self.ram = dis
            self.ram_size = self.ram_size+','+size
    def printDetail(self):
        print(f'Phone Name: {self.name}\n{self.display}: {self.dis_size}\n{self.ram}: {self.ram_size}')


s1 = Smartphone()
print("=================================")
s1.addFeature('Display', '6.1 inch')
print("=================================")
s1.setName('Samsung Note 20')
s1.addFeature('Display', '6.1 inch')
s1.printDetail()
print("=================================")
s2 = Smartphone('Iphone 12 Pro')
s2.addFeature('Display', '6.2 inch')
s2.addFeature('Ram', '6 GB')
print('=================================')
s2.printDetail()
s2.addFeature('Display', 'Amoled panel')
s2.addFeature('Ram', 'DDR5')
print("=================================")
s2.printDetail()
print("=================================")