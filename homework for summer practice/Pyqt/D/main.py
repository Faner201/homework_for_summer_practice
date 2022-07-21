from PySide6.QtWidgets import QApplication
from window_db import WindowDB
import sys

def main():
    app = QApplication(sys.argv)
    programm = WindowDB()
    programm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()