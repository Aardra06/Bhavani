#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP32Servo.h>
#include "bitmaps.h"

// OLED Setup
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// Pin Definitions
#define BUZZER_PIN 23
#define LEFT_WING_PIN 18
#define RIGHT_WING_PIN 19

// Servo Objects
Servo leftWing;
Servo rightWing;

int currentHealth = 100;

void drawExpression(int index) {
  index = constrain(index, 0, 5);
  display.clearDisplay();
  display.drawBitmap(0, 0, expressions[index], 128, 64, SSD1306_BLACK, SSD1306_WHITE);
  display.display();
}

// Servo Wing Animations
void setWingsResting() {
  leftWing.write(0);
  rightWing.write(180);
}

void flapWingsAgitated() {
  for (int i = 0; i < 3; i++) {
    leftWing.write(60);
    rightWing.write(120);
    delay(120);
    leftWing.write(0);
    rightWing.write(180);
    delay(120);
  }
}

void triggerBuzzerDisturbance() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(100);
    digitalWrite(BUZZER_PIN, LOW);
    delay(100);
  }
}

void handleBhavaniBehavior() {
  // Map health (100 -> 0) to expression index (5 -> 0)
  int exprIndex;
  if (currentHealth == 100) {
    exprIndex = 5;
  } else {
    exprIndex = min(4, (int)((currentHealth / 100.0) * 5));
  }
  
  drawExpression(exprIndex);

  // Trigger physical disturbance when working/health is dropping below 80%
  if (currentHealth < 80) {
    triggerBuzzerDisturbance();
    flapWingsAgitated();
  } else {
    digitalWrite(BUZZER_PIN, LOW);
    setWingsResting();
  }
}

void setup() {
  Serial.begin(115200);

  // Initialize Buzzer Pin
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);

  // Attach Servo Motors
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  leftWing.setPeriodHertz(50);
  rightWing.setPeriodHertz(50);
  leftWing.attach(LEFT_WING_PIN, 500, 2400);
  rightWing.attach(RIGHT_WING_PIN, 500, 2400);
  setWingsResting();

  // Initialize OLED Screen
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    for (;;); // Loop indefinitely if OLED fails
  }

  // Display resting face (Index 5) on boot
  drawExpression(5);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    // Parse incoming serial data from Python script
    if (input.startsWith("HEALTH:")) {
      currentHealth = input.substring(7).toInt();
      handleBhavaniBehavior();
    }
  }
}