from start_designer import StartDesign
import glob_var as gv
import utils
from PyQt6.QtWidgets import QMessageBox
import sys
from PyQt6.QtWidgets import QApplication

class StartApp(StartDesign):
    def __init__(self):
        super().__init__()

    def onButtonStartClick(self):
        utils.write(gv.client, f"start('{self.idInput.text()}')")

        message = utils.read_str(gv.client)

        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_app = StartApp()
    start_app.show()
    sys.exit(app.exec())
