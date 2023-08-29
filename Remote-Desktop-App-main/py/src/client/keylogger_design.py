import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class KeyloggerDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keystroke")
        self.setGeometry(0, 0, 347, 271)

        self.txtOutput = QTextEdit(self)
        self.txtOutput.setEnabled(False)
        self.txtOutput.setGeometry(12, 77, 318, 182)

        buttonWidth = 75
        buttonHeight = 59

        self.buttonHook = QPushButton("Hook", self)
        self.buttonHook.setGeometry(12, 12, buttonWidth, buttonHeight)
        self.buttonHook.clicked.connect(self.onButtonHookClick)

        self.buttonUnhook = QPushButton("Unhook", self)
        self.buttonUnhook.setGeometry(93, 13, buttonWidth, buttonHeight)
        self.buttonUnhook.clicked.connect(self.onButtonUnhookClick)

        self.buttonPrintKey = QPushButton("In phím", self)
        self.buttonPrintKey.setGeometry(174, 12, buttonWidth, buttonHeight)
        self.buttonPrintKey.clicked.connect(self.onButtonPrintKeyClick)

        self.buttonClear = QPushButton("Xóa", self)
        self.buttonClear.setGeometry(256, 13, buttonWidth, buttonHeight)
        self.buttonClear.clicked.connect(self.onButtonClearClick)

    def onButtonHookClick(self):
        pass

    def onButtonUnhookClick(self):
        pass

    def onButtonPrintKeyClick(self):
        pass

    def onButtonClearClick(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerDesign()
    keylogger_app.show()
    sys.exit(app.exec())
