import sys, utils
from client_design import ClientDesign
from listproc import ListProcApp
from listapp import ListAppApp
from registry import RegistryApp
from pic import PicApp
from keylogger import KeyloggerApp
from shutdown import ShutdownApp
import global_variables as gv
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtNetwork import QTcpSocket, QHostAddress
from PyQt6.QtWidgets import QApplication

class ClientApp(ClientDesign):
    def __init__(self):
        super().__init__()
        self.viewApp = None

    def onButtonConnectClick(self):
        self.buttonConnect.setEnabled(False)

        gv.client = QTcpSocket()
        gv.client.connectToHost(QHostAddress(self.ipInput.text()), 5656)

        if not gv.client.waitForConnected():
            self.buttonConnect.setEnabled(True)

            QMessageBox.warning(self, "Error", "Lỗi kết nối đến server")
            gv.client = None
        else:
            self.buttonConnect.setEnabled(False)
            self.ipInput.setEnabled(False)
            self.buttonConnect.setText("Connected")

            QMessageBox.information(self, "Success", "Kết nối đến server thành công")

    def onButtonQuitClick(self):
        self.closeEvent(None)
        sys.exit()

    def onButtonShutdownClick(self):
        self.open(ShutdownApp, True)

    def onButtonAppClick(self):
        self.open(ListAppApp)

    def onButtonRegistryClick(self):
        self.open(RegistryApp)

    def onButtonCaptureClick(self):
        self.open(PicApp)

    def onButtonKeystrokeClick(self):
        self.open(KeyloggerApp)

    def onButtonProcessClick(self):
        self.open(ListProcApp)

    def open(self, App, pass_self=False):
        if gv.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        self.closeApp()

        if App:
            self.viewApp = App(self) if pass_self else App()
            self.viewApp.show()

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()

        if gv.client:
            utils.write(gv.client, "quit()")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_app = ClientApp()
    client_app.show()
    sys.exit(app.exec())
