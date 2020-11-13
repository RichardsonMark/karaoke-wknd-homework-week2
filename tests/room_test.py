import unittest
#from classes.guest import Guest
from classes.room import Room
#from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 =  Room("Yellow Submarine", 8, 50)
        self.room_2 =  Room("Purple Rain", 10, 60)
        self.room_3 =  Room("Blue Monday", 12, 70)
        self.room_4 =  Room("Black and White Town", 15, 80)
        self.room_5 =  Room("Pink Cadillac", 20, 90)
        self.room_6 =  Room("99 Red Baloons", 22, 100)
        


#    @unittest.skip("Delete this line to run the test")
    def test_room_name(self):
        self.assertEqual("Yellow Submarine", self.room_1.name)
