from PyQt6.QtNetwork import QTcpSocket, QHostAddress
from PyQt6.QtWidgets import QMessageBox, QApplication
from clientDesigner import ClientDesign
import sys
import utils
import globalVar as gv
from process import ProcessApp
from registry import RegistryApp
from listApp import ListAppApp
from keylog import KeylogApp
from pic import PicApp


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

            QMessageBox.information(
                self, "Success", "Kết nối đến server thành công")

    def open(self, App, passSelf=False):
        if gv.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        self.closeApp()

        if App:
            self.viewApp = App(self) if passSelf else App()
            self.viewApp.show()

    def onButtonAppClick(self):
        self.open(ListAppApp)

    def onButtonProcessClick(self):
        self.open(ProcessApp)

    def onButtonCaptureClick(self):
        self.open(PicApp)

    def onButtonKeystrokeClick(self):
        self.open(KeylogApp)

    def onButtonRegistryClick(self):
        self.open(RegistryApp)

    def onButtonQuitClick(self):
        self.closeEvent(None)
        sys.exit()

    def onButtonShutdownClick(self):
        if gv.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return
        print("shutdown")
        self.shutdown()

    def onButtonLogoutClick(self):
        print("logout")
        if gv.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return
        self.logout()

    def shutdown(self):
        print("shutdown")
        utils.write(gv.client, "shutdown()")
        message = utils.readStr(gv.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            gv.client = None
            self.buttonConnect.setEnabled(True)
            self.ipInput.setEnabled(True)

    def logout(self):
        print("logout")
        utils.write(gv.client, "logout()")
        message = utils.readStr(gv.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            gv.client = None
            self.buttonConnect.setEnabled(True)
            self.ipInput.setEnabled(True)

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
    clientApp = ClientApp()
    clientApp.show()
    sys.exit(app.exec())
