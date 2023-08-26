import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class KeyloggerDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keystroke")
        self.setGeometry(0, 0, 347, 271)

        self.txt_result = QTextEdit(self)
        self.txt_result.setEnabled(False)
        self.txt_result.setGeometry(12, 77, 318, 182)

        button_width = 75
        button_height = 59

        self.btn_hook = QPushButton("Hook", self)
        self.btn_hook.setGeometry(12, 12, button_width, button_height)
        self.btn_hook.clicked.connect(self.on_btn_hook_click)

        self.btn_unhook = QPushButton("Unhook", self)
        self.btn_unhook.setGeometry(93, 13, button_width, button_height)
        self.btn_unhook.clicked.connect(self.on_btn_unhook_click)

        self.btn_print_key = QPushButton("In phím", self)
        self.btn_print_key.setGeometry(174, 12, button_width, button_height)
        self.btn_print_key.clicked.connect(self.on_btn_print_key_click)

        self.btn_clear = QPushButton("Xóa", self)
        self.btn_clear.setGeometry(256, 13, button_width, button_height)
        self.btn_clear.clicked.connect(self.on_btn_clear_click)

    def on_btn_hook_click(self):
        pass

    def on_btn_unhook_click(self):
        pass

    def on_btn_print_key_click(self):
        pass

    def on_btn_clear_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerDesign()
    keylogger_app.show()
    sys.exit(app.exec())
