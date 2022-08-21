#from turtle import color


class Color:
    def __init__(self , color):
        self.color = color

    def __add__(self, other):
        if (self.color == 'red' and other.color == 'yellow') or (self.color == 'yellow' and other.color == 'red'):
            return Color("Orange")

        elif (self.color == 'red' and other.color == 'blue') or (self.color == 'blue' and other.color == 'red'):
            return Color('Violet')

        elif (self.color == 'yellow' and other.color == 'blue') or (self.color == 'blue' and other.color == 'yellow'):
            return Color('Green')

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.color)