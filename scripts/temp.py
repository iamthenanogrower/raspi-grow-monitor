#!/usr/bin/python
#
# raspi-grow-monitor - temperature sensor
# https://github.com/iamthenanogrower/raspi-grow-monitor
#
# thanks to the people who wrote parts of this code before me
#
import os
import glob
import time
import pymysql

# enter the db
db = pymysql.connect(host='localhost',
                     user='your_username',
                     passwd='your_password',
                     db='raspi-grow-monitor',
                     autocommit='True')

cur = db.cursor()

# temp sensor things - don't forget to install/config these properly
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# functions
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# main loop
while True:
        # temp reading
        temp_c = str(read_temp())
	query = 'UPDATE devices SET value=' + temp_c + ' WHERE device="temp1"'
	cur.execute(query)

time.sleep(2)
