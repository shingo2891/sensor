#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# web.py
# Upload data to web server
import requests
import datetime

import logging
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger()


# --------------------
#
# --------------------
def set_time(time_utc):
    log.debug("web.set_time()")
    global time
    time = time_utc
    log.debug("time:" + str(time))


# --------------------
#
# --------------------
def set_value(arg_atm, arg_tmp, arg_hum, arg_lux):
    log.debug("web.set_value()")
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


# --------------------
#
# --------------------
def update():
    log.debug("web.update")
    d = datetime.datetime.now()

    date = d.strftime("%Y%m%d")
    time = d.strftime("%H:%M:%S")

    url = "http://192.168.0.101:8080/sensor/sensor.php?"
    url = url + "date=" + date + "&"
    url = url + "time=" + time + "&"
    url = url + "tmp=" + str(tmp) + "&"
    url = url + "hum=" + str(hum) + "&"
    url = url + "lux=" + str(lux) + "&"
    url = url + "atm=" + str(atm)

    dbg_str = "Request URL: " + url
    log.debug(dbg_str)

    req = requests.get(url)

    dbg_str = "Response: " + str(req)
    log.debug(dbg_str)


# --------------------
# main
# --------------------
if __name__ == '__main__':
    print "Start web.py"

    date = "20991231"
    time = "00:00:00"
    tmp = 99.99
    hum = 88.88
    lux = 999
    atm = 1999.9

    url = "http://192.168.0.101:8080/sensor/sensor.php?"
    url = url + "date=" + date + "&"
    url = url + "time=" + time + "&"
    url = url + "tmp=" + str(tmp) + "&"
    url = url + "hum=" + str(hum) + "&"
    url = url + "lux=" + str(lux) + "&"
    url = url + "atm=" + str(atm)

    dbg_str = "Request URL: " + url
    log.debug(dbg_str)

    req = requests.get(url)

    dbg_str = "Response: " + str(req)
    log.debug(dbg_str)

    print "End web.py"

# end of web.py
