import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

temp = '{0:0.2f}'.format(sensor.read_temperature())
print(temp)
pressure = '{0:0.2f}'.format(sensor.read_pressure())
print(pressure)
altitude = '{0:0.2f}'.format(sensor.read_altitude())
print(altitude)
sealevelPressure = '{0:0.2f}'.format(sensor.read_sealevel_pressure())
print(sealevelPressure)
