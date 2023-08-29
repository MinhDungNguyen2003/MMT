from listproc_design import ListProcDesign
from start import StartApp
from kill import KillApp
import global_variables as gv
import utils
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys
from PyQt6.QtWidgets import QApplication

class ListProcApp(ListProcDesign):
    def __init__(self):
        super().__init__()
        self.viewApp = None

        self.clear()

    def onButtonShowClick(self):
        utils.write(gv.client, "show_proc()")

        self.clear(True)

        procs = utils.read_all(gv.client, utils.read_int(gv.client))
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
            self.model.setHorizontalHeaderLabels(["Name Process", "ID Process", "Count Thread", "CPU (s)"])

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listproc_app = ListProcApp()
    listproc_app.show()
    sys.exit(app.exec())
