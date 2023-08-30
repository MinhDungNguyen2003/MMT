from processDesigner import ProcessDesigner
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QStandardItem
from start import StartApp
from kill import KillApp
import globalVar as gv
import utils
import sys


class ProcessApp(ProcessDesigner):
    def __init__(self):
        super().__init__()
        self.viewApp = None

        self.clear()

    def onButtonShowClick(self):
        utils.write(gv.client, "showProcess()")

        self.clear(True)

        procs = utils.readAll(gv.client, utils.readInt(gv.client))
        procs = utils.parse(procs)

        for proc in procs:
            self.model.appendRow([QStandardItem(data) for data in proc])

    def onButtonKillClick(self):
        self.closeApp()
        self.viewApp = KillApp()
        self.viewApp.show()

    def onButtonStartClick(self):
        self.closeApp()
        self.viewApp = StartApp()
        self.viewApp.show()

    def onButtonClearClick(self):
        self.clear()

    def clear(self, headers=False):
        self.model.clear()

        if headers:
            self.model.setHorizontalHeaderLabels(
                ["Name Process", "ID Process", "Count Thread", "CPU (s)"])

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    processApp = ProcessApp()
    processApp.show()
    sys.exit(app.exec())
