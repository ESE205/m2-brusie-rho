import RPi.GPIO as GPIO
import time
from time import sleep
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

SWITCH_PIN = 8
GPIO.setup(SWITCH_PIN, GPIO.IN)
LED_PIN = 11
LED_IS_ON = False
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

rate = int(input('Enter interval:'))
duration = int(input('Enter duration:'))

DEBUG = False
if '-debug' in sys.argv:
    DEBUG = True

if GPIO.input(SWITCH_PIN):
    with open('data.txt', 'w') as f:
        f.write('numbers:\n')
        for i in range(0,duration):
            GPIO.output(LED_PIN, LED_IS_ON)
        
            f.write(f'{time.time():1.0f} \t {LED_IS_ON}\n')
            if DEBUG:
                print(f'{time.time():1.0f} \t {i} \t {LED_IS_ON}\n')
            LED_IS_ON = not(LED_IS_ON)
            time.sleep(rate)
        
GPIO.cleanup();


    


