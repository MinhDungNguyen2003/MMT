from PyQt6.QtWidgets import QApplication
from client import ClientApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientApp = ClientApp()
    clientApp.show()
    sys.exit(app.exec())
