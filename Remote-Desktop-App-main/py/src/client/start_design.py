import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class StartDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start")
        self.setGeometry(
            gv.WINX + gv.WINW + gv.GL, gv.WINY + gv.WINH + 4 * gv.GL,
            gv.WINW * 2 // 3, 2 * gv.GL + gv.SS
        )

        self.buttonStart = QPushButton("Start", self)
        self.buttonStart.setGeometry(gv.WINW * 2 // 3 - gv.GL - gv.S, gv.GL, gv.S, gv.SS)
        self.buttonStart.clicked.connect(self.onButtonStartClick)

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Enter Name")
        self.idInput.setGeometry(gv.GL, gv.GL, gv.WINW * 2 // 3 - gv.G - 2 * gv.GL - gv.S, gv.SS)

    def onButtonStartClick(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_app = StartDesign()
    start_app.show()
    sys.exit(app.exec())
