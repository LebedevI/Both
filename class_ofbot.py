import pyautogui
from settings import *

class create():
    def mycreate(self, unit, coordinate, objects):
        self.unit = unit
        self.coordinate = coordinate
        self.objects = objects
        
    def get_create(self):
        pyautogui.press(self.unit)
        pyautogui.click(self.objects,duration = speed)
        pyautogui.click(self.coordinate, duration = speed)
        
        