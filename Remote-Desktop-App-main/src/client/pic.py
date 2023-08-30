from PyQt6.QtWidgets import QFileDialog, QApplication
from picDesigner import PicDesigner
from PyQt6.QtGui import QPixmap
import os
import globalVar as gv
import utils
import sys


class PicApp(PicDesigner):
    def __init__(self):
        super().__init__()
        self.path = os.path.join(os.path.dirname(
            __file__), "cache\\screenshot.bmp")

        self.takeScreenshot()

    def takeScreenshot(self):
        utils.send(gv.client, "takeScreenshot()")
        data = utils.readAll(gv.client, utils.readInt(gv.client), True)

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
    picApp = PicApp()
    picApp.show()
    sys.exit(app.exec())
