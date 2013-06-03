#!/usr/bin/python
'''
    BEGIN LICENSE

    Copyright (C) 2013 Inventrom <contactus@inventrom.com>
    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU Lesser General Public License version 3, as published
    by the Free Software Foundation.

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranties of
    MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
    PURPOSE.  See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program.  If not, see <http://www.gnu.org/licenses/>

    END LICENSE
'''


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
