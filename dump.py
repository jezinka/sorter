#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from adafruit_servokit import ServoKit  # https://circuitpython.readthedocs.io/projects/servokit/en/latest/

# Parameters
MIN_IMP = 500
MAX_IMP = 2500

# Objects
pca = ServoKit(channels=16)
servo = pca.servo[1]


def dump_right():
    servo.set_pulse_width_range(MIN_IMP, MAX_IMP)

    for j in range(90, 0, -1):
        servo.angle = j
        time.sleep(0.01)
    for j in range(0, 90, 1):
        servo.angle = j
        time.sleep(0.01)
    servo.angle = None  # disable channel


def dump_left():
    servo.set_pulse_width_range(MIN_IMP, MAX_IMP)

    for j in range(90, 180, 1):
        servo.angle = j
        time.sleep(0.01)
    for j in range(180, 90, -1):
        servo.angle = j
        time.sleep(0.01)
    servo.angle = None  # disable channel

if __name__ == '__main__':
    dump_right()
    dump_left()
