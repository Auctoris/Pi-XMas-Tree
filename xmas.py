import RPi.GPIO as GPIO
import time
import random

LEDs = [4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23, 22, 2]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for led in LEDs:
    GPIO.setup(led, GPIO.OUT)

while 1:
    try:
        ok = False
        while not ok:
            L1 = random.randint(0,24)
            L2 = random.randint(0,24)
            L3 = random.randint(0,24)
            if L1 == L2 or L1 == L3 or L2 == L3:
                ok = False
            else:
                ok = True

            GPIO.output(LEDs[L1], GPIO.HIGH)
            GPIO.output(LEDs[L2], GPIO.HIGH)
            GPIO.output(LEDs[L3], GPIO.HIGH)

            t1 = random.gauss(0.225, 0.015)
            time.sleep(t1)

            GPIO.output(LEDs[L1], GPIO.LOW)
            t2 = random.uniform(0.1, 0.3)
            time.sleep(t2)
            GPIO.output(LEDs[L2], GPIO.LOW)
            t3 = random.uniform(0.15, 0.4)
            time.sleep(t3)
            GPIO.output(LEDs[L3], GPIO.LOW)

    except KeyboardInterrupt:        
        GPIO.cleanup()
