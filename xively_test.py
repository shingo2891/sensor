#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# xively_test.py
# Upload xively

import sys
import os
import xively
import xively_key
import subprocess
import time
import datetime
import requests
import sensor

import logging
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger()


#For include check
#print sys.path

atm = 0.0
tmp = 0.0
hum = 0.0
lux = 0.0
time = 0

# extract feed_id and api_key from environment variables
FEED_ID = xively_key.FEED_ID
API_KEY = xively_key.API_KEY
DEBUG = True

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# function to return a datastream object. 
# This either creates a new datastream,
# or returns an existing one
def get_datastream(feed):
    try:
        datastream = feed.datastreams.get("Sensor")
        return datastream
    except:
        datastream = feed.datastreams.create("Sensor", tags="atom")
        return datastream

#----------------
#
#---------------
def set_time( time_utc):
    log.debug("xively_test.set_time()")
    global time
    time = time_utc
    log.debug("time:" + str(time))


#----------------
#
#---------------
def set_value( arg_atm, arg_tmp, arg_hum, arg_lux ):
    log.debug("xively_test.set_value()")
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
    log.debug("xively_test.update()")
    # initialize api client
    api = xively.XivelyAPIClient(API_KEY)
    feed = api.feeds.get(FEED_ID)


    feed.datastreams = [
        xively.Datastream(id='Atmospheric', current_value=atm, at=time),
        xively.Datastream(id='Humidity', current_value=hum, at=time),
        xively.Datastream(id='Light', current_value=lux, at=time),
        xively.Datastream(id='Temperature', current_value=tmp, at=time),
    ]
    try:
        feed.update()
    except requests.HTTPError as e:
        log.error("HTTPError([0]): {1}".format(e.errno, e.strerror))


    log.debug("atm:" + str(atm))
    log.debug("tmp:" + str(tmp))
    log.debug("hum:" + str(hum))
    log.debug("lux:" + str(lux))


#    datastream = get_datastream(feed)
#    datastream.max_value = None
#    datastream.min_value = None

#    if DEBUG:
#        print "Updating Xively feed with values"

#    datastream.current_value = 1000 
#    datastream.at = datetime.datetime.utcnow()

#    try:
#        datastream.update()
#    except requests.HTTPError as e:
#        print "HTTPError([0]): {1}".format(e.errno, e.strerror)

#----------------
# main
#----------------
if __name__ == '__main__':
    d = datetime.datetime.today()
    print "%s" % (d)
    print "Start xively_test.py"
    ret = sensor.update()
    if( ret == True ):
        atm = sensor.get_atm()
        tmp = sensor.get_tmp()
        hum = sensor.get_hum()
        lux = sensor.get_lux()

        update()
    print "End xively_test.py"


