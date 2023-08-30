from pic_designer import PicDesign
import os
import utils
import glob_var as gv
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtWidgets import QApplication


class PicApp(PicDesign):
    def __init__(self):
        super().__init__()
        self.path = os.path.join(os.path.dirname(
            __file__), "cache\\screenshot.bmp")

        self.takeScreenshot()

    def takeScreenshot(self):
        utils.write(gv.client, "takeScreenshot()")
        data = utils.read_all(gv.client, utils.read_int(gv.client), True)

        with open(self.path, "wb") as f:
            f.write(data)

        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.pictureLabel.setPixmap(pixmap)

    def saveScreenshot(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Screenshot", self.path,
            "PNG Images (*.png);;JPG Images (*.jpg);;BMP Images (*.bmp);;All Files (*.*)"
        )

        if file_name:
            self.pictureLabel.pixmap().save(file_name)

    def onButtonTakeClick(self):
        self.takeScreenshot()

    def onButtonSaveClick(self):
        self.saveScreenshot()

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pic_app = PicApp()
    pic_app.show()
    sys.exit(app.exec())
