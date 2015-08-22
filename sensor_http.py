#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sensor_http.py
# Upload data to web server
import requests
import datetime

import logging
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger()

#----------------
#
#---------------
def set_time(time_utc):
    log.debug("sensor_http.set_time()")
    global time
    time = time_utc
    log.debug("time:" + str(time))


#----------------
#
#---------------
def set_value( arg_atm, arg_tmp, arg_hum, arg_lux ):
    log.debug("sensor_http.set_value()")
    global atm
    global hum
    global lux
    global tmp
    atm = arg_atm
    tmp = arg_tmp
    hum = arg_hum
    lux = arg_lux
    log.debug("atm:" + str(atm))
    log.debug("tmp:" + str(tmp))
    log.debug("hum:" + str(hum))
    log.debug("lux:" + str(lux))


#----------------
#
#---------------
def update():
    d = datetime.datetime.now()

    date = d.strftime("%Y%m%d")
    time = d.strftime("%H:%M:%S")
    tmp = "30.00"
    lux = "300"
    atm = "1024.6" 

    url = "http://192.168.0.110/sensor/sensor.php?"
    url = url + "date=" + date + "&"
    url = url + "time=" + time + "&"
    url = url + "tmp=" + tmp + "&"
    url = url + "lux=" + lux + "&"
    url = url + "atm=" + atm
    log.debug(url)

    req = requests.get(url)
    log.debug(req)


#----------------
# main
#----------------
if __name__ == '__main__':
    print "Start sensor_http.py"
    print "End sensor_http.py"

