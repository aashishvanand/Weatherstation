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
<img src="https://raw.githubusercontent.com/aashishvanand/Flick/master/Screenshots/Screenshot_20160322-120905.png" height=480 width =270/>

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

## Preparing the Pi for BMP180
<ol>
  <li> Connect the sensor to the Pi as shown in the circuit diagram </li>
  <li> The BMP Sernsors use I2C Communication Interface to communicate with the Raspberry Pi </li>
  <code> sudo apt-get install python-smbus</code><br>
  <code> sudo apt-get install i2c-tools</code>
  <li> Run <code>sudo raspi-config</code> and follow the prompts to install i2c support for the ARM core and linux kernel</li>
  <li> Then reboot, <code>sudo reboot</code> </li>
  <li> When you are done,run <br>  <code>sudo i2cdetect -y 0</code> (if you are using a version 1 Raspberry Pi)
  <br> <code>sudo i2cdetect -y 1</code> (if you are using a version 2 Raspberry Pi)<br> Once you give this , an address should show up the output <br> Before plugging in the sensor <br><img src="https://raw.githubusercontent.com/aashishvanand/Flick/master/Screenshots/Screenshot_20160322-120905.png" height=480 width =270/> <br>After plugging in the sensor <br><img src="https://raw.githubusercontent.com/aashishvanand/Flick/master/Screenshots/Screenshot_20160322-120905.png" height=480 width =270/><br><b>Notice the 77 ?</b></li>
  <li> Install the Adafruit Python Library <br>
  <br> <code>sudo apt-get update</code> 
  <br> <code>sudo apt-get install git build-essential python-dev python-smbus</code> 
  <br> <code>git clone https://github.com/adafruit/Adafruit_Python_BMP.git</code> 
  <br> <code>cd Adafruit_Python_BMP</code> 
  <br> <code>sudo python setup.py install</code> </li>
  <li> Once the installation is complete <br> <code>cd examples</code> <br>
  <code>sudo python simpletest.py</code><br> To check whether or not the sensor is working </li>
</ol>

## Preparing the GPS Reciever
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
    <code> ssty -F /dev/ttyAMA0 raw 9600 cs8 clocal -cstopb </code>
    <code> cat /dev/ttyAMA0 </code>
  </li>
  <li> Upon execution of the above command you should see running lines of output, we are only bothered about the line that starts with $GPRMC , if all that you see in this line is commas, then your reciever does not have a proper fix with the satellites, try moving the antenna around, and double check your connections</li>
<ol>

<ol>
