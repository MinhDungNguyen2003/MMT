from PyQt6.QtWidgets import QMessageBox, QApplication
from startDesigner import StartDesigner
import globalVar
import utils
import sys


class StartApp(StartDesigner):
    def __init__(self, isApp):
        super().__init__()
        self.isApp = isApp

    def onButtonStartClick(self):
        utils.send(
            globalVar.client, f"start('{self.idInput.text()}', '{self.isApp}')")

        message = utils.readStr(globalVar.client)

        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    startApp = StartApp()
    startApp.show()
    sys.exit(app.exec())
