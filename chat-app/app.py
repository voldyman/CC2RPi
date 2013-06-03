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
import thread
import parser
import serial
from time import sleep

def read_serial(ser, callback):
    while ser.isOpen():
        line = ser.readline()
        cmd = parser.parse(line)
        if cmd is not None:
            callback(cmd)


def cmd_read(cmd):
    sys.stdout.write('\n'+cmd.sender+'>'+ cmd.text)

def main():
    ser = serial.Serial(sys.argv[1], 9600)
    thread.start_new_thread(read_serial, (ser, cmd_read,))

    name = raw_input('Enter Name:')
    to = raw_input('Enter Receiver:')

    while True:
        text = raw_input('>>>')
        line = '@MSG ' + name + ' ' + to + ' :' + text + "\r\n"
        ser.write(line)

if __name__ == '__main__':
    main()
