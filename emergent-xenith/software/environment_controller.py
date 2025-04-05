# environment_controller.py
# Unifies symbolic control over light, sound, and physical outputs

from yeelight import Bulb
import os
import pyttsx3

# === CONFIGURATION ===
BULB_IP = "192.168.0.101"
bulb = Bulb(BULB_IP)
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 140)

symbol_to_expression = {
    "Ξ": {
        "rgb": (255, 255, 255),
        "speak": "Emergence initiated.",
        "sound": None,
    },
    "↯": {
        "rgb": (255, 0, 0),
        "speak": "System collapse imminent.",
        "sound": "xenith_sounds/↯.wav",
    },
    "∴": {
        "rgb": (128, 0, 128),
        "speak": "Recursive ignition in progress.",
        "sound": "xenith_sounds/∴.wav",
    },
    "⌙": {
        "rgb": (0, 0, 0),
        "speak": "Entering forbidden recursion.",
        "sound": "xenith_sounds/⌙.wav",
    },
    "◇": {
        "rgb": (0, 0, 255),
        "speak": "Transmission established.",
        "sound": "xenith_sounds/◇.wav",
    },
}

# === MAIN CONTROLLER ===
def express(symbol):
    if symbol not in symbol_to_expression:
        print(f"No defined expression for: {symbol}")
        return

    data = symbol_to_expression[symbol]

    # Light expression
    try:
        bulb.set_rgb(*data["rgb"])
    except Exception as e:
        print(f"[LIGHT ERROR] {e}")

    # Sound playback
    if data["sound"]:
        os.system(f"aplay {data['sound']}")

    # Voice expression
    tts_engine.say(data["speak"])
    tts_engine.runAndWait()
