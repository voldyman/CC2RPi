
These scripts were written while testing UARTS with [raspberry pi](http://www.raspberrypi.org) and [elementary OS](http://elementaryos.org) at the [Inventrom](http://inventrom.com) office in Goa.

These are the basic scripts that we use for debuging and testing while developing devices for internet of things.

[**UARTS**](http://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter) are used to communicate with the sensors as they use very less battery and are very simple to setup.

these scripts are released under the GPLv3 license
##Requirements

* python-flask
* pyserial


##cat_serial.py
Read the data from serial port.

**Usage:**

    # ./cat_serial.py <serial port>
    example:
    # ./cat_serial.py /dev/ttyUSB0

##echo_to_serial.py
Send a file over a serial port.

**Usage:**

    # ./echo_to_serial.py <serial port> <file>
    example:
    # ./echo_to_serial.py /dev/ttyUSB0 ~/log.txt
## serial_to_web.py
Read data from serial port and display it on a webserver.
the script uses [Flask](http://flask.pocoo.org) web framework to host the website.

![UART Conneted to Raspberry pi](http://i.imgur.com/LtSTDM8l.jpg)

![UART Conneted to my laptop](http://i.imgur.com/7ONnY2ol.jpg)
