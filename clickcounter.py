import os
import threading
import time
from pynput import mouse
from datetime import datetime

class ClickCounter:
    def __init__(self, max_buttons=10):
        self.max_buttons = max_buttons
        self.click_counts = {button: 0 for button in range(1, max_buttons + 1)}
        self.listener = None
        self.running = False
        self.log_file = "click_counts.log"

    def on_click(self, x, y, button, pressed):
        if pressed:
            button_index = button.value
            if button_index in self.click_counts:
                self.click_counts[button_index] += 1
                with open(self.log_file, "a") as log:
                    log.write(f"{datetime.now()} - Button {button_index} Clicks: {self.click_counts[button_index]}\n")

    def start(self):
        self.running = True
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def stop(self):
        self.running = False
        self.listener.stop()

    def run(self):
        while self.running:
            time.sleep(1)

if __name__ == "__main__":
    click_counter = ClickCounter(max_buttons=5)
    click_counter.start()
