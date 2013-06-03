#!/usr/bin/python

import sys
import serial
import thread
# Simple module to enable reading a single character at a time in python
from getch import getch

def reader(soc):
    while soc.isOpen():
        sys.stdout.write(soc.read())
        sys.stdout.flush()

def writer(soc, txt):
    if soc.isOpen():
        soc.write(txt)
        soc.flush()

def main():
    dev = sys.argv[1]
    ser = serial.Serial(dev, 9600)
    thread.start_new_thread(reader,(ser,))

    while ser.isOpen():
        txt = getch()
        sys.stdout.write(txt)
        if txt == 'q':
            ser.close()
        else:
            writer(ser, txt)

if __name__ == '__main__':
    main()
