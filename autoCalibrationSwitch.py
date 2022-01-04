#!/usr/bin/env python
# coding: utf-8
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
)

command = bytearray([0xff, 0x01, 0x79, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
ser.write(command)

file = open("autoCalibration.conf", "w+")
value=file.read()
if (value=="1"):
    print("Auto Calibration wurde deaktiviert")
    file.write("0")
else:
    print("Auto Calibration wurde aktiviert")
    file.write("1")
file.close()
