import pyautogui
import pygetwindow

class Bot:

    def get_display_size(self):
        return pyautogui.size().__str__()

    def position_on_cookie(self):
        if self.get_display_size() == "Size(width=1920, height=1080)":
            pyautogui.moveTo(250, 500, duration=1)
        else:
            raise ValueError("Your screen size is not supported by this software!")

    def click_cookie(self):
        pyautogui.click()
        return True

    def position_window(self):
        windows = pygetwindow.getAllTitles()

        target_window = None
        for window in windows:
            if window.title().endswith('Cookie Clicker - Google Chrome'):
                print(window.title())
                target_window = pygetwindow.getWindowsWithTitle(window.title())
                break

        if target_window:
            target_window.activate()
        else:
            raise Exception("Cookie Clicker window not found.")
