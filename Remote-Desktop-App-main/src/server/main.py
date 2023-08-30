import sys
from PyQt6.QtWidgets import QApplication
from server import ServerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    serverApp = ServerApp()
    serverApp.show()
    sys.exit(app.exec())
