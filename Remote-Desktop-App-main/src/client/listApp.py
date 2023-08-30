from listAppDesigner import ListAppDesigner
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QStandardItem
from kill import KillApp
from start import StartApp
import utils
import sys
import globalVar as gv


class ListAppApp(ListAppDesigner):
    def __init__(self):
        super().__init__()
        self.viewApp = None

        self.clear()

    def onButtonShowClick(self):
        utils.send(gv.client, "showApp()")

        self.clear(True)

        apps = utils.readAll(gv.client, utils.readInt(gv.client))
        apps = utils.parse(apps)

        for app in apps:
            self.model.appendRow([QStandardItem(data) for data in app])

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
                ["Name App", "ID App", "Count Thread", "CPU (s)"])

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listappApp = ListAppApp()
    listappApp.show()
    sys.exit(app.exec())
