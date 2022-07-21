from PySide6.QtWidgets import QWidget, QLabel, QPlainTextEdit, QTextBrowser, QPushButton, QMainWindow

class InputWindow(QMainWindow):
    def __init__(self):
        self.text = ""
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("HTML editor")

        self.label = QLabel(self)
        self.label.setGeometry(120, 30, 200, 100)
        self.label.setText("Введите ниже HTML код")

        self.code_input = QPlainTextEdit(self)
        self.code_input.setGeometry(100, 100, 200, 150)

        self.btn = QPushButton('Перевести', self)
        self.btn.resize(100, 30)
        self.btn.move(150, 300)
        self.btn.clicked.connect(self.pushed)

    
    def pushed(self):
        self.text = self.code_input.toPlainText()
        self.code_output = OutputWindow(self.text)
        self.close()
        self.code_output.show()

    
class OutputWindow(QWidget):
    def __init__(self, text):
        self.text = text
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("HTML editor")

        self.code_output = QTextBrowser(self)
        self.code_output.setGeometry(100, 100, 200, 100)
        self.code_output.setText(self.text)