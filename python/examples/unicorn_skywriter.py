#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np
import random
import skywriter
import signal

unicorn.brightness(0.4)
unicorn.rotation(270)

def make_gaussian(fwhm, x0, y0):
	x = np.arange(0, 8, 1, float)
	y = x[:, np.newaxis]
	fwhm = fwhm
	gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
	return gauss

@skywriter.move()
def spot(x, y, z):
        x0 = x * 7
	y0 = y * 7
	h = 0.8
	fwhm = 5.0
        gauss = make_gaussian(fwhm, x0, y0)
        for j in range(8):
                for i in range(8):
                        s = 0.8
                        v = gauss[i,j]
                        rgb = colorsys.hsv_to_rgb(h, s, v)
                        r = int(rgb[0]*255.0)
                        g = int(rgb[1]*255.0)
                        b = int(rgb[2]*255.0)
                        unicorn.set_pixel(i, j, r, g, b)
        unicorn.show()
        time.sleep(0.0005)

signal.pause()
