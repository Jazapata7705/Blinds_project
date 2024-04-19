/*
   Gamepad module provides three different mode namely Digital, JoyStick and Accerleometer.

   You can reduce the size of library compiled by enabling only those modules that you want to
   use. For this first define CUSTOM_SETTINGS followed by defining INCLUDE_modulename.

   Explore more on: https://thestempedia.com/docs/dabble/game-pad-module/
*/
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

int motor1pin1 = 4;
int motor1pin2 = 5;
int resistor_pin = 6;
int enA = 10;

#include <Dabble.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);


void setup() {
  // put your setup code here, to run once:
  const int ledPin = 13;
  pinMode(ledPin,OUTPUT);
  pinMode(motor1pin1,OUTPUT);
  pinMode(motor1pin2,OUTPUT);
  pinMode(enA, OUTPUT);

  lcd.init();
  lcd.clear();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Light Intensity:");

  Serial.begin(250000);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin(9600);      //Enter baudrate of your bluetooth.Connect bluetooth on Bluetooth port present on evive.
}

void sense_light(){
  
  
  lcd.setCursor(0,1);
  pinMode(resistor_pin,OUTPUT);
  digitalWrite(resistor_pin,LOW);
  delay(100);

  pinMode(resistor_pin,INPUT);
  float current_time = millis();
  float difference = 0;

  while(digitalRead(resistor_pin) == LOW){
    difference = millis() - current_time;
  }
  Serial.print(difference);
  Serial.print(" ");

  if (difference < 280){
    lcd.setCursor(0,1);
    lcd.print("Light");
  }
  else if(difference > 280 and difference < 600){
    lcd.setCursor(0,1);
    lcd.print("Dim  ");
  }else if(difference > 600){
    lcd.setCursor(0,1);
    lcd.print("Dark  ");
  
  }

  delay(1000);
  //lcd.print("Light");
  //lcd.print("Dark");

}



void loop() {
  

  Dabble.processInput();     //this function is used to refresh data obtained from smartphone.Hence calling this function is mandatory in order to get data properly from your mobile.
  const int ledPin = 13;
  pinMode(ledPin,OUTPUT);    
  

  Serial.print("KeyPressed: ");
  
//-------------Manual up and down----------------------------------
  if (GamePad.isLeftPressed())
  {
    Serial.print("Left");
    digitalWrite(motor1pin1,HIGH);
    digitalWrite(motor1pin2,LOW);
    analogWrite(enA,150);
  }
  if (GamePad.isRightPressed())
  {
    Serial.print("Right");
    digitalWrite(motor1pin1,LOW);
    digitalWrite(motor1pin2,HIGH);
    analogWrite(enA,150);
  }
  if (GamePad.isRightPressed()== false and GamePad.isLeftPressed()== false)
  {
    analogWrite(enA,0);
    digitalWrite(motor1pin1,LOW);
    digitalWrite(motor1pin2,LOW);
    
  }
//-------------Automatic/ Light sensor mode-------------------------------------------
  if (GamePad.isSquarePressed())
  {
    Serial.print("Square");
    sense_light();
  }

  if (GamePad.isStartPressed())
  {
    Serial.print("Start");
  }

  Serial.print('\t');
  Serial.println();
}