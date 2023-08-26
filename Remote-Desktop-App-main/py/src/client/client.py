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
        self.view_app = None

    def on_btn_connect_click(self):
        self.btn_connect.setEnabled(False)

        gv.client = QTcpSocket()
        gv.client.connectToHost(QHostAddress(self.txt_ip.text()), 5656)

        if not gv.client.waitForConnected():
            self.btn_connect.setEnabled(True)

            QMessageBox.warning(self, "Error", "Lỗi kết nối đến server")
            gv.client = None
        else:
            self.btn_connect.setEnabled(False)
            self.txt_ip.setEnabled(False)
            self.btn_connect.setText("Connected")

            QMessageBox.information(self, "Success", "Kết nối đến server thành công")

    def on_btn_quit_click(self):
        self.closeEvent(None)
        sys.exit()

    def on_btn_shutdown_click(self):
        self.open(ShutdownApp, True)

    def on_btn_app_click(self):
        self.open(ListAppApp)

    def on_btn_reg_click(self):
        self.open(RegistryApp)

    def on_btn_pic_click(self):
        self.open(PicApp)

    def on_btn_key_click(self):
        self.open(KeyloggerApp)

    def on_btn_proc_click(self):
        self.open(ListProcApp)

    def open(self, App, pass_self=False):
        if gv.client is None:
            QMessageBox.warning(self, "Error", "Chưa kết nối đến server")
            return

        self.close_app()

        if App:
            self.view_app = App(self) if pass_self else App()
            self.view_app.show()

    def close_app(self):
        if self.view_app:
            self.view_app.close()
            self.view_app = None

    def closeEvent(self, event):
        self.close_app()

        if gv.client:
            utils.write(gv.client, "quit()")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_app = ClientApp()
    client_app.show()
    sys.exit(app.exec())
