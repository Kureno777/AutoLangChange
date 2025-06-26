import sys
import pyautogui
import keyboard
import time
from PyQt5.QtWidgets import QApplication
from Keymap import convert_word
from gui.settings_window import SettingsWindow
from gui.tray import TrayIcon
from core.hook import TypingHook
from core.dictionary import DictionaryChecker
dictionary = DictionaryChecker()


def toggle_auto_mode(state):
    print("Auto Mode is now:", "ON" if state else "OFF")

def open_settings(icon=None, item=None):
    window.show()

def exit_app():
    print("Exiting RightLang2...")
    app.quit()

app = QApplication(sys.argv)

window = SettingsWindow()
tray = TrayIcon(open_settings_callback=open_settings,
                toggle_callback=toggle_auto_mode,
                exit_callback=exit_app)

tray.run()
window.show()

from core.hook import TypingHook

def handle_word(word, end_key):
    word = word.strip()

    # STEP 1: Check if the original word is valid
    if dictionary.is_valid_word(word):
        print(f"[Valid Word] → {word} ✅")
        return  # Do nothing

    # STEP 2: Try convert layout
    converted = convert_word(word)

    # STEP 3: Check if converted is valid
    if dictionary.is_valid_word(converted):
        print(f"[Hooked Word] → {word}")
        print(f"[Converted   ] → {converted}")

        time.sleep(0.05)

        # Delete old word + space
        for _ in range(len(word) + 1):
            keyboard.send('backspace')
            time.sleep(0.005)

        # Type the corrected word
        keyboard.write(converted, delay=0.01)

        # Restore the ending key (space/enter/tab)
        if end_key == 'space':
            keyboard.send('space')
        elif end_key == 'enter':
            keyboard.send('enter')
        elif end_key == 'tab':
            keyboard.send('tab')
    else:
        print(f"[Unknown Word] → {word} ❌ no correction")


hook = TypingHook(handle_word)
hook.start()

sys.exit(app.exec_())

