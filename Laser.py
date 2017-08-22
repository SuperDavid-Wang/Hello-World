import  RPi.GPIO as gpio
import  time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(32,gpio.OUT)
gpio.output(32,True)
time.sleep(100)
gpio.cleanup()

