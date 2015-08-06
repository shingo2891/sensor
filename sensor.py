#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# sensor.py
# Get sensor data from arduino

import sys
import os
import serial
import time

import logging
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger()


#For import check
#print sys.path

Atmospheric = 0
Temperature = 0.0
Humidity    = 0.0
Light       = 0.0

def get_atm():
    return Atmospheric

def get_tmp():
    return Temperature

def get_hum():
    return Humidity

def get_lux():
    return Light

#----------------
#
#---------------
def update():
    log.debug("sensor.update()")
    com = serial.Serial()

    com.port="/dev/ttyACM0"
    com.baudrate=9600
    com.bytesize=8
    com.parity="N"
    com.stopbits=1
    com.timeout=1
    com.xonxoff=0
    com.rtscts=0
    com.writeTimeout=None

    com.open()
    com.setDTR(True)

    time.sleep(2.0)

    #接続確認
    com.write("$AA\n")
    log.debug("PI->SENSOR:$AA\n")
    mes = str(com.readline())
    mes = mes.rstrip()
    log.debug("PI<-SENSOR:" + mes)

    if( mes=="$0C,OK" ):
        time.sleep(1.0)
        com.write("$01\n")
        log.debug("PI->SENSOR:$01\n")
        mes = str(com.readline())
        mes = mes.rstrip()
        log.debug("PI<-SENSOR:" + mes)
        out_list = mes.split(",")
#        log.debug(out_list)
#        log.debug(out_list[1])
#        log.debug(out_list[2])
#        log.debug(out_list[3])
#        log.debug(out_list[4])

        global Temperature
        global Humidity
        global Light
        global Atmospheric
        
        Temperature = float(out_list[1])
        Humidity    = float(out_list[2])
        Light       = float(out_list[3])
        Atmospheric = float(out_list[4])
    else:
        log.error("sensor:connection failed")
        com.close()
        return False
    
    #close
    com.close()
    return True

#----------------
#
#---------------
if __name__ == '__main__':
    log.debug("Start sensor.py")
    ret = update()
    log.debug("atm:" + str(Atmospheric))
    log.debug("tmp:" + str(Temperature))
    log.debug("hum:" + str(Humidity))
    log.debug("lux:" + str(Light))
    log.debug("Finish sensor.py")

