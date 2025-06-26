import keyboard
import threading

class TypingHook:
    def __init__(self, on_word_callback):
        self.buffer = ""
        self.on_word_callback = on_word_callback
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._hook_loop, daemon=True).start()

    def _hook_loop(self):
        keyboard.on_press(self._on_key_event)

    def _on_key_event(self, e):
        if not self.running:
            return

        key = e.name

        if key in ['space', 'enter', 'tab']:
            if self.buffer:
                self.on_word_callback(self.buffer, key)
                self.buffer = ""
        elif key == 'backspace':
            self.buffer = self.buffer[:-1]
        elif len(key) == 1:
            self.buffer += key

