# task07
class Match:
    def __init__(self, name):
        self.match_run = 0
        self.match_over = 0
        self.wick = 0
        self.name = name
        self.new = self.name.split('-')
        print('5..4..3..2..1.. Play !!!')

    def add_run(self , run):
        self.match_run += run
        self.sum_run = self.match_run

    def add_over(self , over):
        self.over = over
        if self.over < 5:
            self.match_over += over
            self.sum_over = self.match_over
        else:
            print("Warning! Cannot add 5 over/s (5 over match)")

    def add_wicket(self, wick):
        self.wick = wick


    def print_scoreboard(self):
        print(f'Batting Team:{self.new[0]}')
        print(f'Bowling Team:{self.new[1]}')
        return(f'Total Runs:{self.sum_run} Wickets:{self.wick}  Over: {self.sum_over} ')


match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())