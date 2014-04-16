__author__ = 'hesicong'

import serial
import sys

port = "/dev/tty.usbmodemfa131"
if len(sys.argv) != 1:
    port = sys.argv[1]

ser = serial.Serial(port, 19200, timeout=0.1)
while True:
    cmd = raw_input(">").upper()

    if cmd == "exit":
        break

    ser.write(cmd)
    print(ser.read(500))