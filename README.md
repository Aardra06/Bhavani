<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# BHAVANI🎯


## Basic Details
### Team Name: Haikyuu


### Team Members
- Team Lead: K Ananya Ramesh - School of Engineering, CUSAT
- Member 2: Aardra S V - School of Engineering, CUSAT

### Project Description
Bhavani is a desktop pet which monitors your screen and annoys you if you are being productive. As long as you use social medias such as Youtube, Instagram etc, Bhavani will be healthy and a 'diva'. The moment you stop doom scrolling and start being productive, Bhavani's health deteriorates and she starts to annoy you. In the end she becomes 'Bhavanithalla' and scolds you.

### The Problem (that doesn't exist)
People are being productive and are not doomscrolling enough. Bhavani hates productive people. Bhavani wants you to doom scroll. Don't be productive, be like Bhavani, poke your nose in other's business.

### The Solution (that nobody asked for)
Bhavani herself is the solution. Bhavani makes sure you are using your time doomscrolling instead of being productive. Dont make her turn into 'Bhavanithalla' unless you want to be scolded.

## Technical Details
### Technologies/Components Used
For Software:
- Languages: Python, Arduino IDE
- Libraries used (in Python): os, time, json, pygetwindow, serial, pygame
- Libraries used (in Arduino IDE): Wire.h, Adafruit_GFX.h, Adafruit_SSD1306.h, ESP32Servo.h, bitmaps.h
- Tools: Visual Studio Code, Arduino IDE

For Hardware:
- Main components:ESP32 Dev Module, OLED Display(128x64 px), Active buzzer, 2 Servo Motors (SG9)  
- Specifications: 1- transistor(BC547),1- 1k ohm resistor, 1- Protection Diode, Jumper wires, Perf Board
- Tools: Soldering Iron

### Implementation
For Software:
# Installation
Follow these steps to set up the software environment and configure both the Python tracking script and the ESP32 desktop companion.
### Prerequisites
* **Python 3.x** installed on your system
* **Arduino IDE** (v2.0 or later recommended)
* An **ESP32 Microcontroller** connected via USB cable

### 1. Hardware Firmware Setup (Arduino IDE)

1. **Install ESP32 Board Support:**
   * Open Arduino IDE and navigate to **File > Preferences**.
   * Add the following URL to **Additional Boards Manager URLs**:
     ```text
     [https://espressif.github.io/arduino-esp32/package_esp32_index.json](https://espressif.github.io/arduino-esp32/package_esp32_index.json)
     ```
   * Go to **Tools > Board > Boards Manager...**, search for `esp32`, and install the **esp32 by Espressif Systems** package.

2. **Required Libraries:**
   Ensure the following libraries are installed via **Tools > Manage Libraries...**:
   * `Adafruit SSD1306`
   * `Adafruit GFX Library`
   * `ESP32Servo`

3. **Upload Firmware:**
   * Open `bhavani.ino` in Arduino IDE.
   * Select your board under **Tools > Board > ESP32 Arduino** (e.g., *ESP32 Dev Module*).
   * Select the correct port under **Tools > Port**.
   * Click **Upload**.
   * 
### 2. Software Setup (Python Tracker)

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Aardra06/Bhavani.git](https://github.com/Aardra06/Bhavani.git)
   cd Bhavani
2. Install necessary python libraries: pygame pyserial pygetwindow
3. Configure COM Port; update the COM_PORT variable to match your USB serial port
# Run
 To run Bhavani, jsut connect your ESP32 to your computer via USB and launch the tracker script: python tracker.py

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
Components:
1. ESP32 Dev Module
<img width="1920" height="1920" alt="image" src="https://github.com/user-attachments/assets/cb8714ba-beac-4807-8fa2-2c4726182a35" />
<br>
2. OLED Display
   <img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/68ff7c13-9b38-4bbb-b23e-e587d91735a0" />
   <br>
3. Active Buzzer
   <img width="500" height="355" alt="image" src="https://github.com/user-attachments/assets/21e83bfa-8ce1-4c61-b961-04287dd3e699" />
   <br>
5. Servo Motors
   <img width="1200" height="900" alt="image" src="https://github.com/user-attachments/assets/2f949032-ec43-4caa-9f86-db5fe9655c65" />
   <br>

Build Process:
1. <img width="1600" height="1600" alt="image" src="https://github.com/user-attachments/assets/266e8fec-fb69-4be8-9e7a-f23cb28c7770" />
Here we have connected the OLED Display and the buzzer to the ESP32. The default expression is seen on the OLED screen.
2.<img width="1600" height="1600" alt="image" src="https://github.com/user-attachments/assets/5236f147-c6da-4732-9b0e-ecc0e975b4a5" />
Here we have arranged and soldered the components to the perf board.

Final Photo:


### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- K Ananya Ramesh: Hardware
- Aardra S V: Software
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)


