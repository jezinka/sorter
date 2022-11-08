#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from adafruit_servokit import ServoKit  # https://circuitpython.readthedocs.io/projects/servokit/en/latest/

# Parameters
MIN_IMP = 500
MAX_IMP = 2500
MIN_ANG = 0
MAX_ANG = 90

# Objects
pca = ServoKit(channels=16)
servo = pca.servo[0]


def main():
    servo.set_pulse_width_range(MIN_IMP, MAX_IMP)

    while True:
        for j in range(MIN_ANG, MAX_ANG, 1):
            servo.angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG, MIN_ANG, -1):
            servo.angle = j
            time.sleep(0.01)
        servo.angle = None  # disable channel
        time.sleep(0.5)


if __name__ == '__main__':
    main()
