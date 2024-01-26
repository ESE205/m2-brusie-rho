import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

SWITCH_PIN = 7
GPIO.setup(SWITCH_PIN, GPIO.IN)
LED_PIN = 11
LED_IS_ON = True
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)


    

while True:
    GPIO.output(LED_PIN, LED_IS_ON)
    print(LED_IS_ON)
    if GPIO.input(SWITCH_PIN) == True:
        LED_IS_ON = True
        print('hello')
    else:
        LED_IS_ON = False
        print('hi')
    


GPIO.cleanup()
