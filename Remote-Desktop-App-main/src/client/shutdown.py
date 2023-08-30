from PyQt6.QtWidgets import QMessageBox, QApplication
from shutdownDesigner import ShutdownDesigner
import globalVar as gv
import utils
import sys


class ShutdownApp(ShutdownDesigner):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def onButtonShutdownClick(self):
        self.shutdown()

    def onButtonLogoutClick(self):
        self.logout()

    def shutdown(self):
        utils.write(gv.client, "shutdown()")
        message = utils.readStr(gv.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            gv.client = None
            self.parent.closeApp()
            self.parent.buttonConnect.setEnabled(True)
            self.parent.ipInput.setEnabled(True)
            self.parent.buttonConnect.setText("Connect")

    def logout(self):
        utils.write(gv.client, "logout()")
        message = utils.readStr(gv.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            gv.client = None
            self.parent.closeApp()
            self.parent.buttonConnect.setEnabled(True)
            self.parent.ipInput.setEnabled(True)
            self.parent.buttonConnect.setText("Connect")

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    shutdownApp = ShutdownApp()
    shutdownApp.show()
    sys.exit(app.exec())
