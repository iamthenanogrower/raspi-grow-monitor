# new-dawn branch
Gonna try some cool stuff here.

# raspi-grow-monitor
This is a very simple indoor grow monitor for Raspberry Pi.

It collects data with python-scripts talking to sensors and pushing it to mysql.
You can then monitor this data in real-time through php/ajax on a web browser.

[Make sure you are running something like apache2, php and mysql on your raspi.](https://howtoraspberrypi.com/how-to-install-web-server-raspberry-pi-lamp/)

If you are a rookie to mysql I highly recommend installing phpmyadmin.

## Installation
* Connect temperature sensor to GPIO pin #4 and soil moisture sensor (DO) to GPIO pin #21.

* [Turn on GPIO/1-wire and make sure you can read the temperature sensor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20)

* Install the pymysql library for Python:
```
sudo apt-get install python-pymysql
```

* Clone the html folder to your /var/www/html/whatever folder.

* Clone the scripts folder to preferably /home/pi/scripts and make sure they're executable.

* To make the scripts autorun on boot, edit /etc/profile and add these lines to the bottom:
```
sudo python /home/pi/scripts/moist.py
sudo python /home/pi/scripts/temp.py
```

* Import the rasp-grow-monitor.sql database to your sql server, don't forget add a user with priveleges to use this database.

* Edit the database login details in scripts/moist.py, scripts/temp.py and html/ajax.php accordingly.

## Usage
When installed properly, access host/index.php in your web browser.

## Parts used
* Raspberry Pi 3 #B + 8GB micro sd (with raspbian)
* Temperature sensor DS18B20 (don't forget a 4.7KOhm resistor)
* Soil moisture sensor FC-28

## Pictures
[Screenshot](https://i.redd.it/ysn2knerejq21.png)

[My setup](https://i.imgur.com/FnV2sxv.jpg)

