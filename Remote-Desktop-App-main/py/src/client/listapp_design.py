import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class ListAppDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Application")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WINW, gv.WINH)

        self.buttonShow = QPushButton("Show", self)
        self.buttonShow.setGeometry(gv.GL, gv.GL, (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS)
        self.buttonShow.clicked.connect(self.onButtonShowClick)

        self.buttonKill = QPushButton("Kill", self)
        self.buttonKill.setGeometry(
            gv.GL + gv.G + self.buttonShow.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.buttonKill.clicked.connect(self.onButtonKillClick)

        self.buttonStart = QPushButton("Start", self)
        self.buttonStart.setGeometry(
            gv.GL + 2 * gv.G + 2 * self.buttonShow.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.buttonStart.clicked.connect(self.onButtonStartClick)

        self.buttonClear = QPushButton("Clear", self)
        self.buttonClear.setGeometry(
            gv.GL + 3 * gv.G + 3 * self.buttonShow.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.buttonClear.clicked.connect(self.onButtonClearClick)

        self.model = QStandardItemModel()
        self.tableStyle = QTableView(self)
        self.tableStyle.setModel(self.model)
        self.tableStyle.setGeometry(
            gv.GL, gv.GL + gv.G + 2 * gv.SS,
            gv.WINW - 2 * gv.GL, gv.WINH - (2 * gv.GL + gv.G + 2 * gv.SS)
        )
        self.tableStyle.verticalHeader().setVisible(False)
        self.tableStyle.setShowGrid(False)
        self.tableStyle.setFrameStyle(0)
        self.tableStyle.setAlternatingRowColors(True)
        self.tableStyle.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tableStyle.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

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
    listapp_app = ListAppDesign()
    listapp_app.show()
    sys.exit(app.exec())
