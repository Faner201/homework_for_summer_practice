from PySide6.QtWidgets import QApplication
from calculate import Calculate
import sys


def main():
    app = QApplication(sys.argv)
    programm = Calculate()
    programm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()