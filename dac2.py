def dec2bin(num):
    return [int(e) for e in bin(num)[2:].zfill(8)]

def dec2dac(num):
    GPIO.output(dac, dec2bin(num))
    return (dec2bin(num))

import RPi.GPIO as GPIO
import time

dac=[26,19,13,6,5,11,9,10]
bits=len(dac)
levels=2**bits
max_volt=3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        s=input('Enter an period of a signal >')
        if float(s)>0:
            t=float(s)/512
            for i in range(256):
                dec2dac(i)
                time.sleep(t)
            for i in range(255,-1,-1):
                dec2dac(i)
                time.sleep(t)
            

        
        else:
            print('Entered value is not positive')
            continue
except ValueError:
    print('Entered number is not a number')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')