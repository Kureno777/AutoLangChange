from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import threading
import sys

class TrayIcon:
    def __init__(self, open_settings_callback, toggle_callback, exit_callback):
        self.icon = Icon("AutoLangChange")
        self.open_settings_callback = open_settings_callback
        self.toggle_callback = toggle_callback
        self.exit_callback = exit_callback

        self.auto_mode = True

        self.icon.icon = self.create_icon()
        self.icon.title = "AutolangChange"

        self.icon.menu = Menu(
            MenuItem(
                lambda item: f"Auto Mode: {'ON' if self.auto_mode else 'OFF'}",
                self.toggle_auto_mode
            ),
            MenuItem("Open Settings", self.open_settings_callback),
            MenuItem("Exit", self.exit)
        )

    def create_icon(self):
        image = Image.new('RGB', (64, 64), color='white')
        draw = ImageDraw.Draw(image)
        draw.ellipse((16, 16, 48, 48), fill='limegreen')
        return image

    def toggle_auto_mode(self, icon, item):
        self.auto_mode = not self.auto_mode
        self.toggle_callback(self.auto_mode)
        self.icon.update_menu()  # Update label

    def exit(self, icon, item):
        self.icon.stop()
        self.exit_callback()

    def run(self):
        threading.Thread(target=self.icon.run, daemon=True).start()

