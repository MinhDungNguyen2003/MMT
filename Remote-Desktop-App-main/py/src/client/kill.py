from kill_design import KillDesign
import global_variables as gv
import utils
from PyQt6.QtWidgets import QMessageBox
import sys
from PyQt6.QtWidgets import QApplication

class KillApp(KillDesign):
    def __init__(self):
        super().__init__()

    def onButtonKillClick(self):
        utils.write(gv.client, f"kill('{self.txtId.text()}')")

        message = utils.read_str(gv.client)

        if "Please" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kill_app = KillApp()
    kill_app.show()
    sys.exit(app.exec())
