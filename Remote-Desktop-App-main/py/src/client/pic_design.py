import os, sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class PicDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Take Screenshots")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WIN16 + gv.G + gv.S + gv.GL, gv.WIN9)

        self.pictureLabel = QLabel(self)
        self.pictureLabel.setGeometry(gv.GL, gv.GL, gv.WIN16 - gv.GL, gv.WIN9 - 2 * gv.GL)
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setPixmap(QPixmap(os.getcwd() + "/pic.png"))

        self.buttonTake = QPushButton("Take\nScreenshot", self)
        self.buttonTake.setGeometry(gv.WIN16 + gv.G, gv.GL, gv.S, gv.SXL)
        self.buttonTake.clicked.connect(self.onButtonTakeClick)

        self.buttonSave = QPushButton("Save", self)
        self.buttonSave.setGeometry(gv.WIN16 + gv.G, gv.GL + gv.G + gv.SXL, gv.S, gv.WIN9 - gv.G - 2 * gv.GL - gv.SXL)
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
    pic_app = PicDesign()
    pic_app.show()
    sys.exit(app.exec())
