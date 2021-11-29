import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
pins=(23)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)
GPIO.setwarnings(False)
@app.route('/')
def index():
    return render_template('on.html')

@app.route('/on')
def on():
   GPIO.output(pins,GPIO.HIGH)
   return render_template('on.html')
@app.route('/off')
def off():
   GPIO.output(pins,GPIO.LOW)
   return render_template('on.html')




if __name__ == "__main__":
   app.run(host='192.168.0.104', port=80, debug=True)
