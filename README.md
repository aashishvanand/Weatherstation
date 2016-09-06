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


  
