from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import designer.files_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(324, 500)
        Form.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton#btn\n"
",#btn_backspace\n"
",#btn_del\n"
",#btn_truediv\n"
",#btn_mul\n"
",#btn_sub\n"
",#btn_add\n"
",#button{\n"
"    color:#f90;\n"
"}\n"
"\n"
"QPushButton#btn_equally {\n"
"    color: #f90;\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(Form)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setMinimumSize(QSize(300, 0))
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(Form)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"front-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(100)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_button = QGridLayout()
        self.layout_button.setObjectName(u"layout_button")
        self.btn_add = QPushButton(Form)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_sub = QPushButton(Form)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_0 = QPushButton(Form)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_mul = QPushButton(Form)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_point = QPushButton(Form)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_equally = QPushButton(Form)
        self.btn_equally.setObjectName(u"btn_equally")
        sizePolicy2.setHeightForWidth(self.btn_equally.sizePolicy().hasHeightForWidth())
        self.btn_equally.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_equally, 4, 3, 1, 1)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn = QPushButton(Form)
        self.btn.setObjectName(u"btn")
        sizePolicy2.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
        self.btn.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn, 0, 0, 1, 1)

        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        sizePolicy2.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.button, 4, 0, 1, 1)

        self.btn_truediv = QPushButton(Form)
        self.btn_truediv.setObjectName(u"btn_truediv")
        sizePolicy2.setHeightForWidth(self.btn_truediv.sizePolicy().hasHeightForWidth())
        self.btn_truediv.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_truediv, 0, 3, 1, 1)

        self.btn_del = QPushButton(Form)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy2.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_del, 0, 2, 1, 1)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_backspace = QPushButton(Form)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)

        self.layout_button.addWidget(self.btn_backspace, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.layout_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"calculate", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("Form", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("Form", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("Form", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("Form", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("Form", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("Form", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("Form", u"x", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("Form", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("Form", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("Form", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("Form", u".", None))
#endif // QT_CONFIG(shortcut)

        for sc in (','):
                QShortcut(sc, self.btn_point). activated.connect(self.btn_point.animateClick)

        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("Form", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("Form", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_equally.setText(QCoreApplication.translate("Form", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_equally.setShortcut(QCoreApplication.translate("Form", u"=", None))
#endif // QT_CONFIG(shortcut)

        for sc in ('Enter', 'Return'):
                QShortcut(sc, self.btn_equally). activated.connect(self.btn_equally.animateClick)


        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("Form", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn.setText(QCoreApplication.translate("Form", u"C", None))
        self.button.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.btn_truediv.setText(QCoreApplication.translate("Form", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_truediv.setShortcut(QCoreApplication.translate("Form", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_del.setText(QCoreApplication.translate("Form", u"<-", None))
#if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(QCoreApplication.translate("Form", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("Form", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("Form", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText(QCoreApplication.translate("Form", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("Form", u"Del", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

