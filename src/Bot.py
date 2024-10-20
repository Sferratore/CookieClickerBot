import pyautogui

class Bot:

    def get_display_size(self):
        return pyautogui.size().__str__()

    def position_on_cookie(self):
        if self.get_display_size() == "Size(width=1920, height=1080)":
            pyautogui.moveTo(250, 500, duration=1)
        else:
            raise ValueError("Your screen size is not supported by this software!")
