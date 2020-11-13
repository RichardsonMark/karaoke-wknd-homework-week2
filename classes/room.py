class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.guests = []
        self.playlist = []


# check in a guest to a room
    def check_in(self, guest):
        self.guests.append(guest)

# check a guest out from a room
    def check_out(self, guest):
        self.guests.remove(guest)

# add a song to a playlist in a room
    def add_song(self, song, artist, genre):
        self.playlist.append([song, artist, genre])