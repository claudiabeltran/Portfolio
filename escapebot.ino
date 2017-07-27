
#include <Servo.h>                           // Include servo library

int pushButton = 2;

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

void setup() {
  // put your setup code here, to run once:
//  servoLeft.attach(13);                      // Attach left signal to pin 13
//  servoRight.attach(12);    // Attach left signal to pin 12
  Serial.begin(9600);
  pinMode(pushButton, INPUT);
}


void stayStill (int times){
  servoLeft.detach();
  servoRight.detach();
  delay(times);
  servoLeft.attach(13);
  servoRight.attach(12);
}
void moveForward (int times){
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(0);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);
  delay(times);
}
void moveBackward (int times){
  servoLeft.writeMicroseconds(0);
  servoRight.writeMicroseconds(2000);
  servoLeft.attach(13);                     
  servoRight.attach(12);
  delay (times);
}
void turnRight (int degree){
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);
  delay ((1100/180) * degree);
}
void turnLeft (int degree){
  servoLeft.writeMicroseconds(0);
  servoRight.writeMicroseconds(0);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);
  delay ((1100/180) * degree);
}

void loop() {
  int buttonState = digitalRead(pushButton);
  Serial.println(buttonState);
  if (buttonState == 1) {
   stayStill(1000);
   turnRight(360);
   turnLeft(360);
   moveBackward(1000);
   moveForward(1000);
   servoLeft.detach();
   servoRight.detach();
  }
}

