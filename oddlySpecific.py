import keyboard
from time import *

def giveResources():
    print("[+] Giving resources")
    for i in range(10):
        keyboard.press_and_release('enter')
        sleep(0.2)
        keyboard.write('give me liberty or give me coin')
        sleep(0.2)
        keyboard.press_and_release('enter')
        sleep(0.2)
    for i in range(10):
        keyboard.press_and_release('enter')
        sleep(0.2)
        keyboard.write('medium rare please')
        sleep(0.2)
        keyboard.press_and_release('enter')
        sleep(0.2)
    for i in range(10):
        keyboard.press_and_release('enter')
        sleep(0.2)
        keyboard.write('<censored>')
        sleep(0.2)
        keyboard.press_and_release('enter')
        sleep(0.2)


while True:
    if keyboard.read_key() == "]":
        giveResources()
        break
