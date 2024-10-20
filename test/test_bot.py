import unittest
import pygetwindow
import pyautogui
import time
import keyboard

from Bot import Bot

class TestBot(unittest.TestCase):
    
    def test_get_size(self):
        # Arrange
        b = Bot()
        #Act
        size = b.get_display_size()
        #Assert
        self.assertTrue(size.startswith("Size"))

    # Questo test può uscire positivo solo e unicamente se hai Cookie Clicker aperto.
    def test_position_window(self):
        # Arrange
        b = Bot()
        # Act
        b.position_window()
        gw = pygetwindow.getActiveWindow()
        time.sleep(10)
        # Assert
        self.assertTrue(gw.title.endswith("Cookie Clicker - Google Chrome"))

    def test_pointer_positioning(self):
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


    def test_execute_bot(self):
        # Arrange
        b = Bot()
        # Act
        b.execute_bot()
        #Assert
        self.assertTrue(True)

