from PySide6.QtWidgets import *
from PySide6 import QtCore, QtWidgets

class KfcWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: #b29cb5;')
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(25, 20, 300, 210))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 250, 100, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setText("Купить")


    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle("Терминал")



class KfcValue(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(210, 80)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 40, 130, 35))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStyleSheet('background-color: #b29cb5;')
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 190, 30))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setStyleSheet('background-color: #b29cb5;')

        self.retranslate_ui(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslate_ui(self, Dialog):
        Dialog.setWindowTitle("Выберите количество")


class Cheque(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 300)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: #b29cb5;')
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 580, 230))
        self.textBrowser.setObjectName("textBrowser")


    def retranslate_ui(self, Form):
        Form.setWindowTitle("Чек")

