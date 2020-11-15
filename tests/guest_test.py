import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Eddie Vedder", "The Wrong Car", 500)         
        self.guest_2 = Guest("Kurt Cobain", "Teen Spirit", 300)
        self.guest_3 = Guest("Billy Corgan", "1979", 500)         
        self.guest_4 = Guest("Chris Cornell", "The Day I Tried To Live", 385)
        self.guest_5 = Guest("Zack De la Rocha", "Testify", 500)         
        self.guest_6 = Guest("Chino Moreno", "Change In the House of Flies", 350)

        self.room_1 =  Room("Yellow Submarine", 8, 50)
        self.room_2 =  Room("Purple Rain", 10, 60)
        self.room_3 =  Room("Blue Monday", 12, 70)

        self.song_1 = Song("Tether", "Chvrches", "Synth Pop")
        self.song_2 = Song("Questions and Answers", "Biffy Clyro", "Alt Rock")
        self.song_3 = Song("The Wrong Car", "The Twilight Sad", "Post Punk")
        self.song_4 = Song("Fast Blood", "Frightened Rabbit", "Indie Folk")
        self.song_5 = Song("Scottish Fiction", "Idlewild", "Indie")

#    @unittest.skip("Delete this line to run the test")
    def test_guest_name(self):
        self.assertEqual("Eddie Vedder", self.guest_1.name)

#    @unittest.skip("Delete this line to run the test")
    def test_playlist_has_fav_song(self):
        self.room_1.playlist = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5]
        donkey_kong = self.guest_1.playlist_has_fav_song(self.room_1)
        no_donkey_kong = self.guest_2.playlist_has_fav_song(self.room_1)
        self.assertEqual("WooHoo, it's on!!", donkey_kong)
        self.assertEqual("D'oh! " + self.guest_2.fav_song + " isn't on the playlist, boo!!", no_donkey_kong)


