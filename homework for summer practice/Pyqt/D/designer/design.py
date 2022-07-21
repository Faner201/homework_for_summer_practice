from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #968c8c")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_search_title = QPushButton(self.centralwidget)
        self.btn_search_title.setObjectName(u"btn_search_title")
        self.btn_search_title.setGeometry(QRect(50, 10, 75, 23))
        self.btn_search_title.setStyleSheet(u"color: #ffffff;")
        self.btn_add_film = QPushButton(self.centralwidget)
        self.btn_add_film.setObjectName(u"btn_add_film")
        self.btn_add_film.setGeometry(QRect(50, 40, 75, 23))
        self.btn_add_film.setStyleSheet(u"color: #ffffff;")
        self.ln_create_film = QLineEdit(self.centralwidget)
        self.ln_create_film.setObjectName(u"ln_create_film")
        self.ln_create_film.setGeometry(QRect(160, 40, 411, 20))
        self.ln_create_film.setStyleSheet(u"color: #ffffff;")
        self.ln_create_cat = QLineEdit(self.centralwidget)
        self.ln_create_cat.setObjectName(u"ln_create_cat")
        self.ln_create_cat.setGeometry(QRect(650, 40, 42, 22))
        self.ln_create_cat.setStyleSheet(u"color: #ffffff;")
        self.ln_search_title = QLineEdit(self.centralwidget)
        self.ln_search_title.setObjectName(u"ln_search_title")
        self.ln_search_title.setGeometry(QRect(160, 10, 411, 20))
        self.ln_search_title.setStyleSheet(u"color: #ffffff;")
        self.btn_search_title_2 = QPushButton(self.centralwidget)
        self.btn_search_title_2.setObjectName(u"btn_search_title_2")
        self.btn_search_title_2.setGeometry(QRect(50, 70, 75, 23))
        self.btn_search_title_2.setStyleSheet(u"color: #ffffff;")
        self.list_films = QTableWidget(self.centralwidget)
        self.list_films.setObjectName(u"list_films")
        self.list_films.setGeometry(QRect(45, 110, 711, 431))
        self.list_films.setStyleSheet(u"color: #ffffff;")
        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(590, 40, 42, 22))
        self.date.setStyleSheet(u"color: #ffffff;")
        self.duration = QLineEdit(self.centralwidget)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(710, 40, 51, 22))
        self.duration.setStyleSheet(u"color: #ffffff;")
        self.ln_serch_cat = QLineEdit(self.centralwidget)
        self.ln_serch_cat.setObjectName(u"ln_serch_cat")
        self.ln_serch_cat.setGeometry(QRect(160, 70, 411, 21))
        self.ln_serch_cat.setStyleSheet(u"color: #ffffff;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_search_title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_add_film.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ln_create_film.setText("")
        self.ln_create_film.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u0435\u0438\u0435 \u0444\u0438\u043b\u044c\u043c\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442\u0435\u0441\u044c \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ln_create_cat.setText("")
        self.ln_create_cat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440", None))
        self.ln_search_title.setText("")
        self.ln_search_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0438\u043b\u044c\u043c\u0430", None))
        self.btn_search_title_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.duration.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.ln_serch_cat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0436\u0430\u043d\u0440 \u0444\u0438\u043b\u044c\u043c\u0430", None))
    # retranslateUi

