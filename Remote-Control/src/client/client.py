from PyQt6.QtNetwork import QTcpSocket, QHostAddress
from PyQt6.QtWidgets import QMessageBox, QApplication
from clientDesigner import ClientDesigner
import sys
import utils
import globalVar
from process import ProcessApp
from registry import RegistryApp
from listApp import ListAppApp
from keylog import KeylogApp
from pic import PicApp


class ClientApp(ClientDesigner):
    def __init__(self):
        super().__init__()
        self.viewApp = None

    def open(self, App, passSelf=False):
        if globalVar.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        self.closeApp()

        if App:
            self.viewApp = App(self) if passSelf else App()
            self.viewApp.show()

    def onButtonConnectClick(self):

        self.buttonConnect.setEnabled(False)

        globalVar.client = QTcpSocket()
        globalVar.client.connectToHost(QHostAddress(self.ipInput.text()), 5656)

        if not globalVar.client.waitForConnected():
            self.buttonConnect.setEnabled(True)

            QMessageBox.warning(self, "Error", "Lỗi kết nối đến server")
            globalVar.client = None
        else:
            self.buttonConnect.setEnabled(False)
            self.ipInput.setEnabled(False)

            QMessageBox.information(
                self, "Success", "Kết nối đến server thành công")

    def onButtonShutdownClick(self):
        if globalVar.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        utils.send(globalVar.client, "shutdown()")
        message = utils.readStr(globalVar.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            globalVar.client = None
            self.buttonConnect.setEnabled(True)
            self.ipInput.setEnabled(True)

    def onButtonLogoutClick(self):
        if globalVar.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        utils.send(globalVar.client, "logout()")
        message = utils.readStr(globalVar.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)
            globalVar.client = None
            self.buttonConnect.setEnabled(True)
            self.ipInput.setEnabled(True)

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

    def closeApp(self):
        if self.viewApp:
            self.viewApp.close()
            self.viewApp = None

    def closeEvent(self, event):
        self.closeApp()

        if globalVar.client:
            utils.send(globalVar.client, "quit()")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientApp = ClientApp()
    clientApp.show()
    sys.exit(app.exec())

    # def shutdown(self):
    #     print("shutdown")
    #     utils.send(globalVar.client, "shutdown()")
    #     message = utils.readStr(globalVar.client)
    #     if "Error" in message:
    #         QMessageBox.warning(self, "Error", message)
    #     else:
    #         QMessageBox.information(self, "Success", message)
    #         globalVar.client = None
    #         self.buttonConnect.setEnabled(True)
    #         self.ipInput.setEnabled(True)

    # def logout(self):
    #     print("logout")
    #     utils.send(globalVar.client, "logout()")
    #     message = utils.readStr(globalVar.client)
    #     if "Error" in message:
    #         QMessageBox.warning(self, "Error", message)
    #     else:
    #         QMessageBox.information(self, "Success", message)
    #         globalVar.client = None
    #         self.buttonConnect.setEnabled(True)
    #         self.ipInput.setEnabled(True)
