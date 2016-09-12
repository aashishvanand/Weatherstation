# IOT Weather Station
## Abstract
<p> The purpose of this Weather Station is to provide real time weather information to the user on demand. The weather station consists of Sensors capable of reading temperature, pressure, humidity, etc. These details are sent to a SQL Server that is hosted in a remote location. The android application then reads the data off the databse located in the server and presents it to the user. 
The existing system gets the data from satellites and sends it to the remote server from which the client side mobile application loads the data, this project takes the reading from the physical environment

## Components
<ol>
  <li> Raspberry Pi B+ [or later]</li>
  <li> Gobbler </li>
  <li> Breadboard </li>
  <li> Connecting wires </li>
  <li> DHT22 [or DHT11] Digital Humidity and Temperature Sensor </li>
  <li> BMP180 Sensor </li>
  <li> GPS Antenna </li>
  <li> GPS Reciever </li>
  <li> Power Source for Raspberry Pi </li>
  <li> Power Source for GPS Reciever</li>
  <li> An ethernet cable or a Wifi Module [USB ones work fine] </li>
</ol>

## Requirements
<ul>
  <li> Router with DHCP capability</li>
  <li> Wired or wireless Router </li>
  <li> Local SQL server [ensure static IP and DNS registration] or a web hosting  account that has SQL</li>
  <li> Android Phone </li>
</ul>

## Circuit Diagram
Download Fritzing from <a href="http://fritzing.org/download/">here</a> and open the <a href="https://github.com/aashishvanand/Weatherstation/blob/master/Weather%20Station.fzz">Fritzing project</a> to have a better idea about the connections.<br><b>FULL DISCLOSURE</b> The GPS Reciever used here is not the same as used in the real project, its for indication only, but even this should work fine, as the GPS tutorial is pretty much the same for any reciever.

<img src="https://github.com/aashishvanand/Weatherstation/blob/master/Screenshots/Weather%20Station_bb.jpg"/>

## Pre Connection Procedure
<ol>
  <li> Flash the <a href="https://www.raspberrypi.org/downloads/raspbian/">Raspbian Jessie OS</a> into the MicroSD card of your Raspberry Pi using the <a href="https://sourceforge.net/projects/win32diskimager/">Win32 Disk Imager</a> Software</li>
  <li> Insert the MicrSD card into your Rapsberry Pi </li>
  <li> Download and run <a href="http://www.putty.org/"> Putty</a>, a SSH Client.
  <li> Power up the Raspberry Pi and connect it to your router using an ethernet cable</li>
  <li> Determine the IP Address of your Raspberry pi from the router and enter that IP Address as hostname in the Hostname text field in putty</li>
  <li> Connect to the Pi using putty, even if the connection refuses once or twice, its okay, try again, it will connect. </li>
  <li> The default username is "pi" and password is "raspberry", login to your pi using these credentials </li>
  <li> Expand the file system  in Raspberry pi <code>sudo raspi-config</code> </li>
  <li> Set the time zone of the system in Raspberry pi <code>sudo raspi-config</code></li>
  <li> Run the udpate a few times <code>sudo apt-get update</code> </li>
  <li> Install the necessary softwares <code>sudo apt-get install git-core python-dev python-pip python-smbus</code> .These will come in handy later </li>
  <li> Then reboot, <code>sudo reboot</code> </li>
</ol>

## Preparing the Pi for DHT22 / DHT11
<ol>
  <li> Connect the sensor to the Pi as shown in the circuit diagram </li>
  <li> <code>git clone https://github.com/adafruit/Adafruit_Python_DHT.git</code> to clone the ADafruit DHT repository into your Pi</li>
  <li> <code>cd Adafruit_Python_DHT</code> </li>
  <li> <code>sudo apt-get install build-essential python-dev python-openssl</code> to install the necessary packages needed to install external python libraries</li>
  <li> <code>sudo python setup.py install</code> to install the external library</li>
  <li> <code>sudo ./AdafruitDHT.py 2302 4</code> to run the example and check if the sensor is working or not</li>
</ol>

