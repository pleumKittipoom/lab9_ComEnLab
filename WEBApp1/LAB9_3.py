from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)
LED1 = 18
LED2 = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

@app.route('/')
def hello():
    return render_template('ex_led2.html')

@app.route('/led/<id>', methods=['POST'])
def led(id):
    led_state = request.form.get('led1State') if id == '1' else request.form.get('led2State')
    
    if id == '1':
        if led_state == 'ON':
            GPIO.output(LED1, GPIO.HIGH)
            ledstate = 'ON'
        else:
            GPIO.output(LED1, GPIO.LOW)
            ledstate = 'OFF'
    elif id == '2':
        if led_state == 'ON':
            GPIO.output(LED2, GPIO.HIGH)
            ledstate = 'ON'
        else:
            GPIO.output(LED2, GPIO.LOW)
            ledstate = 'OFF'

    return render_template('ex_led2.html', ledstate=ledstate, id=id)

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
