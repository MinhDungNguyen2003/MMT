import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class KillDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kill")
        self.setGeometry(
            gv.WINX + gv.WINW + gv.GL, gv.WINY + gv.WINH + 4 * gv.GL,
            gv.WINW * 2 // 3, 2 * gv.GL + gv.SS
        )

        self.buttonKill = QPushButton("Kill", self)
        self.buttonKill.setGeometry(gv.WINW * 2 // 3 - gv.GL - gv.S, gv.GL, gv.S, gv.SS)
        self.buttonKill.clicked.connect(self.onButtonKillClick)

        self.txtId = QLineEdit(self)
        self.txtId.setPlaceholderText("Nhập ID")
        self.txtId.setGeometry(gv.GL, gv.GL, gv.WINW * 2 // 3 - gv.G - 2 * gv.GL - gv.S, gv.SS)

    def onButtonKillClick(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kill_app = KillDesign()
    kill_app.show()
    sys.exit(app.exec())
