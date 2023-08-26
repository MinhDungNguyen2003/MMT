import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel

class ClientDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client")
        self.setGeometry(100, 100, 372, 302)

        self.txt_ip = QLineEdit(self)
        self.txt_ip.setPlaceholderText("Nhập IP")
        # self.txt_ip.setText("Nhập IP")
        self.txt_ip.setGeometry(12, 29, 226, 20)

        self.btn_connect = QPushButton("Kết nối", self)
        self.btn_connect.setGeometry(244, 27, 100, 23)
        self.btn_connect.clicked.connect(self.on_btn_connect_click)

        self.btn_proc = QPushButton("Process\n Running", self)
        self.btn_proc.setGeometry(12, 64, 75, 197)
        self.btn_proc.clicked.connect(self.on_btn_proc_click)

        self.btn_app = QPushButton("App Running ", self)
        self.btn_app.setGeometry(93, 64, 145, 63)
        self.btn_app.clicked.connect(self.on_btn_app_click)

        self.btn_key = QPushButton("Keystroke", self)
        self.btn_key.setGeometry(244, 64, 100, 126)
        self.btn_key.clicked.connect(self.on_btn_key_click)

        self.btn_shutdown = QPushButton("Tắt\nmáy", self)
        self.btn_shutdown.setGeometry(93, 133, 48, 57)
        self.btn_shutdown.clicked.connect(self.on_btn_shutdown_click)

        self.btn_pic = QPushButton("Chụp màn hình", self)
        self.btn_pic.setGeometry(147, 133, 91, 57)
        self.btn_pic.clicked.connect(self.on_btn_pic_click)

        self.btn_quit = QPushButton("Thoát", self)
        self.btn_quit.setGeometry(297, 196, 47, 65)
        self.btn_quit.clicked.connect(self.on_btn_quit_click)

        self.btn_reg = QPushButton("Sửa Registry", self)
        self.btn_reg.setGeometry(93, 196, 198, 65)
        self.btn_reg.clicked.connect(self.on_btn_reg_click)

    def on_btn_app_click(self):
        pass

    def on_btn_connect_click(self):
        pass

    def on_btn_shutdown_click(self):
        pass

    def on_btn_reg_click(self):
        pass

    def on_btn_quit_click(self):
        pass

    def on_btn_pic_click(self):
        pass

    def on_btn_key_click(self):
        pass

    def on_btn_proc_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_app = ClientDesign()
    client_app.show()
    sys.exit(app.exec())
