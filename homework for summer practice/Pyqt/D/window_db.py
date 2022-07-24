import sqlite3
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QGridLayout
from PySide6.QtCore import Qt
from designer.design import Ui_MainWindow

sqlite_connection = sqlite3.connect(r'/Users/fanfurick/Documents/code/homework_for_summer_practice/Pyqt/D/films.db')
cursor = sqlite_connection.cursor()


tootlips = [
    "Название фильма", 
    "Год создания", 
    "Жанр", 
    "Хрономитраж"
]

class WindowDB(QMainWindow):
    def __init__(self):
        super(WindowDB, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.btn_search_title.clicked.connect(self.search_name)
        self.ui.btn_search_title_2.clicked.connect(self.search_gread)
        self.ui.btn_add_film.clicked.connect(self.adding_movie)


    def search_name(self) -> None:
        if self.ui.ln_search_title.text():
            text = self.ui.ln_search_title.text()
            cursor.execute("select * from Films where title like ?", (text+'%',))
            self.processing_db(self.search())


    def search(self):
        numbers = []
        while True:
                equest = cursor.fetchone()
                if equest:
                    numbers.append(equest[1:])
                else:
                    break
        return numbers


    def processing_db(self, numbers) -> None:
        grid_layout = QGridLayout(self)
        self.ui.list_films.setMaximumHeight(400)
        self.ui.list_films.setMaximumWidth(700)
        self.ui.list_films.setColumnCount(len(numbers[0]))
        self.ui.list_films.setRowCount(len(numbers))
        self.ui.list_films.setHorizontalHeaderLabels(["Название фильма", "Год создания", "Жанр", "Хрономитраж"])
        for tootlip in range(len(numbers[0])):
            self.ui.list_films.horizontalHeaderItem(tootlip).setToolTip(str(numbers[0][tootlip]))
            self.ui.list_films.horizontalHeaderItem(tootlip).setTextAlignment(Qt.AlignHCenter)

        for number in range(len(numbers)):
            for tootlip in range(len(numbers[0])):
                self.ui.list_films.setItem(number, tootlip, QTableWidgetItem(str(numbers[number][tootlip])))

        self.ui.list_films.resizeColumnsToContents()

        grid_layout.addWidget(self.ui.list_films, 0, 0)


    def search_gread(self) -> None:
        if self.ui.ln_serch_cat.text():
            text = self.ui.ln_serch_cat.text().lower()
            cursor.execute(f"select * from genres where title = '{text}'")
            equast_text = cursor.fetchone()
            cursor.execute(f"select * from Films where genre = '{equast_text[0]}'")
            self.processing_db(self.search())


    def adding_movie(self) -> None:
        if self.ui.ln_create_film.text() and self.ui.date.text() and self.ui.ln_create_cat.text() and self.ui.duration.text():
            name_text = self.ui.ln_create_film.text()
            date_text = self.ui.date.text()
            category_text = self.ui.ln_create_cat.text().lower()
            duration_text = self.ui.duration.text()
            equest_category = cursor.execute(f"select * from genres where title = '{category_text}'").fetchone()
            cursor.execute(f"insert into Films (title, year, genre, duration) values('{name_text}', '{date_text}', '{equest_category[0]}', '{duration_text}')")
            sqlite_connection.commit()
            cursor.execute(f"select * from Films where title = '{name_text}'")
            equest_add = cursor.fetchone()
            number = []
            number.append(equest_add[1:])
            self.processing_db(number)