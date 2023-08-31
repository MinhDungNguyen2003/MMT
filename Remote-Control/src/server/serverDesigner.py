import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit


class ServerDesigner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Server")
        self.setGeometry(100, 100, 155, 200)

        self.buttonOpenServer = QPushButton("Mở Server", self)
        self.buttonOpenServer.setGeometry(10, 10 + 40, 130, 135)
        self.buttonOpenServer.clicked.connect(self.onButtonOpenServerClick)
        self.showIP = QTextEdit("IP Address: ", self)
        self.showIP.setReadOnly(True)
        self.showIP.setGeometry(10, 10, 130, 30)

    def onButtonOpenServerClick(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    serverApp = ServerDesigner()
    serverApp.show()
    sys.exit(app.exec())
