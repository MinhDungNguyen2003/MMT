from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys


class KillDesigner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kill")
        self.setGeometry(510, 420, 266, 45)

        self.buttonKill = QPushButton("Kill", self)
        self.buttonKill.setGeometry(181, 10, 75, 25)
        self.buttonKill.clicked.connect(self.onButtonKillClick)

        self.txtId = QLineEdit(self)
        self.txtId.setPlaceholderText("Nhập ID")
        self.txtId.setGeometry(10, 10, 166, 25)

    def onButtonKillClick(self):
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    killApp = KillDesigner()
    killApp.show()
    sys.exit(app.exec())
