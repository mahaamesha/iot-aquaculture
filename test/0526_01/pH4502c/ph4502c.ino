// Program Sensor pH-meter ; PH-4502C
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
/*
int pH = A0;
int buf[10], temp;

float PH(float voltage) {
  return 7 + ((12.5 - voltage) / 0.18);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pH, INPUT);

  lcd.init();
  lcd.backlight();
  delay(1000);
  lcd.clear();
}

void loop() {
  lcd.clear();

  for(int i=0;i<10;i++){
    buf[i]=analogRead(pH);
    delay(10);
  }

  float avgValue = 0;
  for(int i=0;i<10;i++)
  avgValue += buf[i];

  //float pHVol = (float)avgValue*5.0/1024/10;
  float pHVol = (float)avgValue*5/1024/10;
  float pHValue = -5.70 * pHVol + 21.34;

  lcd.setCursor(0,0);
  lcd.print("pHValue = ");
  lcd.print(pHValue);
  delay(1000);

  Serial.print("sensor = ");
  Serial.println(PH(pHVol));
  Serial.println(pHValue);

  delay(1000);
}
*/

int pHSense = A0;
int samples = 10;
float adc_resolution = 1024.0;


  float pH(float voltage){
    return 16.15 + ((2.5 - voltage)/0.18);
  }

void setup(){
  Serial.begin(9600);
  pinMode(pHSense, INPUT);

  lcd.init();
  lcd.backlight();
  delay(1000);
  lcd.clear();
}

void loop(){
  lcd.clear();
  
  int measuring = 0;

  for(int i=0;i<samples;i++){
    measuring += analogRead(pHSense);
    delay(10);
  }

  float voltage = 5/adc_resolution*measuring/samples;

  lcd.setCursor(0,0);
  lcd.print("pHValue = ");
  lcd.print(pH(voltage));
  delay(1000);
  
  Serial.print("pH = ");
  Serial.println(pH(voltage));
  delay(3000);
}
