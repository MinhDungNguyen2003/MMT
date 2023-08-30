from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class ShutdownDesigner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown")
        self.setGeometry(100, 420, 280, 70)

        self.buttonShow = QPushButton("Shutdown", self)
        self.buttonShow.setGeometry(10, 10, 120, 50)
        self.buttonShow.clicked.connect(self.onButtonShutdownClick)

        self.buttonLogout = QPushButton("Logout", self)
        self.buttonLogout.setGeometry(135, 10, 120, 50)
        self.buttonLogout.clicked.connect(self.onButtonLogoutClick)

    def onButtonShutdownClick(self):
        pass

    def onButtonLogoutClick(self):
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    shutdownApp = ShutdownDesigner()
    shutdownApp.show()
    sys.exit(app.exec())
