#!/usr/bin/python

import serial
import sys
from time import sleep

if len(sys.argv) < 3:
    print 'Syntax: cat_to_serial <serial> <file>'
    exit()

dev = sys.argv[1]
file =  sys.argv[2]

ser = serial.Serial(dev, 9600)

with open(file) as fp:
        for line in iter(fp.readline, ''):
            ser.write(line)
            ser.flush()
            sleep(0.12)
