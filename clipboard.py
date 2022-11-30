import pyautogui

import time
print()
#input
word = input('Sentence: ')
num = int(input('how often?: '))

#Time till start after input
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Go')

#How often typed
for _ in range(num):
    #message
    pyautogui.typewrite(word)
    #press enter
    pyautogui.press("enter")