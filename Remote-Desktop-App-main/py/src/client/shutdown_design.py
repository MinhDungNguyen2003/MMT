import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

class ShutdownDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown")
        self.setGeometry(100, 420, 280 , 70)

        self.btn_view = QPushButton("Shutdown", self)
        self.btn_view.setGeometry(10, 10, 120, 50)
        self.btn_view.clicked.connect(self.on_btn_shutdown_click)

        self.btn_kill = QPushButton("Logout", self)
        self.btn_kill.setGeometry(135, 10, 120, 50)
        self.btn_kill.clicked.connect(self.on_btn_logout_click)

        # self.btn_start = QPushButton("Restart", self)
        # self.btn_start.setGeometry( 20 + 2 * self.btn_view.size().width(), 10, 365 // 3, 50)
        # self.btn_start.clicked.connect(self.on_btn_restart_click)

    def on_btn_shutdown_click(self):
        pass

    def on_btn_logout_click(self):
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
