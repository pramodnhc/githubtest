import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.IN)
gpio.setup(5, gpio.OUT)

while True:
    input_value = gpio.input(7)
    if input_value == False:
        print('The button has been pressed...')
        gpio.output(5,gpio.HIGH)
    else
        gpio.output(5,gpio.LOW)