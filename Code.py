from time import sleep
from threading import Thread
from pynput import keyboard
import pyautogui
import random

ekranX, ekranY = pyautogui.size()
x = int(ekranX/2)
y = int(ekranY/2)

def on_press(key, abortKey='esc'):    
    try:
        k = key.char 
    except:
        k = key.name
    if k == abortKey:
        print('end loop ...')
        return False

def dongu():
    while True:
        sleep(random.randint(450, 600))
        randomNumber = random.randint(100, 200)
        pyautogui.moveTo(x, y-randomNumber)
        sleep(1)
        pyautogui.click()
        sleep(random.randint(450, 600))
        randomNumber = random.randint(100, 200)
        pyautogui.moveTo(x, y+randomNumber)
        sleep(1)
        pyautogui.click()

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start() 
    Thread(target=dongu, args=(), name='dongu', daemon=True).start()
    listener.join()
