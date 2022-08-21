# task10
class EPL_Team:
    def __init__(self , name , song = 'NO slogan'):
        self.name = name
        self.song = song
        self.total = 0

    def showClubInfo(self):
        return(f'Name: {self.name} \nSong: {self.song}\nTotal No of title: {self.total}')
    
    def increaseTitle(self):
        self.total += 1

    def changeSong(self , new):
        self.new = new
        self.song = self.new


manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())