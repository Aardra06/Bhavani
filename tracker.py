import os
import time
import json
import serial
import pygetwindow as gw
import pygame

# Initialize Pygame Mixer for audio playback
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COM_PORT = "COM4"
DATA_FILE = os.path.join(BASE_DIR, "data.json")

# Expression audio mapping (Index 5 = Resting/Full Health, Index 0 = Max Anger/Low Health)
AUDIO_MAP = {
    0: os.path.join(BASE_DIR, "expression_0.mp3"),   # Very Angry
    1: os.path.join(BASE_DIR, "expression_1.mp3"),   # Angry
    2: os.path.join(BASE_DIR, "expression_2.mpeg"),  # Annoyed
    3: os.path.join(BASE_DIR, "expression_3.mpeg"),  # Neutral
    4: os.path.join(BASE_DIR, "expression_4.mpeg"),  # Happy
    5: os.path.join(BASE_DIR, "expression_5.mpeg")   # Resting / Working
}

try:
    ser = serial.Serial(COM_PORT, 115200, timeout=1)
    time.sleep(2)
    print("ESP32 Connected via USB!")
except Exception as e:
    print(f"Serial Error: {e}")
    ser = None

distraction_keywords = ["youtube", "reddit", "twitter", "x.com", "instagram", "netflix", "twitch", "gaming"]
health = 100
prev_health = 100
current_expression = -1 

def play_mood_audio(expr_index):
    """Plays mood audio and waits until the track completely finishes playing."""
    audio_path = AUDIO_MAP.get(expr_index)
    if audio_path and os.path.exists(audio_path):
        if os.path.getsize(audio_path) == 0:
            print(f"Skipping Mood {expr_index}: File size is 0 KB.")
            return

        try:
            print(f"Playing Laptop Audio for Mood Index {expr_index}: {os.path.basename(audio_path)}")
            
            # Stop any ongoing playback
            pygame.mixer.music.stop()
            
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            
            # Wait for the audio clip to finish completely
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        except Exception as err:
            print(f"Audio Playback Error on Mood {expr_index}: {err}")
    else:
        print(f"Audio file missing for Mood Index {expr_index}: {audio_path}")

while True:
    status = "Working"
    try:
        window = gw.getActiveWindow()
        if window and window.title:
            title = window.title.lower()
            
            # Check for distractions
            if any(k in title for k in distraction_keywords):
                status = "Procrastinating"
                health = min(100, health + 10)  # Health INCREASES when procrastinating
            else:
                status = "Working"
                health = max(0, health - 15)    # Health DROPS when working

        # Exact Expression Index Mapping (Health 100 -> Index 5, Health 0 -> Index 0)
        if health == 100:
            new_expression = 5
        else:
            new_expression = min(4, int((health / 100.0) * 5))

        # Check expression change
        if new_expression != current_expression:
            # Condition 1: Health is dropping (Play audio immediately)
            # Condition 2: Health is increasing AND reached full recovery (Index 5)
            if health < prev_health or (health > prev_health and new_expression == 5):
                play_mood_audio(new_expression)

            current_expression = new_expression

        prev_health = health

        # Send updated health to ESP32 over Serial
        if ser:
            ser.write(f"HEALTH:{health}\n".encode())

        # Save state to data.json
        data = {
            "health": health,
            "status": status,
            "expression": current_expression,
            "last_updated": int(time.time())
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

        print(f"Status: {status} | Health: {health}% | Mood Index: {current_expression}")

    except Exception as e:
        print(f"Tracking error: {e}")

    # Standard loop interval between health checks
    time.sleep(5)