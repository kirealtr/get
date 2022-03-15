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
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        s=input('Enter an integer between 0 and 255 ("q" to exit) >')

        if s.isdigit():
            num=int(s)

            if 0<=num<=255:
                signal = dec2dac(num)
                volt=(num/256)*max_volt
                print('Entered value: {:^3} -> {}, voltage={:.2f}'.format(num, signal, volt))
            else:
                print('Entered value is too high')
                continue

        elif s=='q':
            print('Shutting down...')
            break
        
        else:
            print('Entered value was not a positive integer')
            continue

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')