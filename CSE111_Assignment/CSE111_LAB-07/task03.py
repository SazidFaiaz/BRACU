# task03

class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
    def __init__(self , name = 'Default' , num = 0 , type='NO type'):
        super().set_name(name)
        self.num = num
        self.type = type
    def detail(self):
        return f'Cricket Tournament Name: {super().get_name()} \nNumber of Teams:{self.num}\nType:{self.type}'

class Tennis_Tournament(Tournament):
    def __init__(self , name , nump):
        super().set_name(name)
        self.nump = nump
    def detail(self):
        return f"Cricket Tournament Name: {super().get_name()} \nNumber of Players:{self.nump}"

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt =Tennis_Tournament("Roland Garros",128)
print(tt.detail())
