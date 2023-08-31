from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import os
import sys
from PyQt6.QtGui import QPixmap


class PicDesigner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Take Screenshots")
        self.setGeometry(100, 420, 588, 280)

        self.pictureLabel = QLabel(self)
        self.pictureLabel.setGeometry(10, 10, 470, 260)
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setPixmap(QPixmap(os.getcwd() + "/pic.png"))

        self.buttonTake = QPushButton("Take\nScreenshot", self)
        self.buttonTake.setGeometry(503, 10, 75, 150)
        self.buttonTake.clicked.connect(self.onButtonTakeClick)

        self.buttonSave = QPushButton("Save", self)
        self.buttonSave.setGeometry(503, 165, 75, 105)
        self.buttonSave.clicked.connect(self.onButtonSaveClick)

    def takeScreenshot(self):
        pass

    def onButtonTakeClick(self):
        pass

    def onButtonSaveClick(self):
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pic_app = PicDesigner()
    pic_app.show()
    sys.exit(app.exec())
