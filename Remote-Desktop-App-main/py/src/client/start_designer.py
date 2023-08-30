import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class StartDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start")
        self.setGeometry(510, 420, 266, 45)


        self.buttonStart = QPushButton("Start", self)
        self.buttonStart.setGeometry(181, 10, 75, 25)
        self.buttonStart.clicked.connect(self.onButtonStartClick)

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Enter Name")
        self.idInput.setGeometry(10, 10, 166, 25)

    def onButtonStartClick(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_app = StartDesign()
    start_app.show()
    sys.exit(app.exec())
