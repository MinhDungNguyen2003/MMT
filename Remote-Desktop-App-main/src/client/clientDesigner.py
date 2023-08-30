import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel


class ClientDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client")
        self.setGeometry(100, 100, 372, 350)

        self.ipInput = QLineEdit(self)
        self.ipInput.setPlaceholderText("Nhập IP")
        self.ipInput.setGeometry(12, 29, 226, 20)

        self.buttonConnect = QPushButton("Kết nối", self)
        self.buttonConnect.setGeometry(244, 27, 100, 23)
        self.buttonConnect.clicked.connect(self.onButtonConnectClick)

        self.buttonApp = QPushButton("App Running ", self)
        self.buttonApp.setGeometry(93, 64, 145, 63)
        self.buttonApp.clicked.connect(self.onButtonAppClick)

        self.buttonProcess = QPushButton("Process\n Running", self)
        self.buttonProcess.setGeometry(12, 64, 75, 197)
        self.buttonProcess.clicked.connect(self.onButtonProcessClick)

        self.buttonKeystroke = QPushButton("Keystroke", self)
        self.buttonKeystroke.setGeometry(244, 64, 100, 126)
        self.buttonKeystroke.clicked.connect(self.onButtonKeystrokeClick)

        self.buttonCapture = QPushButton("Chụp màn hình", self)
        self.buttonCapture.setGeometry(93, 133, 145, 57)
        self.buttonCapture.clicked.connect(self.onButtonCaptureClick)

        self.buttonShutdown = QPushButton("Tắt máy", self)
        self.buttonShutdown.setGeometry(12, 200 + 66, 163, 57)
        self.buttonShutdown.clicked.connect(self.onButtonShutdownClick)

        self.buttonLogout = QPushButton("Logout", self)
        self.buttonLogout.setGeometry(163 + 18, 200 + 66, 163, 57)
        self.buttonLogout.clicked.connect(self.onButtonLogoutClick)

        self.buttonQuit = QPushButton("Thoát", self)
        self.buttonQuit.setGeometry(297, 196, 47, 65)
        self.buttonQuit.clicked.connect(self.onButtonQuitClick)

        self.buttonRegistry = QPushButton("Sửa Registry", self)
        self.buttonRegistry.setGeometry(93, 196, 198, 65)
        self.buttonRegistry.clicked.connect(self.onButtonRegistryClick)

    def onButtonConnectClick(self):
        pass

    def onButtonAppClick(self):
        pass

    def onButtonProcessClick(self):
        pass

    def onButtonCaptureClick(self):
        pass

    def onButtonKeystrokeClick(self):
        pass

    def onButtonRegistryClick(self):
        pass

    def onButtonQuitClick(self):
        pass

    def closeEvent(self, event):
        pass

    def onButtonShutdownClick(self):
        pass

    def onButtonLogoutClick(self):
        pass

    def shutdown(self):
        pass

    def logout(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientApp = ClientDesign()
    clientApp.show()
    # clientApp.applyButtonStyle(clientApp.buttonConnect)
    # clientApp.applyButtonStyle(clientApp.buttonApp)
    sys.exit(app.exec())
