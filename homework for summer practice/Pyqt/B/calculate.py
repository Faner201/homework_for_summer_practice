from typing import Optional, Union
from unicodedata import digit
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFontDatabase
from designer.design import Ui_Form
from operator import add, sub, mul, truediv


operations = {
    '+': add,
    '-': sub,
    'x': mul,
    '/': truediv,
}

error_zero_div = 'Деление на ноль'
error_undefined = 'Результат не определён'


class Calculate(QWidget):
    def __init__(self):
        super(Calculate, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        self.ui.btn.clicked.connect(self.clear_all)
        self.ui.btn_backspace.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.button.clicked.connect(self.denial)
        self.ui.btn_del.clicked.connect(self.backspace)

        self.ui.btn_add.clicked.connect(self.math_operation)
        self.ui.btn_sub.clicked.connect(self.math_operation)
        self.ui.btn_mul.clicked.connect(self.math_operation)
        self.ui.btn_truediv.clicked.connect(self.math_operation)
        self.ui.btn_equally.clicked.connect(self.calculate)


    def add_digit(self) -> None:
        self.remove_error()
        self.clearing_input()
        btn = self.sender()
        
        digit_buttons = (
            'btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
            'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9'
        )

        if btn.objectName() in digit_buttons:
            if self.ui.le_entry.text() == '0':
                self.ui.le_entry.setText(btn.text())
            else:
                self.ui.le_entry.setText(self.ui.le_entry.text() + btn.text())


    def add_point(self) -> None:
        self.clearing_input()
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')


    def denial(self) -> None:
        self.clearing_input()
        entry = self.ui.le_entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]
        self.ui.le_entry.setText(entry)


    def backspace(self) -> None:
        self.remove_error()
        self.clearing_input()
        entry = self.ui.le_entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and entry[:1] == '-':
                self.ui.le_entry.setText('0')
            else:
                self.ui.le_entry.setText(entry[:-1])
        else:
            self.ui.le_entry.setText('0')
                    

    
    def clear_all(self) -> None:
        self.remove_error()
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()


    def clear_entry(self) -> None:
        self.remove_error()
        self.clearing_input()
        self.ui.le_entry.setText('0')

    
    def clearing_input(self) -> None:
        if self.get_math_signal() == '=':
            self.ui.lbl_temp.clear()


    @staticmethod
    def remove_zero(num:str) -> str:
        zero = str(float(num))
        return zero[:-2] if zero[-2:] == '.0' else zero


    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_zero(self.ui.le_entry.text())

        if not self.ui.lbl_temp.text() or self.get_math_signal() == '=':
            self.ui.lbl_temp.setText(entry + f' {btn.text()} ')
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
                self.ui.lbl_temp.setText(temp + self.remove_zero(entry) + ' =')
                self.ui.le_entry.setText(result)
                return result
            except KeyError:
                pass
            except ZeroDivisionError:
                if self.get_temp_number() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)



    def math_operation(self) -> None:
        temp = self.ui.lbl_temp.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math_signal() != btn.text():
                if self.get_math_signal() == '=':
                    self.add_temp()
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{btn.text()} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f' {btn.text()}')


    def show_error(self, text: str) -> None:
        self.ui.le_entry.setText(text)
        self.disable_buttons(True)


    def remove_error(self) -> None:
        if self.ui.le_entry.text() in (error_undefined, error_zero_div):
            self.ui.le_entry.setText('0')
            self.disable_buttons(False)

    
    def disable_buttons(self, disable: bool) -> None:
        self.ui.btn_add.setDisabled(disable)
        self.ui.btn_sub.setDisabled(disable)
        self.ui.btn_truediv.setDisabled(disable)
        self.ui.btn_mul.setDisabled(disable)
        self.ui.btn_point.setDisabled(disable)
        self.ui.button.setDisabled(disable)
        self.ui.btn_equally.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: #f90;'
        self.change_buttons_color(color)

    
    def change_buttons_color(self, color: str) -> None:
        self.ui.btn_add.setStyleSheet(color)
        self.ui.btn_sub.setStyleSheet(color)
        self.ui.btn_truediv.setStyleSheet(color)
        self.ui.btn_mul.setStyleSheet(color)
        self.ui.btn_point.setStyleSheet(color)
        self.ui.button.setStyleSheet(color)
        self.ui.btn_equally.setStyleSheet(color)
