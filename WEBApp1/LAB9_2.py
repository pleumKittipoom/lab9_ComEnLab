# from flask import Flask 
from flask import Flask 
app = Flask(__name__) 

import RPi.GPIO as GPIO
import time
LED1 = 18
LED2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)



@app.route('/<led>/<state>') 
def led(led,state): 
    if(led == "led1"):
        if(state == "on"):
            GPIO.output(LED1, True)
            return f'<h3>LED 1 - ON</h3>'
        elif (state == "off"):
            GPIO.output(LED1, False)
            return f'<h3>LED 1 - OFF</h3>'

    elif(led == "led2"):
        if(state == "on"):
            GPIO.output(LED2, True)
            return f'<h3>LED 2 - ON</h3>'
        elif (state == "off"):
            GPIO.output(LED2, False)
            return f'<h3>LED 2 - OFF</h3>'
    



@app.route('/')
def index():
    return 'Lab 9_4'
    
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')