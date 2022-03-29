def dec2bin(num):
    return [int(e) for e in bin(num)[2:].zfill(8)]

def dec2dac(num):
    GPIO.output(dac, dec2bin(num))
    return (dec2bin(num))

def bin2dec(y):
    x = list(map(str, y))
    return int(''.join(x), base = 2 )

def adc():
    outp = [0]*8
    for i in range(8):
        outp[i] = 1
        GPIO.output(dac, outp)
        time.sleep(0.002)
        com_out = GPIO.input(comp)
        if not com_out:
            outp[i] = 0
    dv = bin2dec(outp)
    volt = dv*3.3/256
    print('Digital value: {} , Analog value: {:.2f}'.format(dv, volt))
    return dv


import RPi.GPIO as GPIO
import time
import math

dac=[26,19,13,6,5,11,9,10]
leds = [21,20,16,12,7,8,25,24]
bits=len(dac)
levels=2**bits
max_volt=3.3
comp = 4
troy = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troy, GPIO.OUT)

GPIO.output(troy, GPIO.HIGH)

try:
    while True:
        dv = adc()
        num = math.ceil(dv*8/256)
        vol = [1]*num
        while len(vol)<8:
            vol.append(0)
        GPIO.output(leds, vol)


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(leds)
    print('GPIO cleanup completed')