import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class ServerDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Server")
        self.setGeometry(100, 100, 400, 280)

        self.buttonOpenServer = QPushButton("Start Server", self)
        self.buttonOpenServer.setGeometry(10, 10, 130, 135)
        self.buttonOpenServer.clicked.connect(self.onButtonOpenServerClick)

    def onButtonOpenServerClick(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_app = ServerDesign()
    server_app.show()
    sys.exit(app.exec())
