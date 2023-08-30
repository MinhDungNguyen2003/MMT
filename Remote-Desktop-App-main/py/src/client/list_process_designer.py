import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


class ListProcDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Process")
        self.setGeometry(100, 420, 400, 280)

        self.buttonKill = QPushButton("Kill", self)
        self.buttonKill.setGeometry(10, 10, 91, 50)
        self.buttonKill.clicked.connect(self.onButtonKillClick)

        self.buttonShow = QPushButton("Show", self)
        self.buttonShow.setGeometry(106, 10, 91, 50)
        self.buttonShow.clicked.connect(self.onButtonShowClick)

        self.buttonClear = QPushButton("Clear", self)
        self.buttonClear.setGeometry(202, 10, 91, 50)
        self.buttonClear.clicked.connect(self.onButtonClearClick)

        self.buttonStart = QPushButton("Start", self)
        self.buttonStart.setGeometry(298, 10, 91, 50)
        self.buttonStart.clicked.connect(self.onButtonStartClick)

        self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(["Name Process", "ID Process", "Count Thread"])
        self.tableStyle = QTableView(self)
        self.tableStyle.setModel(self.model)
        self.tableStyle.setGeometry(10, 65, 380, 205)
        self.tableStyle.verticalHeader().setVisible(False)
        self.tableStyle.setShowGrid(False)
        self.tableStyle.setFrameStyle(0)
        self.tableStyle.setAlternatingRowColors(True)
        self.tableStyle.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tableStyle.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

    def onButtonShowClick(self):
        pass

    def onButtonKillClick(self):
        pass

    def onButtonStartClick(self):
        pass

    def onButtonClearClick(self):
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listproc_app = ListProcDesign()
    listproc_app.show()
    sys.exit(app.exec())
