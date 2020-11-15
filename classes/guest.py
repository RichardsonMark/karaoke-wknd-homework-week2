class Guest:
    def __init__(self, name, fav_song, wallet):
        self.name = name
        self.fav_song = fav_song
        self.wallet = wallet

    def playlist_has_fav_song(self, room):
        if room.search_for_song(self.fav_song) != None:
            return "WooHoo, it's on!!"
        else:
            return "D'oh! " + self.fav_song + " isn't on the playlist, boo!!"
