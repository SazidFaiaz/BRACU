class Team:
    def __init__(self , name=""):
        self.__name = name
        self.__pname = []

    def setName(self, newname):
        self.__name = newname

    def addPlayer(self , other):
        self.__pname.append(other.player)

    def printDetail(self):
        print('=====================')
        print(f'Team: {self.__name} \nList of Players: \n{self.__pname}')
        print('=====================')

class Player:
    def __init__(self , player):
        self.player = player

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()