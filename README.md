# raspi-grow-monitor
This is a very simple indoor grow monitor for Raspberry Pi.

It collects data with python-scripts talking to sensors and pushing it to mysql.
You can then monitor this data in real-time through php/ajax on a web browser.

Make sure you are running something like apache2, php and mysql on your raspi.
If you are a rookie to mysql I highly recommend installing phpmyadmin.

Screenshot: https://i.redd.it/ysn2knerejq21.png

My setup: https://i.imgur.com/Vaa0UkG.jpg

## Installation
* Clone html to your /var/www/html/whatever folder.

* Clone scripts to preferably /home/pi and make sure they're executable.

* To make the scripts autorun on boot you can add these lines to the bottom of /etc/profile:

```
sudo python /home/pi/scripts/moist.py &
sudo python /home/pi/scripts/temp.py &
```

* Connect temperature sensor to GPIO pin #4 and soil moisture sensor (DO) to GPIO pin #21.

* Import the grow.sql database to your sql server, don't forget add a user with priveleges to use this database.

* Edit the database login details in scripts/moist.py, scripts/temp.py and html/ajax.php accordingly.

## Usage
When installed properly, access host/index.php in your web browser.

## Parts used
* Raspberry Pi 3 #B + 8GB micro sd (with raspbian)
* Temperature sensor DS18B20 (don't forget a 4.7KOhm resistor)
* Soil moisture sensor FC-28
