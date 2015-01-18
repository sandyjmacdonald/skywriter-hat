#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import skywriter
import signal

unicorn.brightness(0.4)
unicorn.rotation(270)

@skywriter.move()
def palette(x, y, z):
	h = x
	s = y
	v = 1 - z
        for j in range(8):
                for i in range(8):
                        rgb = colorsys.hsv_to_rgb(h, s, v)
                        r = int(rgb[0]*255.0)
                        g = int(rgb[1]*255.0)
                        b = int(rgb[2]*255.0)
                        unicorn.set_pixel(i, j, r, g, b)
        unicorn.show()
        time.sleep(0.0005)

signal.pause()
