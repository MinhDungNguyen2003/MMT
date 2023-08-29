from registry_design import RegistryDesign
import global_variables as gv
import utils
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import sys
from PyQt6.QtWidgets import QApplication

class RegistryApp(RegistryDesign):
    def __init__(self):
        super().__init__()

    def onButtonInjectRegistryClick(self):
        content = self.registryInput.toPlainText()
        self.executeAndHandleResult(f"registry_inject('''{content}''')")

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
                QMessageBox.warning(self, "Error", "Failed to open file\nPlease choose a readable file")

    def onButtonInjectClick(self):
        callee = {
            "Get Value": f"registry_get_value('{self.linkInput.text()}', '{self.nameValueInput.text()}')",
            "Set Value": f"""registry_set_value(
                '{self.linkInput.text()}',
                '{self.nameValueInput.text()}',
                '{self.valueInput.text()}',
                '{self.optionTypeValue.currentText()}'
            )""",
            "Delete Value": f"registry_delete_value('{self.linkInput.text()}', '{self.nameValueInput.text()}')",
            "Create Key": f"registry_create_key('{self.linkInput.text()}')",
            "Delete Key": f"registry_delete_key('{self.linkInput.text()}')"
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
        utils.write(gv.client, command)
        message = utils.read_str(gv.client)
        if "Please" in message:
            QMessageBox.warning(self, "Error", message)
            self.Output.setText(...,"Lỗi\n")
        else:
            QMessageBox.information(self, "Success", message)
            self.Output.setText(...,message+"\n")

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registry_app = RegistryApp()
    registry_app.show()
    sys.exit(app.exec_())