## Preparing the Pi for BMP180 / BMP085
<ol>
  <li> Connect the sensor to the Pi as shown in the circuit diagram </li>
  <li> The BMP Sernsors use I2C Communication Interface to communicate with the Raspberry Pi </li>
  <code> sudo apt-get install python-smbus</code><br>
  <code> sudo apt-get install i2c-tools</code>
  <li> Run <code>sudo raspi-config</code> and follow the prompts to install i2c support for the ARM core and linux kernel</li>
  <li> Then reboot, <code>sudo reboot</code> </li>
  <li> When you are done,run <br>  <code>sudo i2cdetect -y 0</code> (if you are using a version 1 Raspberry Pi)
  <br> <code>sudo i2cdetect -y 1</code> (if you are using a version 2 Raspberry Pi)<br> Once you give this , an address should show up the output <br><br><b> Before plugging in the sensor</b><br><br><img src="https://github.com/aashishvanand/Weatherstation/blob/master/Screenshots/beforeBMP.PNG"/><br><br><b>After plugging in the sensor</b><br><br><img src="https://github.com/aashishvanand/Weatherstation/blob/master/Screenshots/afterBMP.png"/><br><b>Notice the 77 ?</b></li>
  <li> Install the Adafruit Python Library <br>
  <br> <code>sudo apt-get update</code> 
  <br> <code>sudo apt-get install git build-essential python-dev python-smbus</code> 
  <br> <code>git clone https://github.com/adafruit/Adafruit_Python_BMP.git</code> 
  <br> <code>cd Adafruit_Python_BMP</code> 
  <br> <code>sudo python setup.py install</code> </li>
  <li> Once the installation is complete <br> <code>cd examples</code> <br>
  <code>sudo python simpletest.py</code><br> To check whether or not the sensor is working </li>
</ol>

## Preparing the Pi for the GPS Reciever
<ol>
  <li> Connect the GPS antenna to the GPS Reciever</li>
  <li> Connect power to the GPS Reciever, and ensure to set it to the right power setting </li>
  <li> Esnure the GPS Reciever has a proper FIX to the satellites, different recievers indicate this in a different way. Mine has the status LED blinkng </li>
  <li> Once connected, run the following command
    <br><code> sudo nano /boot/cmdline.txt</code>
    <br> and remove <i>console=ttyAMA0,115200</i> and also if it is there remove <i>kgdboc=ttyAMA0,115200</i>
  </li>
  <li>Enter the following code, <br>
    <code> sudo systemctl stop serial-gettty@ttyAMA0.service</code><br>
    <code> sudo systemctl disable serial-gettty@ttyAMA0.service </code> <br>
    And reboot with <code> sudo reboot </code>
  </li>
  <li> Enter the code, <br>
    <code> ssty -F /dev/ttyAMA0 raw 9600 cs8 clocal -cstopb </code> <br>
    <code> cat /dev/ttyAMA0 </code>
  </li>
  <li> Upon execution of the above command you should see running lines of output, we are only bothered about the line that starts with $GPRMC , if all that you see in this line is commas, then your reciever does not have a proper fix with the satellites, try moving the antenna around, and double check your connections</li>
</ol>

## The Python Script
The python script Weather Station.py is the main script that runs in the python to send the data to the database, it recieves the data from the sensors and sends it to a php file in the server via HTTP POST, and the PhP file then sends the data to the database. Create a php code that reads data off the super global array $_POST[] and send the data to the mySQL or SQLite database. It is preferable to create a hosting account to take care of hostin your server side script. The best one I would reccommend is <a href="http://www.hostinger.in/">hostinger</a>, which has php and mySQL support by default. 
<br>
One more thing you need to do is to ensure that this code runs periodically as this code only sends data once, use <a href= "https://www.raspberrypi.org/documentation/linux/usage/cron.md">crontab</a> to automate this task. I would reccomend running this code for once in 15 or 30 minutes, any less will result in a very huge database with hardly an variation between neighbouring records. <br>
You need to modify the path in /Python/WeatherStation.py as per your server. You can run a local server in your raspberry pi and make it handle all the request or you can do it as in our case a dedicated wamp server to handle all the request.

## Android Application
Download the application <a href="https://github.com/aashishvanand/Weatherstation/raw/master/WeatherStation.apk">here</a>.
Modify its source to get the data from your server and build the apk using Android Studio. you can check out this gitlink directly into andorid studio.<br>
The Android application displays the weather information the Pi records from its sorroundings. Clicking on the location card will open up Google Maps pointing to the location of the Weather Station , this information is recieved from the GPS Module

##Php Script
As you have the option to install a wamp server in pi its really easy to connect PHP with MySQL in a pi or you can do it as in our case to make a request from the Python (Pi) to the Dedicated Wamp Server to handle the request.
You need to place the Php folder to your /etc/var/www/html/temperature/ make sure to add the database parameters according to your database db_location, db_user, db_password, db_name <br>
Php handles all the request to store all the values sent from the raspberry pi to database. It also is responsible for providing the values from the database to android application. If any Doubts in setting up a wamp server <a href="https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu">this</a> should help you.

##Database Creation
We use MySql as our primary database this could be either in the same pi that records the temperature or as in our case a dedicated server to store the records. The create table command with the fields is listed down <br> <br>
<code>create table temperature( id int(11) primary key auto_increment,temperature varchar(10), pressure varchar(10),
seapressure varchar(10), humidity varchar(10), latitude varchar(10), longitude varchar(10),
altitude varchar(10), lightintensity varchar(10), co2 varchar(10), rainfall varchar(10), time datetime);</code>
