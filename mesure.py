import numpy as np
import RPi.GPIO as io
import time
from numpy.random import normal

trig = 18
echo = 24


def mesure_distance():
    io.output(trig, True)
    time.sleep(10e-6)
    io.output(trig, False)

    StartTime = time.time()
    StopTime = time.time()

    while io.input(echo) == 0:
        StartTime = time.time()

    while io.input(echo) == 1:
        StopTime = time.time()

    dt = StopTime - StartTime
    distance = (dt * 340 * 1e2) / 2
    # handle strage cases
    if distance > 400:
        distance = 400
    if distance < 0:
        distance = 0
    return distance


def mesure_distance_fake(d=50, sigma=1):
    return normal(d, sigma)


def streem_distance(d=50, sigma=1, fake=True):
    k = 0
    distances = []
    while True:
        if fake:
            dist = mesure_distance_fake(d, sigma)
        else:
            dist = mesure_distance()
        distances.append(dist)
        yield k, float("{:.2f}".format(dist)), float(
            "{:.2f}".format(np.mean(distances))
        ), float("{:.2f}".format(np.std(distances)))
        k += 1
