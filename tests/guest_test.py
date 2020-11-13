import unittest
from classes.guest import Guest
from classes.room import Room
#from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
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
    def test_guest_name(self):
        self.assertEqual("Eddie Vedder", self.guest_1.name)


