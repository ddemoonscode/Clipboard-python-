import pyautogui

import time

#input
word = input('Sentence: ')
num = int(input('how often?: '))

#Time till start after input
time.sleep(3)
#How often typed
for i in range(num):
    #message
    pyautogui.typewrite(word)
    #press enter
    pyautogui.press("enter")