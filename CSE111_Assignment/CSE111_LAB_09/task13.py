class msgClass:
    def __init__(self):
        self.content = 0
class Q5:
    def __init__(self):
        self.sum = 3
        self.y = 6
        self.x = 1
    def methodA(self):
        x = 1
        y = 1
        msg = [msgClass()]
        myMsg = msgClass()
        myMsg.content = self.x
        msg[0] = myMsg
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0].content
        print(f"{x} {y} {self.sum}")
    def methodB(self, *args):
        if len(args) == 1:
            x = 1
            y = 1
            y = self.sum + args[0].content
            self.y = y + args[0].content
            x = self.x + 3 + args[0].content
            self.sum = self.sum + x + y
            Q5.x = args[0].content + x + 2
            print(f"{x} {y} {self.sum}")
            return y
        else:
            x = 1
            self.y = self.y + args[0][0].content
            args[0][0].content = self.y + args[1].content
            x = x + 3 + args[1].content
            self.sum = self.sum + x + self.y
            args[1].content = self.sum - args[0][0].content
            print(f"{Q5.x} {self.y} {self.sum}")
            return self.sum


q =  Q5()
q.methodA()

