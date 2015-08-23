#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# main.py
# main script

# import sys
# import os
# import serial
# import time
import datetime
import sensor
import xively_test
import web

import logging
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger()


# --------------------
#
# --------------------
if __name__ == '__main__':
    log.info("Start main.py")
    ret = sensor.update()
    if ret is True:
        log.info("sensor update successful")
        atm = sensor.get_atm()
        tmp = sensor.get_tmp()
        hum = sensor.get_hum()
        lux = sensor.get_lux()

        log.debug("atm:" + str(atm))
        log.debug("tmp:" + str(tmp))
        log.debug("hum:" + str(hum))
        log.debug("lux:" + str(lux))

        d = datetime.datetime.today()
        log.debug("today:%s" % (d))

        utc_now = datetime.datetime.utcnow()
        log.debug("utcnow:%s" % (utc_now))

        xively_test.set_time(utc_now)
        xively_test.set_value(atm, tmp, hum, lux)
        xively_test.update()

        web.set_time(utc_now)
        web.set_value(atm, tmp, hum, lux)
        web.update()
    else:
        log.error("sensor update fail")

    log.info("Finish main.py")


# end of main.py
