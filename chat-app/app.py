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
