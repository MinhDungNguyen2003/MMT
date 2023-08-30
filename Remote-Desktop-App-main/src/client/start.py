from PyQt6.QtWidgets import QMessageBox, QApplication
from startDesigner import StartDesigner
import globalVar as gv
import utils
import sys


class StartApp(StartDesigner):
    def __init__(self):
        super().__init__()

    def onButtonStartClick(self):
        utils.write(gv.client, f"start('{self.idInput.text()}')")

        message = utils.readStr(gv.client)

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
