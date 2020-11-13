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