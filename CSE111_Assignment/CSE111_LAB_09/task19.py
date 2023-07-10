class A:
    temp = -5

    def __init__(self):
        self.sum = 0
        self.y = 0
        self.y = self.temp - 3
        self.sum = A.temp + 2
        A.temp -= 2

    def methodA(self, m, n):
        x = 1
        A.temp += 1
        self.y = self.y + m + self.temp
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(f"{x} {self.y} {self.sum}")


class B(A):
    x = -10

    def __init__(self, b=None):
        super().__init__()
        self.y = 4
        self.temp = -5
        self.sum = 2
        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 3
            self.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(1, 3)

    def methodA(self, m, n):
        x = 1
        self.temp += 1
        self.y = self.y + m + self.temp
        x = x + 7 + n
        super().methodA(x, m)
        self.sum = self.sum + x + self.y
        print(f"{x} {self.y} {self.sum}")

    def methodB(self, m, n):
        y = 3
        y = y + self.y
        B.x = self.y + 3 + self.temp
        self.methodA(B.x, y)
        self.sum = self.x + y + self.sum
        print(f"{B.x} {y} {self.sum}")

a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(3,2)
b2.methodB(1,2)