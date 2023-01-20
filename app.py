import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from gui.main_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        # self.stats_list = [9, 9, 9, 9, 9, 9]

        # self.str_stat.set_name("STR")
        # self.con_stat.set_name("CON")
        # self.dex_stat.set_name("DEX")
        # self.int_stat.set_name("INT")
        # self.wis_stat.set_name("WIS")
        # self.cha_stat.set_name("CHA")

        # # Populate "classes" combobox
        # self.classes.addItem('war')
        # self.classes.addItem('pal')
        # self.classes.addItem('ran')
        # self.classes.addItem('mag')
        # self.classes.addItem('cle')
        # self.classes.addItem('dru')
        # self.classes.addItem('thi')
        # self.classes.addItem('bar')

        # # Populate "races" combobox
        # self.races.addItem('hum')
        # self.races.addItem('elf')
        # self.races.addItem('dwa')

    def connectSignalsSlots(self):
        # self.action_Exit.triggered.connect(self.close)
        # self.action_Find_Replace.triggered.connect(self.findAndReplace)
        # self.action_About.triggered.connect(self.about)
        # self.create.clicked.connect(self.createClick)
        # self.classes.currentIndexChanged.connect(self.classChanged)
        pass

    # def classChanged(self):
    #     if not fullfill_req(self.stats_list, self.classes.currentText()):
    #         pass

    # def findAndReplace(self):
    #     dialog = FindReplaceDialog(self)
    #     dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    # def createClick(self):
    #     self.stats_list = create_char('Pepito', self.classes.currentText(), self.races.currentText(), 1)
    #     self.str_stat.set_value(self.stats_list[0])
    #     self.con_stat.set_value(self.stats_list[1])
    #     self.dex_stat.set_value(self.stats_list[2])
    #     self.int_stat.set_value(self.stats_list[3])
    #     self.wis_stat.set_value(self.stats_list[4])
    #     self.cha_stat.set_value(self.stats_list[5])


# class FindReplaceDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi("ui/find_replace.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
