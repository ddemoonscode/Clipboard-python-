import pyautogui
import time

#Time between Message
time.sleep(2)
#How often typed
for i in range(50):
    #message
    pyautogui.typewrite("Hallo Luggi")
    #press enter
    pyautogui.press("enter")