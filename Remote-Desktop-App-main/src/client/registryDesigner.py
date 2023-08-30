from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QGroupBox, QComboBox, QLineEdit, QTextBrowser
import sys


class RegistryDesigner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registry")

        self.injectBox = QGroupBox("Inject Registry", self)
        self.injectBox.setGeometry(10, 10, 380, 160)

        self.browseInput = QLineEdit(self.injectBox)
        self.browseInput.setPlaceholderText("Đường dẫn ...")
        self.browseInput.setGeometry(10, 20, 280, 25)
        self.browseInput.textChanged.connect(self.onBrowseInputChange)

        self.buttonBrowse = QPushButton("Browse", self.injectBox)
        self.buttonBrowse.setGeometry(295, 20, 80, 25)
        self.buttonBrowse.clicked.connect(self.onButtonBrowseClick)

        self.registryInput = QTextEdit(self.injectBox)
        self.registryInput.setGeometry(10, 50, 280, 100)
        self.registryInput.setPlaceholderText("Nội dung")

        self.buttonInject = QPushButton("Gửi nội dung", self.injectBox)
        self.buttonInject.setGeometry(295, 50, 80, 100)
        self.buttonInject.clicked.connect(self.onButtonInjectRegistryClick)

        self.editBox = QGroupBox("Sửa giá trị trực tiếp", self)
        self.editBox.setGeometry(10, 175, 380, 250)

        self.optionApp = QComboBox(self.editBox)
        self.optionApp.setGeometry(10, 20, 360, 25)
        self.optionApp.setPlaceholderText("Chọn chức năng")
        self.optionApp.addItems(
            ["Get Value", "Set Value", "Delete Value", "Create Key", "Delete Key"])
        self.optionApp.currentIndexChanged.connect(self.onOptionAppChange)

        self.linkInput = QLineEdit(self.editBox)
        self.linkInput.setGeometry(10, 50, 360, 25)
        self.linkInput.setPlaceholderText("Đường dẫn")

        self.nameValueInput = QLineEdit(self.editBox)
        self.nameValueInput.setGeometry(10, 80, 120, 25)
        self.nameValueInput.setPlaceholderText("Value Name")

        self.valueInput = QLineEdit(self.editBox)
        self.valueInput.setGeometry(135, 80, 120, 25)
        self.valueInput.setPlaceholderText("Value")

        self.optionTypeValue = QComboBox(self.editBox)
        self.optionTypeValue.setGeometry(260, 80, 110, 25)
        self.optionTypeValue.setPlaceholderText("Kiểu dữ liệu")
        self.optionTypeValue.addItems(
            ["String", "Binary", "DWORD", "QWORD", "Multi-String", "Expandable String"])

        self.Output = QTextBrowser(self.editBox)
        self.Output.setGeometry(10, 110, 360, 100)
        self.Output.setEnabled(False)

        self.buttonInjectEdit = QPushButton("Gửi", self.editBox)
        self.buttonInjectEdit.setGeometry(15, 215, 100, 25)
        self.buttonInjectEdit.clicked.connect(self.onButtonInjectClick)

        self.buttonClear = QPushButton("Xóa", self.editBox)
        self.buttonClear.setGeometry(130, 215, 100, 25)
        self.buttonClear.clicked.connect(self.onButtonClearClick)
        self.setGeometry(510, 100, 400, 435)

    def onButtonInjectRegistryClick(self):
        pass

    def onButtonBrowseClick(self):
        pass

    def onButtonInjectClick(self):
        pass

    def onOptionAppChange(self, index):
        pass

    def onButtonClearClick(self):
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    registryApp = RegistryDesigner()
    registryApp.show()
    sys.exit(app.exec())

# Windows Registry Editor Version 5.00
# [HKEY_CURRENT_USER\\test]
# "ten"="test1"
