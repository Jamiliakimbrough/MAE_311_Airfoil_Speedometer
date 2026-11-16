#include "HX711.h"
// Pin definitions
int LOADCELL_DOUT_PIN = 3;
int LOADCELL_SCK_PIN = 2;

int b = 0.457;
int a = 0.305;


int rho = 1.222;
int c_l = 0.4;

int factor = (c_l*rho*a*b);
HX711 scale;
 
void setup() {
  Serial.begin(9600);
  Serial.println("HX711 Demo");

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

  delay(1000);
  scale.tare();
  scale.set_scale(505.f);
 

  Serial.println("Scale tared. Place weight on the load cell.");
}

void loop() {
  // Read weight in units (grams)
  if (scale.is_ready()) {
    float reading = scale.get_units(20);
    float speed = sqrt((reading*0.002)/factor)/2.237;// average of 10 readings
    Serial.print("Speed: ");
    Serial.print(reading);
    Serial.println(" m/s");
  } else {
    Serial.println("HX711 not found.");
  }
  delay(500);
}