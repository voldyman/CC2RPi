#!/usr/bin/python

import serial
import sys

if len(sys.argv) < 2:
    print 'Syntax: cat_serial <serial port>'
    exit()

dev = sys.argv[1]
ser = serial.Serial(dev, 9600)

for data in iter(ser.read,''):
    sys.stdout.write(data)
    sys.stdout.flush()
