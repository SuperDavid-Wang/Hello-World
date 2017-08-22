import  RPi.GPIO as gpio
import  time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7,gpio.OUT)
gpio.output(7,True)
time.sleep(5)
gpio.cleanup()

