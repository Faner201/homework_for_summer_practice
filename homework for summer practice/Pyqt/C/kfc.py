import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QIcon
from PySide6 import QtCore
from designer import KfcValue, KfcWindow, Cheque

import json

with open(r'/Users/fanfurick/Documents/code/homework_for_summer_practice/Pyqt/C/products.json') as file:
    products = json.load(file)


value = 0


class Cheque(QWidget, Cheque):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


class SetValue(QDialog, KfcValue):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.buttonBox.accepted.connect(self.get_value)


    def get_value(self):
        global value
        value = self.spinBox.value()


class Terminal(QMainWindow, KfcWindow):
    def __init__(self):
        super().__init__()
        self.cheque = Cheque()
        self.setup_ui(self)
        self.listWidget.setViewMode(QListWidget.IconMode)
        for item in products:
            pixmap = QPixmap(item['src'])
            item = QListWidgetItem(QIcon(pixmap), item['name'] + ' - ' + item['cost'])
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
        self.listWidget.itemChanged.connect(self.changed)
        self.order = dict()
        self.prices = dict()
        self.pushButton.clicked.connect(self.get_cheque)


    def changed(self, item):
        pos, price = item.text().split(' - ')
        self.prices[pos] = int(price)
        if item.checkState():
            window = SetValue()
            window.show()
            window.exec()
            self.order[pos] = value
        else:
            self.order[item.text()] = 0


    def get_cheque(self):
        total_price = 0
        cheque_text = str()
        for name in self.order.keys():
            if self.order[name] > 0:
                current_price = self.prices[name] * self.order[name]
                if 1 == current_price % 10:
                    rubles = 'рубль'
                elif 2 <= current_price % 10 <= 4:
                    rubles = 'рубля'
                else:
                    rubles = 'рублей'
                cheque_text += '"{}" в количестве {} шт., \t {} {}.\n'.format(name,
                                                                              self.order[name], current_price, rubles)
                total_price += current_price
        if 1 == total_price % 10:
            rubles = 'рубль'
        elif 2 <= total_price % 10 <= 4:
            rubles = 'рубля'
        else:
            rubles = 'рублей'
        cheque_text += "Сумма к оплате: {} {}".format(total_price, rubles)
        self.cheque.textBrowser.setText(cheque_text)
        self.cheque.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Terminal()
    ex.show()
    sys.exit(app.exec())
