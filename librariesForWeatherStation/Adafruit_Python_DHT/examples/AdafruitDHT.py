import sys
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 4 
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print(str(temperature)+'\n'+str(humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
