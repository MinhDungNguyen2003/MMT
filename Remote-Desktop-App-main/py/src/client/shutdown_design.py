import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

class ShutdownDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown")
        self.setGeometry(100, 420, 280 , 70)

        self.buttonShow = QPushButton("Shutdown", self)
        self.buttonShow.setGeometry(10, 10, 120, 50)
        self.buttonShow.clicked.connect(self.onButtonShutdownClick)

        self.buttonLogout = QPushButton("Logout", self)
        self.buttonLogout.setGeometry(135, 10, 120, 50)
        self.buttonLogout.clicked.connect(self.onButtonLogoutClick)

        # self.btn_start = QPushButton("Restart", self)
        # self.btn_start.setGeometry( 20 + 2 * self.btn_view.size().width(), 10, 365 // 3, 50)
        # self.btn_start.clicked.connect(self.on_btn_restart_click)

    def onButtonShutdownClick(self):
        pass

    def onButtonLogoutClick(self):
        pass

    # def on_btn_restart_click(self):
    #     pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shutdown_app = ShutdownDesign()
    shutdown_app.show()
    sys.exit(app.exec())
