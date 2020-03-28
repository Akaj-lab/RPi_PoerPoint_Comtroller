from pynput.keyboard import Controller, Key
from time import sleep
import RPi.GPIO as GPIO

GPIO.setup(17, GPIO.IN)


keyboard = Controller()

while True:
    if GPIO.input(17):
        print('is pressed')
        keyboard.press(' ')
        keyboard.release(' ')
        sleep(0.5)
    else:
        print('not')
