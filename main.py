from PyQt5.QtWidgets import QApplication
import sys
from gui.settings_window import SettingsWindow
from gui.tray import TrayIcon

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

def handle_word(word):
    print(f"[Hooked Word] → {word}")

hook = TypingHook(handle_word)
hook.start()

sys.exit(app.exec_())

