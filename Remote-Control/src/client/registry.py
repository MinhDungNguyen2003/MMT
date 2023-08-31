from PyQt6.QtWidgets import QFileDialog, QMessageBox, QApplication
from registryDesigner import RegistryDesigner
import globalVar
import utils
import sys


class RegistryApp(RegistryDesigner):
    def __init__(self):
        super().__init__()

    def onButtonInjectRegistryClick(self):
        content = self.registryInput.toPlainText()
        self.executeAndHandleResult(f"registryInject('''{content}''')")

    def onBrowseInputChange(self):
        if "." in self.browseInput.text():
            try:
                with open(self.browseInput.text(), "r") as f:
                    self.registryInput.setText(f.read())
            except:
                pass

    def onButtonBrowseClick(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Registry File", "", "Registry Files (*.reg);;All Files (*.*)"
        )
        if file_name:
            self.browseInput.setText(file_name)
            try:
                with open(file_name, "r") as f:
                    self.registryInput.setText(f.read())
            except:
                QMessageBox.warning(
                    self, "Error", "Failed to open file\nPlease choose a readable file")

    def onButtonInjectClick(self):
        callee = {
            "Get Value": f"registryGetValue('{self.linkInput.text()}', '{self.nameValueInput.text()}')",
            "Set Value": f"""registrySetValue(
                '{self.linkInput.text()}',
                '{self.nameValueInput.text()}',
                '{self.valueInput.text()}',
                '{self.optionTypeValue.currentText()}'
            )""",
            "Delete Value": f"registryDeleteValue('{self.linkInput.text()}', '{self.nameValueInput.text()}')",
            "Create Key": f"registryCreateKey('{self.linkInput.text()}')",
            "Delete Key": f"registryDeleteKey('{self.linkInput.text()}')"
        }
        command = callee[self.optionApp.currentText()].replace("\\", "\\\\")
        self.executeAndHandleResult(command)

    def onOptionAppChange(self, index):
        visibility = {
            "Get Value": [True, False, False],
            "Set Value": [True, True, True],
            "Delete Value": [True, False, False],
            "Create Key": [False, False, False],
            "Delete Key": [False, False, False]
        }
        selected = self.optionApp.currentText()
        self.nameValueInput.setVisible(visibility[selected][0])
        self.valueInput.setVisible(visibility[selected][1])
        self.optionTypeValue.setVisible(visibility[selected][2])

    def onButtonClearClick(self):
        self.Output.setText("")

    def executeAndHandleResult(self, command):
        utils.send(globalVar.client, command)
        message = utils.readStr(globalVar.client)
        if "Error" in message:
            QMessageBox.warning(self, "Error", message)
            curr_text = self.Output.toPlainText()
            new_txt = curr_text + "Lỗi\n"
            self.Output.setPlainText(new_txt)
        else:
            QMessageBox.information(self, "Success", message)
            current_text = self.Output.toPlainText()
            new_text = current_text + message + "\n"

            self.Output.setPlainText(new_text)

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    registryApp = RegistryApp()
    registryApp.show()
    sys.exit(app.exec_())
