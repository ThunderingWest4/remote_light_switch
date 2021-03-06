import RPi.GPIO as gpio
import requests

#MAKE SURE THAT THERE IS A cred.txt WITH DEVICE CREDENTIALS IN DIRECTORY
print("Initializing Stuff")
#resistor set up so that when the switch is in the "off" position, it reads "on"

f = open("/home/pi/remote_light_switch/toPi/cred.txt", "r")
creds = f.read().split(" ")
f.close()
# Func is called Led to test wireless stuff and all, will change to motor in later stages
function_name = "Led"

swin=6
gpio.setmode(gpio.BCM)
gpio.setup(swin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

#gpio.setup(swin, gpio.IN)

initial = True

URL = "https://api.particle.io/v1/devices/" + creds[0] + "/" + function_name

one = False
zero = False

prevstate = 0
while True:
    inp = gpio.input(swin)
    if(((inp, prevstate) == (1, 1)) and (not one)):
        requests.post(URL, data={'args':"on", 'access_token':creds[1]})
	if not initial:
	        print("flipped")
	        one=True
	        zero=False
	else:
		initial=False
    elif(((inp, prevstate) == (0, 0)) and (not zero)):
        requests.post(URL, data={'args':"off", 'access_token':creds[1]})
	if not initial:
	        print("flipped")
	        zero=True
	        one=False
	else:
		initial=False
    #print(prevstate, inp)
    prevstate = inp
    #time.sleep(0.05)
