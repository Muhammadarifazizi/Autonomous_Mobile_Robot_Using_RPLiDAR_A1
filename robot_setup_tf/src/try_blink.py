#!/usr/bin/env python3

import pyfirmata
import time

if __name__ == '__main__':
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    print("connection successfully started")

    led = board.digital[13]
    while True:
        led.write(1)
        time.sleep(1000)
        led.write(0)
        time.sleep(1000)