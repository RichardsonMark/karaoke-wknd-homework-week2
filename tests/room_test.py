import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 =  Room("Yellow Submarine", 8, 50)
        self.room_2 =  Room("Purple Rain", 10, 60)
        self.room_3 =  Room("Blue Monday", 12, 70)
        self.room_4 =  Room("Black and White Town", 15, 80)
        self.room_5 =  Room("Pink Cadillac", 20, 90)
        self.room_6 =  Room("99 Red Baloons", 22, 100)
        
        self.guest_1 = Guest("Eddie Vedder", "Black", 500)         
        self.guest_2 = Guest("Kurt Cobain", "Teen Spirit", 300)
        self.guest_3 = Guest("Billy Corgan", "1979", 500)         
        self.guest_4 = Guest("Chris Cornell", "The Day I Tried To Live", 385)
        self.guest_5 = Guest("Zack De la Rocha", "Testify", 500)         
        self.guest_6 = Guest("Chino Moreno", "Change In the House of Flies", 350)
        self.guest_7 = Guest("Shirley Manson", "Only Happy When it Rains", 500)         
        self.guest_8 = Guest("PJ Harvey", "This is Love", 300)
        self.guest_9 = Guest("Kim Deal", "Cannonball", 500)         
        self.guest_10 = Guest("Courtney Love", "Malibu", 385)

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
    def test_room_name(self):
        self.assertEqual("Yellow Submarine", self.room_1.name)

#    @unittest.skip("Delete this line to run the test")
    def test_check_in(self):
        self.room_1.check_in(self.guest_1.name)
        self.assertEqual(1, len(self.room_1.guests))

#    @unittest.skip("Delete this line to run the test")
    def test_check_out(self):
        self.room_1.check_in(self.guest_1.name)
        self.room_1.check_in(self.guest_2.name)
        self.room_1.check_out(self.guest_1.name)
        self.assertEqual(1, len(self.room_1.guests))

#    @unittest.skip("Delete this line to run the test")
    def test_add_song(self):
        self.room_1.add_song(self.song_1.title, self.song_1.artist, self.song_1.genre)
        self.room_1.add_song(self.song_2.title, self.song_2.artist, self.song_2.genre)
        self.assertEqual(2, len(self.room_1.playlist))

#    @unittest.skip("Delete this line to run the test")
    def test_room_at_capacity(self):
        self.room_1.check_in(self.guest_1.name)
        self.room_1.check_in(self.guest_2.name)
        self.room_1.check_in(self.guest_3.name)
        self.room_1.check_in(self.guest_4.name)
        self.room_1.check_in(self.guest_5.name)
        self.room_1.check_in(self.guest_6.name)
        self.room_1.check_in(self.guest_7.name)
        self.room_1.check_in(self.guest_8.name)
        self.assertEqual("Sorry, you can't go in to that room, it's full.", self.room_1.room_at_capacity())

#     @unittest.skip("Delete this line to run the test")
    def test_charge_for_share_of_room(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.room_1.charge_for_share_of_room(self.guest_1)
        self.assertEqual(487.5, self.guest_1.wallet)