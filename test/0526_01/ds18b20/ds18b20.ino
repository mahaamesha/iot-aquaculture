#include <LiquidCrystal_I2C.h>
#include <OneWire.h>
#include <DallasTemperature.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
OneWire wiring(6);
DallasTemperature sensor(&wiring);

void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  sensor.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor.setResolution(9);
  sensor.requestTemperatures();
  float dataSuhu = sensor.getTempCByIndex(0);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temperature");

  lcd.setCursor(0, 1);
  lcd.print(dataSuhu, 1);
  lcd.print((char)223);
  lcd.print("C");
  delay(500);
}
