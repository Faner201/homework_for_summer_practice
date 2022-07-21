from typing import Optional, Union
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFontDatabase
from designer.design import Ui_Form
from operator import add, sub, mul, truediv


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


class Calculate(QWidget):
    def __init__(self):
        super(Calculate, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        self.ui.btn.clicked.connect(self.clear_all)
        self.ui.btn_backspace.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)

        self.ui.btn_add.clicked.connect(lambda: self.math_operation('+'))
        self.ui.btn_sub.clicked.connect(lambda: self.math_operation('-'))
        self.ui.btn_mul.clicked.connect(lambda: self.math_operation('*'))
        self.ui.btn_truediv.clicked.connect(lambda: self.math_operation('/'))
        self.ui.btn_equally.clicked.connect(self.calculate)


    def add_digit(self, button_text: str):
        if self.ui.le_entry.text() == '0':
            self.ui.le_entry.setText(button_text)
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text() + button_text)


    def add_point(self) -> None:
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    
    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()


    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')


    @staticmethod
    def remove_zero(num:str) -> str:
        zero = str(float(num))
        return zero[:-2] if zero[-2:] == '.0' else zero


    def add_temp(self, math_signal: str) -> None:
        if not self.ui.lbl_temp.text() or self.get_math_signal() == '=':
            self.ui.lbl_temp.setText(self.remove_zero(self.ui.le_entry.text()) + f' {math_signal} ')
            self.ui.le_entry.setText('0')


    def get_entry_number(self) -> Union[int, float]:
        number = self.ui.le_entry.text().strip('.')

        return float(number) if '.' in number else int(number)

    
    def get_temp_number(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    
    def get_math_signal(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]


    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            try:
                result = self.remove_zero(
                    str(operations[self.get_math_signal()](self.get_temp_number(), self.get_entry_number()))
                )
            except ZeroDivisionError:
                result = "Нельзя делить на 0"
            finally:
                self.ui.lbl_temp.setText(temp + self.remove_zero(entry) + ' =')
                self.ui.le_entry.setText(result)
                return result


    def math_operation(self, math_signal: str):
        temp = self.ui.lbl_temp.text()

        if not temp:
            self.add_temp(math_signal)
        else:
            if self.get_math_signal() != math_signal:
                if self.get_math_signal() == '=':
                    self.add_temp(math_signal)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_signal} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f' {math_signal}')