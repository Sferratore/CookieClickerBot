import unittest
import pygetwindow
import pyautogui

from Bot import Bot

class TestBot(unittest.TestCase):
    
    def test_get_size(self):
        # Arrange
        b = Bot()
        #Act
        size = b.get_display_size()
        #Assert
        self.assertTrue(size.startswith("Size"))
        

    def test_positioning(self):
        #Arrange
        b = Bot()
        #Act
        b.position_on_cookie()
        #Assert
        self.assertTrue(pyautogui.position() == (250, 500) and b.get_display_size() == "Size(width=1920, height=1080)")

    def test_click(self):
        #Arrange
        b = Bot()
        #Act
        isExecuted = b.click_cookie()
        #Assert
        self.assertTrue(isExecuted)

    def test_position_window(self):
        # Arrange
        b = Bot()
        # Act
        b.position_window()
        # Assert
        self.assertTrue(pygetwindow.getActiveWindow().endswith("Cookie Clicker - Google Chrome"))