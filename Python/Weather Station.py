import urllib2, urllib #The libraries needed for the POST Request
import sys # Importing the sys python package
import Adafruit_BMP.BMP085 as BMP085 #Importing the package needed for the BMP Sensor
import Adafruit_DHT #Importing the package needed for the DHT Sensor
import serial#for interfacing with GPS module as well as the Arduino via Serial
import RPi.GPIO as GPIO#for using the GPIO pins on the board      
import os, time#for delay functions
from decimal import *#for precision
GPIO.setmode(GPIO.BOARD)#for setting the gpio header
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
def getLocation():
	try:
		GPSport = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)#the port to which the gps is connected to
		ck=0
		fd=''
		while ck <= 50:
			rcv = GPSport.read(10)
		fd=fd+rcv
		ck=ck+1
		if '$GPRMC' in fd:
			ps=fd.find('$GPRMC')
			dif=len(fd)-ps
		if dif > 50:
			data=fd[ps:(ps+50)]
			p=list(find(data, ","))
			lat=data[(p[2]+1):p[3]]
			lon=data[(p[4]+1):p[5]]
			s1=lat[2:len(lat)]
			s1=Decimal(s1)
			s1=s1/60
			s11=int(lat[0:2])
			s1=s11+s1
			s2=lon[3:len(lon)]
			s2=Decimal(s2)
			s2=s2/60
			s22=int(lon[0:3])
			s2=s22+s2
			s2='{0:0.6f}'.format(s2)
			s1='{0:0.6f}'.format(s1)
		return str(s1),str(s2)
	except:
		s2="Data Unavailable"
		s1="Data Unavailable"
		return str(s1),str(s2)#latitude,longitude
def readDHT():
	#This function will take the readings from the sensor, perform a not null validation and send the data to the calling fucntion
	DHTSensor = Adafruit_DHT.DHT22 # Selecting the type of DHT Sensor
	DHTpin=4
	DHTHumidity, DHTTemp = Adafruit_DHT.read_retry(DHTSensor, DHTpin)
        DHTHumidity='{0:0.2f}'.format(DHTHumidity)
	DHTTemp='{0:0.2f}'.format(DHTTemp)
	if DHTHumidity is not None and DHTTemp is not None:
		return DHTHumidity,DHTTemp
	else:
		print('Failed to get reading from DHT22. Try again!')
		return "Data Unavailable","Data Unavailable"
def readBMP():
	#This function will tkae the readings from the sensor, perform a not null validation and send the data to the calling function
	BMPSensor = BMP085.BMP085() #Selecting the type of BMP Sensor, the sensor used in my station in BMP180 but the class is only available for BMP085, both use the same class and fucntions and connection circuit
	BMPTemp = '{0:0.2f}'.format(BMPSensor.read_temperature())
	pressure = '{0:0.2f}'.format(BMPSensor.read_pressure())
	altitude = '{0:0.2f}'.format(BMPSensor.read_altitude())
	seaLevelPressure = '{0:0.2f}'.format(BMPSensor.read_sealevel_pressure())
	if BMPTemp is not None and pressure is not None and altitude is not None and seaLevelPressure is not None:
		return BMPTemp,pressure,altitude,seaLevelPressure
	else:
		print('Failed to get reading from BMP180. Try again!')
		return "Data Unavailable","Data Unavailable"
def readArduino():
	readSerialSplit=[]
	try:
		arduinoSerial = serial.Serial('/dev/ttyACM0',9600)# The port to which the arduino is connected to.
		readSerial=arduinoSerial.readline()
		readSerialSplit=readSerial.split("*")
		return readSerialSplit
	except:
		readSerialSplit=['Data Unavailable','Data Unavailable','Data Unavailable']
		return readSerialSplit
def main():
	#DHTHumidity,DHTTemp=readDHT()
	#BMPTemp,pressure,altitude,seaLevelPressure=readBMP()
	#latitude,longitude=getLocation()
	#temperature=str(((float(DHTTemp)+float(BMPTemp)))/2)
	arduinoReading=readArduino()
	rainfall=arduinoReading[0]
	light=arduinoReading[1]
	co2=arduinoReading[2]
	print('Rainfall data from Uno '+rainfall)
	print('Light Intensity data from Uno '+light)
	print('CO2 Concentration from Uno '+co2)
	#weatherData=[('temperature',temperature),('pressure',pressure),('altitude',altitude),('seapressure',seaLevelPressure),('humidity',DHTHumidity),('latitude',latitude),('longitude',longitude),('lightintensity',light),('co2',co2),('rainfall',rainfall)]
	#weatherData=urllib.urlencode(weatherData)
	#path="http://aashish.noip.me/temperature/index.php"
	#request=urllib2.Request(path,weatherData)
	#request.add_header("Content-type","application/x-www-form-urlencoded")
	#page=urllib2.urlopen(request).read()
	#print(' A record has been succesfully updated into the Database ')
while(1):
	main()
	time.sleep(1)
