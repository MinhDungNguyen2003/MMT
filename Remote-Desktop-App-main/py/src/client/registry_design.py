import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QGroupBox, QComboBox, QLineEdit, QTextBrowser

class RegistryDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edit Registry")

        self.inject_box = QGroupBox("Inject Registry", self)
        self.inject_box.setGeometry(10, 10, 380, 160)

        self.txt_bro = QLineEdit(self.inject_box)
        self.txt_bro.setPlaceholderText("Đường dẫn ...")
        self.txt_bro.setGeometry(10, 20, 280, 25)
        self.txt_bro.textChanged.connect(self.on_txt_bro_change)

        self.btn_bro = QPushButton("Browse", self.inject_box)
        self.btn_bro.setGeometry(295, 20, 75, 25)
        self.btn_bro.clicked.connect(self.on_btn_bro_click)

        self.txt_reg = QTextEdit(self.inject_box)
        self.txt_reg.setGeometry(10, 50, 280, 100)
        self.txt_reg.setPlaceholderText("Nội dung")

        self.btn_inject = QPushButton("Gửi nội dung", self.inject_box)
        self.btn_inject.setGeometry(295, 50, 80, 100)
        self.btn_inject.clicked.connect(self.on_btn_inject_registry_click)

        self.edit_box = QGroupBox("Sửa trực tiếp", self)
        self.edit_box.setGeometry(10, 175, 380, 250)

        self.op_app = QComboBox(self.edit_box)
        self.op_app.setGeometry(10, 20, 360, 25)
        self.op_app.setPlaceholderText("Chọn chức năng")
        self.op_app.addItems(["Get Value", "Set Value", "Delete Value", "Create Key", "Delete Key"])
        self.op_app.currentIndexChanged.connect(self.on_op_app_change)

        self.txt_link = QLineEdit(self.edit_box)
        self.txt_link.setGeometry(10, 50, 360, 25)
        self.txt_link.setPlaceholderText("Đường dẫn")

        self.txt_name_value = QLineEdit(self.edit_box)
        self.txt_name_value.setGeometry(10, 80, 120 , 25)
        self.txt_name_value.setPlaceholderText("Value Name")

        self.txt_value = QLineEdit(self.edit_box)
        self.txt_value.setGeometry(135, 80, 120, 25)
        self.txt_value.setPlaceholderText("Value")

        self.op_type_value = QComboBox(self.edit_box)
        self.op_type_value.setGeometry(260, 80, 110, 25)
        self.op_type_value.setPlaceholderText("Kiểu dữ liệu")
        self.op_type_value.addItems(["String", "Binary", "DWORD", "QWORD", "Multi-String", "Expandable String"])

        self.txt_kq = QTextBrowser(self.edit_box)
        self.txt_kq.setGeometry(10, 110,360, 100)
        self.txt_kq.setEnabled(False)

        self.btn_inject_edit = QPushButton("Gửi", self.edit_box)
        self.btn_inject_edit.setGeometry(15, 215, 100, 25)
        self.btn_inject_edit.clicked.connect(self.on_btn_inject_click)

        self.btn_clear = QPushButton("Xóa", self.edit_box)
        self.btn_clear.setGeometry( 130, 215, 100, 25)
        self.btn_clear.clicked.connect(self.on_btn_clear_click)
        self.setGeometry(510, 100, 400, 435)

    def on_btn_inject_registry_click(self):
        pass

    def on_btn_bro_click(self):
        pass

    def on_btn_inject_click(self):
        pass

    def on_op_app_change(self, index):
        pass

    def on_btn_clear_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registry_app = RegistryDesign()
    registry_app.show()
    sys.exit(app.exec())
    