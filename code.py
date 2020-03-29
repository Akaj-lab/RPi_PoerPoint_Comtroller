#import all libraries
from pynput.keyboard import Controller, Key
from time import sleep
import RPi.GPIO as GPIO

#initialize GPIO pin 17 (real pin 11)
GPIO.setup(17, GPIO.IN)

#initialize keyboard
keyboard = Controller()

#main loop
while True:
    #reads GPIO pin 17
    if GPIO.input(17):
        print('is pressed')
        #presses spacebar
        keyboard.press(' ')
        keyboard.release(' ')
        #waits for .5 second for debouncing
        sleep(0.5)
    else:
        print('not')
