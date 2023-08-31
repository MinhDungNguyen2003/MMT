from PyQt6.QtWidgets import QMessageBox, QApplication
from killDesigner import KillDesigner
import sys
import utils
import globalVar as gv


class KillApp(KillDesigner):
    def __init__(self, isApp):
        super().__init__()
        self.isApp = isApp

    def onButtonKillClick(self):
        utils.send(gv.client, f"kill('{self.txtId.text()}', '{self.isApp}')")

        message = utils.readStr(gv.client)

        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    killApp = KillApp()
    killApp.show()
    sys.exit(app.exec())
