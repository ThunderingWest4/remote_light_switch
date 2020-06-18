#import RPi.GPIO
import requests
#MAKE SURE THAT THERE IS A cred.txt WITH DEVICE CREDENTIALS IN DIRECTORY

f = open("cred.txt", "r")
creds = f.read().split(" ")
f.close()
function_name = ""

URL = "https://api.particle.io/v1/devices/" + creds[0] + "/" + function_name

while True:
    if("Switch is on" == True):
        requests.post(URL, data={'args':"go", 'access_token':creds[1]})