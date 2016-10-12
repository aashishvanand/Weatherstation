//Including the nescessary header file
#include<MQ135.h>
//Indicating the pins for the sensors
int rainSensorPin=A0;
int lightSensorPin=A1;
int co2SensorPin=A2;
//Loading the sensor requried from the library
MQ135 gasSensor = MQ135(co2SensorPin);
//Setup the board
void setup() {
  Serial.begin(9600);// initialize serial communication @ 9600 baud:  
  pinMode(rainSensorPin,INPUT);
  pinMode(lightSensorPin,INPUT);
  pinMode(co2SensorPin,INPUT);
}
//Returns the rainfall status.
String getRainfall(){
  int rainSensorReading = analogRead(rainSensorPin);// read the sensor on analog A0:
  //return (String(rainSensorReading));
  if(rainSensorReading>=0&&rainSensorReading<=200){
    return("Drenching Rain"); 
  }else if(rainSensorReading>=200 && rainSensorReading<1010){
    return("Raining");
  }else if(rainSensorReading>=1010){
    return("No Rain");
  }
}
//Returns the light intensity in LUX
/*
 *---------------------------------------------------------------------------------
 *Illuminance                  Surfaces illuminated by:
 *---------------------------------------------------------------------------------
  0.0001 lux                   Moonless, overcast night sky (starlight)[3]
  0.002 lux                    Moonless clear night sky with airglow[3]
  0.27–1.0 lux                 Full moon on a clear night[3][4]
  3.4                          lux Dark limit of civil twilight under a clear sky[5]
  50 lux                       Family living room lights (Australia, 1998)[6]
  80 lux                       Office building hallway/toilet lighting[7][8]
  100 lux                      Very dark overcast day[3]
  320–500                      lux Office lighting[6][9][10][11]
  400 lux                      Sunrise or sunset on a clear day.
  1000 lux                     Overcast day;[3] typical TV studio lighting
  10000–25000                  lux Full daylight (not direct sun)[3]
  32000–100000 lux             Direct sunlight
  *----------------------------------------------------------------------------------
 */
String getLight (){
  int RawA1=analogRead(lightSensorPin); //read the sensor on analog A1
  double Vout=RawA1*0.0048828125;// convert the sensor reading to voltage
  int lux=(2500/Vout-500)/10;// convert the voltage to LUX (light intensity in its SI unit)
  return String(lux); //return the light intensity to calling function.
}
//Returns the Co2 Concentration in PPM
String getCo2Concentration(){
  float co2Concentration = gasSensor.getPPM();
  return(String(co2Concentration));
}
//Main function that is done foreveer
void loop() {
  String rainFall=getRainfall();
  String light=getLight();
  String co2Concentration=getCo2Concentration();
  String outputToSerial=rainFall+"*"+light+"*"+co2Concentration;
  Serial.println(outputToSerial);
  //Below are debugging statements, remove when deploying...
  /*Serial.print("Rainfall: ");
  Serial.println(rainFall);
  Serial.print("Light Intensity: ");
  Serial.println(light);
  Serial.print("CO2 Concentration: ");
  Serial.println(co2Concentration);*/
  delay(1000);  // delay between reads
}


