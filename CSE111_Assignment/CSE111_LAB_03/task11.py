# Task 11
class Spotify:
    def __init__(self , lst):
        
        self.lst = lst
        print('Welcome to Spotify!')
        
    def playing_number(self , num):
        self.num = num
        if self.num <= len(self.lst) :
            print(f'Playing {self.num} number song for you Song name: {self.lst[(self.num-1)]}')
        else:
            print(f'{self.num} number song not found. Your playlist has {len(self.lst)+1} songs only.')
        return('##########################')
            
    def add_to_playlist(self , song):
        self.song = song
        self.lst.append(self.song)
        

user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))