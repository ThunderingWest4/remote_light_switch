import RPi.GPIO as gpio
import requests
#MAKE SURE THAT THERE IS A cred.txt WITH DEVICE CREDENTIALS IN DIRECTORY

#resistor set up so that when the switch is in the "off" position, it reads "on"

f = open("/home/pi/remote_light_switch/toPi/cred.txt", "r")
creds = f.read().split(" ")
f.close()
function_name = ""

swout = 12
swin=6
gpio.setmode(gpio.BCM)
gpio.setup(swout, gpio.OUT)
gpio.setup(swin, gpio.IN)
gpio.output(swout, gpio.HIGH)

URL = "https://api.particle.io/v1/devices/" + creds[0] + "/" + function_name


prevstate = 3
while True:
    if((not gpio.input(swin)) and (gpio.input(swin) != prevstate)):
        #requests.post(URL, data={'args':"go", 'access_token':creds[1]})
        print("flip on")
    prevstate = gpio.input(swin)
    #print(prevstate, gpio.input(swin))
