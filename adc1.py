def dec2bin(num):
    return [int(e) for e in bin(num)[2:].zfill(8)]

def dec2dac(num):
    GPIO.output(dac, dec2bin(num))
    return (dec2bin(num))

def adc():
    for i in range(256):
        outp = dec2dac(i)
        time.sleep(0.002)
        com_out = GPIO.input(comp)
        if not com_out:
            volt = i*3.3/256
            print('Digital value: {} , Analog value: {:.2f}'.format(i, volt))
            return


import RPi.GPIO as GPIO
import time

dac=[26,19,13,6,5,11,9,10]
bits=len(dac)
levels=2**bits
max_volt=3.3
comp = 4
troy = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troy, GPIO.OUT)

GPIO.output(troy, GPIO.HIGH)

try:
    while True:
        
        adc()
        

except ValueError:
    print('Error')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')