
class PokemonBasic:
    def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type
    def get_type(self):
        return 'Main type: ' + self.type
    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'
    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness

class PokemonExtra(PokemonBasic):
    def __init__(self, name ='Default', hp=0, weekness=None, type=None, type2=None, *extra):
        super(name, hp, weekness, type)
        self.extra = extra
        self.type2 = type2

    def get_type(self):
        if self.type2 == None:
            return 'Main type: ' + self.type
        else:
            return f'Main type: {self.type}, Secondary type: {self.type2}'

    def get_move(self):
        

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water','Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water','Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())