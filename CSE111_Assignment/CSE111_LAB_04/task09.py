class CricketTeam:
    def __init__(self , name = None , coach = None , captain = None , players = [] ):
        self.name = name
        self.coach = coach
        self.captain = captain
        self.players = players

        if captain not in players:
            self.players.insert(0,captain)
        elif captain in players:
            self.players.remove(captain)
            self.players.insert(0,captain)
        self.scorecard = []
    
    def add_player(self, new_player):
        for i in new_player:
            if i not in self.players:
                self.players.append(i)

    def add_score(self , *score):
        for i in score :
            self.scorecard.append(i)

    def show_total_run(self):
        sum = 0
        for i in self.scorecard:
            sum += i
        return sum

ct0 = CricketTeam() 
print(ct0.name)
print(ct0.coach)
print(ct0.captain)   
ct1 = CricketTeam("Bangladesh")
ct2 = CricketTeam("Bangladesh", "Domingo")
ct3 = CricketTeam("Bangladesh", "Domingo", "Shakib")
ct4 = CricketTeam("Bangladesh", "Domingo", "Shakib", ["Tamim", "Liton", "Sohan"])
ct1.add_player(("Shakib", "Tamim"))
print(ct1.players)
ct2.add_player(["Shakib", "Tamim", "Sohan"])
print(ct2.players)
ct3.add_player(["Shakib", "Mushfiq", "Liton"])
print(ct3.players)
ct4.add_player(("Shakib", "Mustafiz"))
print(ct4.players)
ct1.add_scores(50)
print(ct1.show_total_run())
ct2.add_scores(70, 5)
print(ct2.show_total_run())
ct3.add_scores(70, 5, 85)
print(ct3.show_total_run())
ct4.add_scores(70, 5, 85, 78)
print(ct4.show_total_run())

