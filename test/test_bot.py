import unittest
from Bot import Bot

class TestBot(unittest.TestCase):
    
    def test_get_size(self):
        # Arrange
        b = Bot()
        #Act
        size = b.get_display_size()
        #Assert
        self.assertTrue(size.startswith("Size"))
        
