from shutdown_designer import ShutdownDesign
import glob_var as gv
import utils
from PyQt6.QtWidgets import QMessageBox
import sys
from PyQt6.QtWidgets import QApplication

class ShutdownApp(ShutdownDesign):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def onButtonShutdownClick(self):
        self.shutdown()

    def onButtonLogoutClick(self):
        self.logout()

    # def on_btn_restart_click(self):
    #     self.shutdown("restart()")

    def shutdown(self):
        utils.write(gv.client, "shutdown()")
        message = utils.read_str(gv.client)
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
        message = utils.read_str(gv.client)
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
    shutdown_app = ShutdownApp()
    shutdown_app.show()
    sys.exit(app.exec())
