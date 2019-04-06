#!/usr/bin/python
#
# raspi-grow-monitor - soil moisture sensor
# https://github.com/iamthenanogrower/raspi-grow-monitor
#
# thanks to the people who wrote parts of this code before me
#
import RPi.GPIO as GPIO
import time
import datetime
import pymysql

#gpio-pin for the moisture sensor, change accordingly
moistpin = 21

#db-details
db = pymysql.connect(host='localhost',
                     user='your_username',
                     passwd='your_password',
                     db='raspi-grow-monitor',
                     autocommit='True')

cur = db.cursor()

# tests whether water is present
# returns 0 for dry
# returns 1 for wet
def RCtime (RCpin):
    reading = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1) 
    GPIO.setup(RCpin, GPIO.IN)
    # this takes about 1 millisecond per loop cycle
    while True:
        if (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
        if reading >= 1000:
            return 0
        if (GPIO.input(RCpin) != GPIO.LOW):
            return 1

# main loop
while True:
    time.sleep(1)
    if RCtime(moistpin) == 1:
	# sensor is dry
        print "Sensor is dry"
        currentDT = datetime.datetime.now()
        query = 'UPDATE devices SET value="DRY", datetime=NOW() WHERE device="moist1"'
        cur.execute(query)
        query = 'INSERT INTO `log-moist1`(`value`, `datetime`) VALUES (0, NOW())'
        cur.execute(query)
        while True:
            time.sleep(1)
            if RCtime(moistpin) == 1:
                continue
            if RCtime(moistpin) == 0:
		# sensor is wet
                print "Sensor is wet again"
                print "Waiting for dry soil..."
                currentDT = datetime.datetime.now()
        	query = 'UPDATE devices SET value="WET", datetime=NOW() WHERE device="moist1"'
       		cur.execute(query)
		query = 'INSERT INTO `log-moist1`(`value`, `datetime`) VALUES (1, NOW())'
		cur.execute(query)
                break
