#!/usr/bin/python

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
