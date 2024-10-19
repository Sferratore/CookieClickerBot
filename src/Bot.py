import pyautogui

class Bot:

    def get_display_size(self):
        return pyautogui.size().__str__()