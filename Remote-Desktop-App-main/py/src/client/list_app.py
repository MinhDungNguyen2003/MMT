from list_app_designer import ListAppDesign
from start import StartApp
from kill import KillApp
import glob_var as gv
import utils
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys
from PyQt6.QtWidgets import QApplication

class ListAppApp(ListAppDesign):
    def __init__(self):
        super().__init__()
        self.viewApp = None

        self.clear()

    def onButtonShowClick(self):
        utils.write(gv.client, "showApp()")

        self.clear(True)

        apps = utils.read_all(gv.client, utils.read_int(gv.client))
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
            self.model.setHorizontalHeaderLabels(["Name App", "ID App", "Count Thread", "CPU (s)"])

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listapp_app = ListAppApp()
    listapp_app.show()
    sys.exit(app.exec())
