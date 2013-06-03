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
