from pynput.keyboard import Controller, Key
from time import sleep
from gpiozero import *
import RPi.GPIO as GPIO

BUT_A = Button(9)
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
