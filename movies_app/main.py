import sys
import db_config
from models import Media
from db_config import query_actors, query_directors, generate_query_for_year_others, LIMIT, OFFSET
from db_connect import get_connection_search, execute_query, execute_query_search
from ui_interface import *
from Custom_Widgets.Widgets import *
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QListWidgetItem, QButtonGroup, QMessageBox
from PySide6.QtNetwork import QNetworkAccessManager


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.last_query_count = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_image_loaded)
        self.pending_image_loads = {}
        self.list_items = {}
        self.setup_checkbox_group()
        self.ui.searchPushBtn.clicked.connect(self.perform_search)
        self.ui.searchMethod.returnPressed.connect(self.perform_search)

        self.current_limit = LIMIT
        self.current_offset = OFFSET
        self.current_query = None
        self.setup_buttons()

        self.current_search_query = None
        self.current_search_category = None


        self.search_display_manager = SearchDisplayManager(self.ui)
        self.ui.searchMainPushBtn.clicked.connect(self.search_display_manager.update_search_category)
        self.ui.byFilms.clicked.connect(self.search_display_manager.update_search_category)
        self.ui.byActors.clicked.connect(self.search_display_manager.update_search_category)
        self.ui.byDirectors.clicked.connect(self.search_display_manager.update_search_category)

        self.ui.mainPrint.itemClicked.connect(self.on_item_clicked)

        # Установите значение по умолчанию для limitBox
        self.ui.limitBox.setText(str(db_config.LIMIT))
        self.ui.limitBox.editingFinished.connect(self.update_limit)
        loadJsonStyle(self, self.ui)
        self.show()




        ########################################################################
        # FILMS
        ########################################################################

        self.ui.byFilmButton.clicked.connect(lambda: self.set_last_query("films"))

        ########################################################################
        # TV SERIES
        ########################################################################

        self.ui.serialsButton.clicked.connect(lambda: self.set_last_query("series"))

        ########################################################################
        # TOP FILMS
        ########################################################################

        self.ui.topButton.clicked.connect(lambda: self.set_last_query("films_desc"))
        self.ui.lowestRateButton.clicked.connect(lambda: self.set_last_query("films_asc"))

        ########################################################################
        # GENRES
        ########################################################################

        self.ui.genre1.clicked.connect(lambda: self.set_last_query("comedy"))
        self.ui.genre2.clicked.connect(lambda: self.set_last_query("action"))
        self.ui.genre3.clicked.connect(lambda: self.set_last_query("detective"))
        self.ui.genre4.clicked.connect(lambda: self.set_last_query("drama"))
        self.ui.genre5.clicked.connect(lambda: self.set_last_query("crime"))
        self.ui.genre6.clicked.connect(lambda: self.set_last_query("sports"))
        self.ui.genre7.clicked.connect(lambda: self.set_last_query("horror"))
        self.ui.genre8.clicked.connect(lambda: self.set_last_query("fantasy"))
        self.ui.genre9.clicked.connect(lambda: self.set_last_query("family"))
        self.ui.genre10.clicked.connect(lambda: self.set_last_query("cartoons"))

        ########################################################################
        # YEARS
        ########################################################################
        self.ui.year_others.clicked.connect(
            lambda: self.print_films_by_year(generate_query_for_year_others(LIMIT, OFFSET), "others"))

        self.ui.year_others.clicked.connect(lambda: self.set_last_query("other_year"))
        self.ui.year_2014.clicked.connect(lambda: self.set_last_query("2014"))
        self.ui.year_2015.clicked.connect(lambda: self.set_last_query("2015"))
        self.ui.year_2016.clicked.connect(lambda: self.set_last_query("2016"))
        self.ui.year_2017.clicked.connect(lambda: self.set_last_query("2017"))
        self.ui.year_2018.clicked.connect(lambda: self.set_last_query("2018"))
        self.ui.year_2019.clicked.connect(lambda: self.set_last_query("2019"))
        self.ui.year_2020.clicked.connect(lambda: self.set_last_query("2020"))
        self.ui.year_2021.clicked.connect(lambda: self.set_last_query("2021"))
        self.ui.year_2022.clicked.connect(lambda: self.set_last_query("2022"))
        self.ui.year_2023.clicked.connect(lambda: self.set_last_query("2023"))
        self.ui.year_2024.clicked.connect(lambda: self.set_last_query("2024"))


        ########################################################################
        # COUNTRIES
        ########################################################################
        self.ui.country1.clicked.connect(lambda: self.set_last_query("usa"))
        self.ui.country2.clicked.connect(lambda: self.set_last_query("spain"))
        self.ui.country3.clicked.connect(lambda: self.set_last_query("japan"))


        ########################################################################
        # ACTORS
        ########################################################################

        self.ui.actorButton.clicked.connect(
            lambda: self.print_actors_directors(query_actors(LIMIT, OFFSET), "actors")
        )

        ########################################################################
        # DIRECTORS
        ########################################################################

        self.ui.directorButton.clicked.connect(
            lambda: self.print_actors_directors(query_directors(LIMIT, OFFSET), "directors")
        )


        # Управление виджетами меню
        self.ui.filmsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.tvseriesBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.topBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.countriesBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.actorsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.directorsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.genresBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.yearBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.closeCentralMenu.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        self.ui.searchMainPushBtn.clicked.connect(lambda: self.ui.popupSearchContainer.expandMenu())
        self.ui.serachCloseBtn.clicked.connect(lambda: self.ui.popupSearchContainer.collapseMenu())

        self.current_year_query = None
        self.last_clicked_button = None

        self.is_search_active = False

    def set_last_query(self, query_type):
        self.is_search_active = False
        self.last_clicked_button = query_type
        self.current_offset = 0  # Сброс смещения при смене запроса
        self.update_list()  # Обновление списка



    def setup_buttons(self):
        self.ui.nextButton.clicked.connect(self.next_page)
        self.ui.previousButton.clicked.connect(self.prev_page)

    def update_list(self):
        query = None
        if self.last_clicked_button == "films":
            query = db_config.query_films_by_rating(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "series":
            query = db_config.query_serials(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "films_desc":
            query = db_config.query_top_rated(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "films_asc":
            query = db_config.query_lowest_rated(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "comedy":
            query = db_config.query_comedy(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "action":
            query = db_config.query_action(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "detective":
            query = db_config.query_detective(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "drama":
            query = db_config.query_drama(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "crime":
            query = db_config.query_crime(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "sports":
            query = db_config.query_sports(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "horror":
            query = db_config.query_horror(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "fantasy":
            query = db_config.query_fantasy(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "family":
            query = db_config.query_family(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "cartoons":
            query = db_config.query_cartoons(self.current_limit, self.current_offset)



        elif self.last_clicked_button == "other_year":
            query = db_config.generate_query_for_year_others(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2014":
            query = db_config.query_year_2014(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2015":
            query = db_config.query_year_2015(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2016":
            query = db_config.query_year_2016(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2017":
            query = db_config.query_year_2017(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2018":
            query = db_config.query_year_2018(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2019":
            query = db_config.query_year_2019(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2020":
            query = db_config.query_year_2020(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2021":
            query = db_config.query_year_2021(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2022":
            query = db_config.query_year_2022(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2023":
            query = db_config.query_year_2023(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "2024":
            query = db_config.query_year_2024(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "usa":
            query = db_config.query_country_usa(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "spain":
            query = db_config.query_country_spain(self.current_limit, self.current_offset)
        elif self.last_clicked_button == "japan":
            query = db_config.query_country_japan(self.current_limit, self.current_offset)


        elif self.last_clicked_button == "others":
            query = db_config.generate_query_for_year_others(self.current_limit, self.current_offset)

        if query:
            self.print_films_by_year(query, "others")
        else:
            print("No query to execute.")

    def get_category_query(self, category, limit, offset):
        category_to_query = {
            "films": db_config.query_films_by_rating,
            "series": db_config.query_serials,
            "films_desc": db_config.query_top_rated,
            "films_asc": db_config.query_lowest_rated,
            "comedy": db_config.query_comedy,
            "action": db_config.query_action,
            "detective": db_config.query_detective,
            "drama": db_config.query_drama,
            "crime": db_config.query_crime,
            "sports": db_config.query_sports,
            "horror": db_config.query_horror,
            "fantasy": db_config.query_fantasy,
            "family": db_config.query_family,
            "cartoons": db_config.query_cartoons,
            "other_year": db_config.generate_query_for_year_others,
            "2014": db_config.query_year_2014,
            "2015": db_config.query_year_2015,
            "2016": db_config.query_year_2016,
            "2017": db_config.query_year_2017,
            "2018": db_config.query_year_2018,
            "2019": db_config.query_year_2019,
            "2020": db_config.query_year_2020,
            "2021": db_config.query_year_2021,
            "2022": db_config.query_year_2022,
            "2023": db_config.query_year_2023,
            "2024": db_config.query_year_2024,
            "usa": db_config.query_country_usa,
            "spain": db_config.query_country_spain,
            "japan": db_config.query_country_japan
        }

        query_function = category_to_query.get(category)
        if query_function:
            return query_function(limit, offset)
        else:
            return None

    def next_page(self):
        if self.is_search_active:
            if self.current_search_query:
                self.current_offset += self.current_limit
                query = self.get_search_query(self.current_search_query, self.current_search_category, self.current_limit, self.current_offset)
                self.search_in_database(self.current_search_query, query)
        else:
            if self.last_clicked_button:
                self.current_offset += self.current_limit
                query = self.get_category_query(self.last_clicked_button, self.current_limit, self.current_offset)
                self.print_films_by_year(query, "others")

    def prev_page(self):
        if self.is_search_active:
            if self.current_offset > 0 and self.current_search_query:
                self.current_offset -= self.current_limit
                query = self.get_search_query(self.current_search_query, self.current_search_category, self.current_limit, self.current_offset)
                self.search_in_database(self.current_search_query, query)
        else:
            if self.current_offset > 0 and self.last_clicked_button:
                self.current_offset -= self.current_limit
                query = self.get_category_query(self.last_clicked_button, self.current_limit, self.current_offset)
                self.print_films_by_year(query, "others")

    # управление чекбоксами
    def setup_checkbox_group(self):
        self.checkbox_group = QButtonGroup(self)
        self.checkbox_group.setExclusive(True)
        self.checkbox_group.addButton(self.ui.byFilms)
        self.checkbox_group.addButton(self.ui.byActors)
        self.checkbox_group.addButton(self.ui.byDirectors)

    # Логика для окна поиска и CeckBox
    def perform_search(self):
        self.is_search_active = True
        search_text = self.ui.searchMethod.text().strip()
        if not search_text:
            QMessageBox.information(self, "Поиск", "Введите текст для поиска.")
            return

        self.current_search_query = search_text
        self.current_offset = 0

        if self.ui.byFilms.isChecked():
            self.current_search_category = 'by_film'
        elif self.ui.byActors.isChecked():
            self.current_search_category = 'by_actors'
        elif self.ui.byDirectors.isChecked():
            self.current_search_category = 'by_directors'
        else:
            self.current_search_category = 'by_film'

        query = self.get_search_query(self.current_search_query, self.current_search_category, self.current_limit,
                                      self.current_offset)
        self.search_in_database(search_text, query)
        self.record_search_query(search_text, self.current_search_category)

        self.ui.searchMethod.clear()
        self.ui.serachCloseBtn.click()

    def get_search_query(self, search_text, category, limit, offset):
        if category == 'by_film':
            return db_config.query_film_search_user(search_text, limit, offset)
        elif category == 'by_actors':
            return db_config.query_actor_search_user(search_text, limit, offset)
        elif category == 'by_directors':
            return db_config.query_director_search_user(search_text, limit, offset)

    def search_in_database(self, search_text, query):
        params = (f"%{search_text}%",)
        results, column_names = execute_query(query, params)

        if not results:
            QMessageBox.information(self, "Поиск", "Ничего не найдено.")
            return

        self.ui.mainPrint.clear()
        index = 0
        if 'film_name' in column_names:
            for result in results:
                film_info = dict(zip(column_names, result))
                film_text = f"{film_info['film_name']}, Страна: {film_info['country']}, Рейтинг: {film_info['rating']}, Продолжительность: {film_info['duration']} - Жанры: {film_info['genres']}"
                item = QListWidgetItem(film_text)
                self.ui.mainPrint.addItem(item)
                self.list_items[index] = item

                if film_info.get('downloaded_img'):
                    image_path = os.path.abspath(film_info['downloaded_img'])
                    if os.path.exists(image_path):
                        pixmap = QPixmap(image_path)
                        item.setIcon(QIcon(pixmap))
                index += 1
        else:
            for result in results:
                item_text = ', '.join(str(value) for value in result)
                item = QListWidgetItem(item_text)
                self.ui.mainPrint.addItem(item)
                self.list_items[index] = item
                index += 1

    def print_films_by_year(self, query, year_description):
        results = Media.get_by_query(query)
        self.last_query_count = len(results)
        self.current_year_query = query
        self.ui.mainPrint.clear()
        index = 0
        for film in results:
            film_info = film.to_dict()
            film_text = f"{film_info['film_name']}, Страна: {film_info['country']}, Рейтинг: {film_info['rating']}, Продолжительность: {film_info['duration']} - Жанры: {film_info['genres']}"
            item = QListWidgetItem(film_text)
            self.ui.mainPrint.addItem(item)
            self.list_items[index] = item
            if film_info['downloaded_img']:
                pixmap = QPixmap(film_info['downloaded_img'])
                if not pixmap.isNull():
                    item.setIcon(QIcon(pixmap))
            index += 1

    def on_image_loaded(self, reply):
        data = reply.readAll()
        pixmap = QPixmap()
        success = pixmap.loadFromData(data)
        if success:
            index = self.pending_image_loads.pop(reply, None)
            if index is not None and index in self.list_items:
                item = self.list_items[index]
                if item and self.ui.mainPrint.item(self.ui.mainPrint.row(item)):
                    item.setIcon(QIcon(pixmap))
                del self.list_items[index]
        reply.deleteLater()

    def print_actors_directors(self, query, category):
        results = Media.get_by_query(query)
        self.ui.mainPrint.clear()
        for media_object in results:
            name = getattr(media_object, category + '_name', 'Unknown')
            item = QListWidgetItem(name)
            self.ui.mainPrint.addItem(item)



    def display_results(self, query):
        results = Media.get_by_query(query)
        self.ui.mainPrint.clear()
        for actor in results:
            item = QListWidgetItem(actor.name)
            self.ui.mainPrint.addItem(item)

    def update_limit(self):
        text = self.ui.limitBox.text()
        if text:
            try:
                new_limit = int(text)
                db_config.LIMIT = new_limit
                self.ui.limitBox.setText(str(db_config.LIMIT))
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Нужно ввести число!")
                self.ui.limitBox.setText(str(db_config.LIMIT))
        else:
            QMessageBox.warning(self, "Ошибка", "Нужно ввести число!")
            self.ui.limitBox.setText(str(db_config.LIMIT))

    ########################################################################
    # Переход по ссылке
    ########################################################################
    def on_item_clicked(self, item):
        film_name = item.text().split(',')[0]
        self.display_film_info(film_name)


    ########################################################################
    # Вывод самой конечной информации, полная информация о фильме
    ########################################################################

    def display_film_info(self, film_name):
        query = db_config.query_film_link(film_name)
        results = Media.get_by_query(query)
        if results:
            self.ui.mainPrint.clear()
            for film in results:
                film_info = film.to_dict()
                film_text = (f"                                                                          {film_info['film_name']}\n     Год: {film_info['year']}\n     Страна: {film_info['country']}"
                             f"\n     Рейтинг: {film_info['rating']}\n     Продолжительность: {film_info['duration']}"
                             f"\n     Актеры: {film_info['actors_names']}\n     Режжистер: {film_info['directors_names']}\n     Жарны: {film_info['genres']}")
                item = QListWidgetItem(film_text)
                self.ui.mainPrint.addItem(item)
                index = self.ui.mainPrint.row(item)
                self.list_items[index] = item
                if film_info['downloaded_img']:
                    image_path = os.path.abspath(film_info['downloaded_img'])
                    if os.path.exists(image_path):
                        pixmap = QPixmap(image_path)
                        item.setIcon(QIcon(pixmap))


    ########################################################################
    # Вывод запросов из search_frequency
    ########################################################################
    def record_search_query(self, search_text, category):
        connection = None
        cursor = None
        try:
            connection = get_connection_search()
            if connection is None:
                return

            cursor = connection.cursor()
            check_query = f"SELECT id, frequency FROM search_frequency WHERE {category} = %s;"
            cursor.execute(check_query, (search_text,))
            result = cursor.fetchone()

            if result:
                id, frequency = result
                frequency += 1
                update_query = f"UPDATE search_frequency SET frequency = %s WHERE id = %s;"
                cursor.execute(update_query, (frequency, id))
            else:
                insert_query = f"INSERT INTO search_frequency ({category}, frequency) VALUES (%s, 1);"
                cursor.execute(insert_query, (search_text,))

            connection.commit()
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()


class SearchDisplayManager:
    def __init__(self, ui):
        self.ui = ui

    def display_top_searches(self, category):
        if category not in ['by_film', 'by_actors', 'by_directors']:
            QMessageBox.warning(self.ui, "Ошибка", "Неверная категория поиска.")
            return

        query = f"SELECT {category}, frequency FROM search_frequency WHERE {category} IS NOT NULL ORDER BY frequency DESC LIMIT 11;"
        results, _ = execute_query_search(query)

        self.ui.searchDbResults.clear()
        for result in results:
            search_query = result[0]
            frequency = result[1]
            self.ui.searchDbResults.addItem(f"{search_query} - Частота: {frequency}")

    def update_search_category(self):
        if not any([self.ui.byFilms.isChecked(), self.ui.byActors.isChecked(), self.ui.byDirectors.isChecked()]):
            self.ui.byFilms.setChecked(True)

        if self.ui.byFilms.isChecked():
            self.display_top_searches('by_film')
        elif self.ui.byActors.isChecked():
            self.display_top_searches('by_actors')
        elif self.ui.byDirectors.isChecked():
            self.display_top_searches('by_directors')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
