import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Tether", "Chvrches", "Synth Pop")
        self.song_2 = Song("Questions and Answers", "Biffy Clyro", "Alt Rock")
        self.song_3 = Song("The Wrong Car", "The Twilight Sad", "Post Punk")
        self.song_4 = Song("Fast Blood", "Frightened Rabbit", "Indie Folk")
        self.song_5 = Song("Scottish Fiction", "Idlewild", "Indie")
        self.song_6 = Song("Lightspeed", "Twin Atlantic", "Indie")
        self.song_7 = Song("Midfield Maestro Fiction", "There Will be Fireworks", "Indie")
        self.song_8 = Song("Quiet Little Voices", "We Were Promised Jetpcks", "Indie")
        self.song_9 = Song("Stop Coming to my House", "Mogwai", "Post Rock")

        
        
#    @unittest.skip("Delete this line to run the test")
    def test_song_title(self):
        self.assertEqual("Questions and Answers", self.song_2.title)