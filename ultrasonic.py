import RPi.GPIO as GPIO 
import subprocess
import signal
import os
import time

GPIO.setmode(GPIO.BOARD)

PIN_ECHO = 11
PIN_TRIGGER = 13

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

print("Sensor initialising...")

time.sleep(2)

def record():
    subprocess.Popen("python3 record.py", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

while True:
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1: 
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:", distance, "cm")

    if distance > 100:
        print("Not sensing")
    if distance < 100:
        break

    time.sleep(1)

record()
GPIO.cleanup()
