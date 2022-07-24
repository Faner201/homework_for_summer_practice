from PySide6.QtWidgets import QApplication
from kfc import Terminal
import sys


def main():
    app = QApplication(sys.argv)
    programm = Terminal()
    programm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()