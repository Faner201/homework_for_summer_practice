from PySide6.QtWidgets import QApplication
from window import InputWindow
import sys

def main():
    app = QApplication(sys.argv)
    programm = InputWindow()
    programm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()