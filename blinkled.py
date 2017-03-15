# import curses and GPIO
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

while True:

 GPIO.output(5,GPIO.HIGH)
 time.sleep(0001)
 GPIO.output(5,GPIO.LOW)
 time.sleep(0001)

GPIO.cleanup()
