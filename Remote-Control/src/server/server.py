from PyQt6.QtNetwork import QTcpServer, QHostAddress, QAbstractSocket
from PyQt6.QtWidgets import QApplication
from serverDesigner import ServerDesigner
import socket
import sys
import os
import re
import winreg
import globalVar
import subprocess
from keylogger import Keylogger


class ServerApp(ServerDesigner):
    def __init__(self):
        super().__init__()
        self.keylogger = Keylogger()

    def getNetworkIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ipAddress = s.getsockname()[0]
        s.close()
        return ipAddress

    def onButtonOpenServerClick(self):
        if globalVar.server is None:
            ipAddress = self.getNetworkIP()
            print(ipAddress)
            globalVar.server = QTcpServer(self)
            globalVar.server.listen(QHostAddress(ipAddress), 5656)
            globalVar.server.newConnection.connect(self.onNewConnection)
            self.buttonOpenServer.setEnabled(False)
            self.buttonOpenServer.setText("Đã mở server")
            self.showIP.setText(ipAddress)

    def onNewConnection(self):
        globalVar.client = globalVar.server.nextPendingConnection()
        if globalVar.client.state() == QAbstractSocket.SocketState.ConnectedState:
            self.handleClient()

    def showApp(self):
        processes = subprocess.Popen([
            "powershell",
            "gps",
            "| ? { $_.MainWindowTitle }",
            "| select ProcessName, Id, @{Name='ThreadCount';Expression ={$_.Threads.Count}}, CPU"
        ], shell=True, stdout=subprocess.PIPE).stdout.readlines()[3:-2]
        processes = [process.decode().rstrip() for process in processes]
        apps = []

        for process in processes:
            m = re.match("(.+?) +(\d+) +(\d+) *(\d*,?\d*)", process)
            apps.append([m.group(1), m.group(2), m.group(3),
                        m.group(4) if m.group(4) else "0"])

        self.sendResponse(str(f"{len(str(apps))}\n"))
        self.sendResponse(str(apps))

    def showProcess(self):
        processes = subprocess.Popen([
            "powershell",
            "gps",
            "| select ProcessName, Id, @{Name='ThreadCount';Expression ={$_.Threads.Count}}, CPU"
        ], shell=True, stdout=subprocess.PIPE).stdout.readlines()[3:-2]
        processes = [process.decode().rstrip() for process in processes]
        apps = []

        for process in processes:
            m = re.match("(.+?) +(\d+) +(\d+) *(\d*,?\d*)", process)
            apps.append([m.group(1), m.group(2), m.group(3),
                        m.group(4) if m.group(4) else "0"])

        self.sendResponse(str(f"{len(str(apps))}\n"))
        self.sendResponse(str(apps))

    def kill(self, processId, isApp):
        result = subprocess.call(
            ["powershell", "taskkill /F /PID", processId],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            if eval(isApp):
                self.sendResponse(
                    f"Error: Không tìm thấy ứng dụng {processId}")
            else:
                self.sendResponse(
                    f"Error: Không tìm thấy proccess {processId}")
        else:
            if eval(isApp):
                self.sendResponse(f"Đã tắt ứng dụng {processId}")
            else:
                self.sendResponse(f"Đã diệt proccess {processId}")

    def start(self, exeName, isApp):
        result = subprocess.call(
            ["powershell", "Start-Process", exeName],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            if eval(isApp):
                self.sendResponse(f"Error: Không tìm thấy ứng dụng {exeName}")
            else:
                self.sendResponse(f"Error: Không tìm thấy proccess {exeName}")
        else:
            if eval(isApp):
                self.sendResponse(f"Đã mở ứng dụng {exeName}")
            else:
                self.sendResponse(f"Đã mở proccess {exeName}")

    def takeScreenshot(self):
        path = os.path.join(os.path.dirname(__file__), "cache\\screenshot.bmp")

        QApplication.primaryScreen().grabWindow(0).save(path)

        with open(path, "rb") as f:
            data = f.read()

        self.sendResponse(str(f"{len(data)}\n"))
        self.sendResponse(data, True)

    def keylogHook(self):
        self.keylogger.hook()

    def keylogUnhook(self):
        self.keylogger.unhook()

    def keylogPrint(self):
        self.sendResponse(self.keylogger.print().replace("\n", "\r") + "\n")

    def keylogClear(self):
        self.keylogger.clear()

    def registryInject(self, registry):
        path = os.path.join(os.path.dirname(__file__),
                            "cache\\registryFile.reg")

        with open(path, "w") as f:
            f.write(registry)

        result = subprocess.run(
            f'regedit.exe /s "{path}"',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        if result.stderr:
            self.sendResponse("Error: Sửa thất bại")
        else:
            self.sendResponse("Sửa thành công!")

    def registryGetValue(self, path, nameValue):
        try:
            rootKey, subKey = path.split("\\", 1)
            rootKey = getattr(winreg, rootKey)
            key = winreg.OpenKey(rootKey, subKey)
            value, _ = winreg.QueryValueEx(key, nameValue)
            winreg.CloseKey(key)

            self.sendResponse(f"{value}\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registrySetValue(self, path, nameValue, value, typeOption):
        try:
            rootKey, subKey = path.split("\\", 1)
            rootKey = getattr(winreg, rootKey)
            key = winreg.OpenKey(rootKey, subKey, 0, winreg.KEY_SET_VALUE)
            typeVal = ""

            if typeOption == "String":
                typeVal = winreg.REG_SZ
            elif typeOption == "Multi-String":
                typeVal = winreg.REG_MULTI_SZ
            elif typeOption == "Expandable String":
                typeVal = winreg.REG_EXPAND_SZ
            elif typeOption == "DWORD":
                typeVal = winreg.REG_DWORD
                value = int(value)
            elif typeOption == "QWORD":
                typeVal = winreg.REG_QWORD
                value = int(value)
            elif typeOption == "Binary":
                typeVal = winreg.REG_BINARY
                value = bytes(map(int, value.split()))
            else:
                self.sendResponse("Error: kiểu không hợp lệ\n")
                return

            winreg.SetValueEx(key, nameValue, 0, typeVal, value)
            winreg.CloseKey(key)

            self.sendResponse("Set value thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryDeleteValue(self, path, nameValue):
        try:
            rootKey, subKey = path.split("\\", 1)
            rootKey = getattr(winreg, rootKey)
            key = winreg.OpenKey(rootKey, subKey, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, nameValue)
            winreg.CloseKey(key)

            self.sendResponse("Xóa value thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryCreateKey(self, path):
        try:
            rootKey, subKey = path.split("\\", 1)
            rootKey = getattr(winreg, rootKey)
            key = winreg.CreateKey(rootKey, subKey)
            winreg.CloseKey(key)

            self.sendResponse("Tạo key thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryDeleteKey(self, path):
        try:
            rootKey, subKey = path.split("\\", 1)
            rootKey = getattr(winreg, rootKey)
            winreg.DeleteKey(rootKey, subKey)

            self.sendResponse("Xóa key thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def handleClient(self):
        while True:
            functionCall = self.receiveSignal()
            function = functionCall.split("(")[0]

            if hasattr(self, function):
                eval(f"self.{functionCall}")

    def receiveSignal(self, size=1024):
        try:
            globalVar.client.waitForReadyRead()
            return globalVar.client.read(size).decode()
        except:
            self.quit()

    def shutdown(self):
        try:
            os.system("shutdown /s /t 15")
            self.sendResponse("Shutdown!")
        except:
            self.sendResponse("Error: Shutdown thất bại")

    def logout(self):
        try:
            os.system("shutdown -l")
            self.sendResponse("Logged out!")
        except:
            self.sendResponse("Error: Logout thất bại")

    def sendResponse(self, response, raw=False):
        globalVar.client.write(response if raw else response.encode())
        globalVar.client.flush()
        globalVar.client.waitForBytesWritten()

    def quit(self):
        globalVar.client.close()
        globalVar.server.close()
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    serverApp = ServerApp()
    serverApp.show()
    sys.exit(app.exec())
