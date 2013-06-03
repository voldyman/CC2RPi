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


import threading
from serial import Serial
from time import sleep
import sys

if len(sys.argv) < 2:
    print 'Syntax: server.py <serial port>'
    exit()

dev = sys.argv[1]

class UARTHandler(threading.Thread):
    data = ''

    def run(self):
        ser = Serial(dev, 9600)
        while ser.isOpen():
            txt = ser.read()
            ser.flush()
            self.data = self.data + txt

#recv_thread.join()

from flask import Flask

app =  Flask(__name__)

@app.route('/')
def index():
    return open('web.html','r').read()

@app.route('/status')
def status():
    print recv_thread.data
    return recv_thread.data

recv_thread = UARTHandler()

def main():
    recv_thread.start()
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
