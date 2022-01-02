#!/usr/bin/env python
# coding: utf-8
from datetime import datetime
import logging
import time
import serial
import RPi.GPIO as GPIO

gruen=22
gelb=27
rot=17
k=1

logging.basicConfig(filename='/home/wzJvhTLp/co2.txt',level=logging.DEBUG)

GPIO.setwarnings(False)
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(gruen, GPIO.OUT)
GPIO.setup(gelb, GPIO.OUT)
GPIO.setup(rot, GPIO.OUT)

def setAmpel(wert):
    if 400<wert<1000:
        GPIO.output(gruen,GPIO.HIGH)
        GPIO.output(gelb,GPIO.LOW)
        GPIO.output(rot,GPIO.LOW)
    if 1000<=wert<1400:
        GPIO.output(gruen,GPIO.LOW)
        GPIO.output(gelb,GPIO.HIGH)
        GPIO.output(rot,GPIO.LOW)
    if 1400<=wert:
        GPIO.output(gruen,GPIO.LOW)
        GPIO.output(gelb,GPIO.LOW)
        GPIO.output(rot,GPIO.HIGH)

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
)

while True:

    command = bytearray([0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    ser.write(command)
    time.sleep(1)
    x=ser.read(9)
    if len(x)>= 4 and x[0] == 0xff and x[1] == 0x86:
        y=x[2]*256 + x[3]
        now=datetime.now()
        mytime=now.strftime("%Y-%m-%d_%H-%M-%S")
        co2=f"{mytime}: co2: {y}"
        logging.info(co2)
        setAmpel(y)
        sleepLog=f"{mytime}: sleeping 1 Min"
        logging.info(sleepLog)
        time.sleep(60)
            
#GPIO.cleanup()