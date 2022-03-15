def dec2bin(num):
    return [int(e) for e in bin(num)[2:].zfill(8)]

def dec2dac(num):
    GPIO.output(dac, dec2bin(num))
    return (dec2bin(num))

import RPi.GPIO as GPIO

dac=[26,19,13,6,5,11,9,10]
bits=len(dac)
levels=2**bits
max_volt=3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 1000)
p.start(0)

try:
    while True:
        s=input('Enter a dutycycle in percents (any letter to exit) >')
        if float(s)>0:
            dc=float(s)
            if 0<=dc<=100:
                p.ChangeDutyCycle(dc)
            else:
                print('Entered value is too high')
            
    
        else:
            print('Entered value is not a positive integer')
except ValueError:
    print('Shutting down...')

finally:
    p.stop()
    GPIO.output(2, GPIO.LOW)
    GPIO.cleanup(2)
    print('GPIO cleanup completed')