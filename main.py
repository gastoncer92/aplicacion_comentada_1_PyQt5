import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from gui_1_ui import *
from gui_2_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(
            self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(
            self.ventanaNueva)

    def ventanaNueva(self):
        gui2.show()


class Window2(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


app = QApplication([])
gui = MainWindow()
gui2 = Window2()
gui.show()
app.exec_()
