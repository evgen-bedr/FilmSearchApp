# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1339, 788)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:white;\n"
"\n"
"}\n"
"#centralwidget {\n"
"	background-color: #1f232a;\n"
"\n"
"}\n"
"\n"
"#mainPrint {\n"
"	font-size: 18px;\n"
"	padding-left:5px;\n"
"	padding-top:10px;\n"
"	padding-right:10px;\n"
"	\n"
"}\n"
"\n"
"#lineEdit {\n"
"	background-color: #16191d;\n"
"	color:white;\n"
"	font-size: 16px;\n"
"	border-radius:7px;\n"
"	font-weight:bold;\n"
"	margin-right:11px;\n"
"	padding-left:7px;\n"
"	\n"
"}\n"
"\n"
"\n"
"#MenuCategories {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#MenuCategories QPushButton {\n"
"	color:white;\n"
"	font-size: 16px;\n"
"	text-align:left;\n"
"	padding:2px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	\n"
"}\n"
"\n"
"#mainPrint {\n"
"	color:white;\n"
"	font-size: 16px;\n"
"	padding-bottom: 10px;\n"
"}\n"
"\n"
"#centralMenuSubContainer {\n"
"	background-color: #2c313c;\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"\n"
"\n"
""
                        "#frame_3, #popupSearchSubContainer{\n"
"	background-color: #16191d;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#headerContainer, #mainBodyContainer_2{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#searchMethod {\n"
"	background-color: #16191d;\n"
"	color:white;\n"
"	font-size: 16px;\n"
"	border-radius:10px;\n"
"	padding-left: 5px;\n"
"}\n"
"#popupSearchSubContainer {\n"
"	background-color: #2c313c;\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"\n"
"#searchDbResults{\n"
"	font-size: 16px;\n"
"	color:white;\n"
"	padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#year_2024, QPushButton#year_2023, QPushButton#year_2022, QPushButton#year_2021\n"
", QPushButton#year_2020, QPushButton#year_2019, QPushButton#year_2018, QPushButton#year_2017\n"
", QPushButton#year_2016, QPushButton#year_2015, QPushButton#year_2014, QPushButton#year_others, QPushButton#byFilmButton, QPushButton#serialsButton\n"
", QPushButton#lowestRateButton, QPushButton#topButton, QPushButton#countryButton, QPushButton#country1, QPushButton#count"
                        "ry2, QPushButton#country3, QPushButton#actorButton, QPushButton#directorButton {\n"
"    background-color: #16191d;\n"
"    border-radius: 10px;  \n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#year_2024:hover, QPushButton#year_2023:hover, QPushButton#year_2022:hover\n"
", QPushButton#year_2021:hover, QPushButton#year_2020:hover, QPushButton#year_2019:hover, QPushButton#year_2018:hover, QPushButton#year_2017:hover, QPushButton#year_2016:hover, QPushButton#year_2015:hover, QPushButton#year_2014:hover, QPushButton#year_others:hover,\n"
"QPushButton#byFilmButton:hover, QPushButton#serialsButton:hover\n"
", QPushButton#lowestRateButton:hover, QPushButton#topButton:hover, QPushButton#countryButton:hover, QPushButton#country1:hover, QPushButton#country2:hover, QPushButton#country3:hover, QPushButton#actorButton:hover, QPushButton#directorButton:hover {\n"
"    background-color: #808080;\n"
"}\n"
"\n"
"QPushButton#genre1, QPushButton#genre2, QPushButton#genre3, QPushButton#genre4, QPushButton#genre5, QPushBu"
                        "tton#genre6,\n"
"QPushButton#genre7, QPushButton#genre8, QPushButton#genre9,\n"
"QPushButton#genre10 {\n"
"    background-color: #16191d;\n"
"    border-radius: 10px;  \n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#genre1:hover, QPushButton#genre2:hover, QPushButton#genre3:hover, QPushButton#genre4:hover, QPushButton#genre5:hover, QPushButton#genre6:hover,\n"
"QPushButton#genre7:hover, QPushButton#genre8:hover, QPushButton#genre9:hover,\n"
"QPushButton#genre10:hover {\n"
"    background-color: #808080;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#QPushButton.yearButton {\n"
"    background-color: #16191d;\n"
"    border-radius: 10px;  \n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"#QPushButton.yearButton:hover {\n"
"    background-color: #808080;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(65, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuCategories = QWidget(self.leftMenuContainer)
        self.MenuCategories.setObjectName(u"MenuCategories")
        self.MenuCategories.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.MenuCategories)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.MenuCategories)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.homeBtn.setMouseTracking(True)
        self.homeBtn.setFocusPolicy(Qt.StrongFocus)
        self.homeBtn.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home_ww.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.homeBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.MenuCategories)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(18)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.filmsBtn = QPushButton(self.frame_2)
        self.filmsBtn.setObjectName(u"filmsBtn")
        self.filmsBtn.setFont(font)
        self.filmsBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.filmsBtn.setMouseTracking(True)
        self.filmsBtn.setFocusPolicy(Qt.StrongFocus)
        self.filmsBtn.setLayoutDirection(Qt.LeftToRight)
        self.filmsBtn.setAutoFillBackground(False)
        self.filmsBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/film_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.filmsBtn.setIcon(icon1)
        self.filmsBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.filmsBtn)

        self.tvseriesBtn = QPushButton(self.frame_2)
        self.tvseriesBtn.setObjectName(u"tvseriesBtn")
        self.tvseriesBtn.setFont(font)
        self.tvseriesBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.tvseriesBtn.setMouseTracking(True)
        self.tvseriesBtn.setFocusPolicy(Qt.StrongFocus)
        self.tvseriesBtn.setAutoFillBackground(False)
        self.tvseriesBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/serial_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tvseriesBtn.setIcon(icon2)
        self.tvseriesBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.tvseriesBtn)

        self.topBtn = QPushButton(self.frame_2)
        self.topBtn.setObjectName(u"topBtn")
        self.topBtn.setFont(font)
        self.topBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.topBtn.setMouseTracking(True)
        self.topBtn.setFocusPolicy(Qt.StrongFocus)
        self.topBtn.setLayoutDirection(Qt.LeftToRight)
        self.topBtn.setAutoFillBackground(False)
        self.topBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/top_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.topBtn.setIcon(icon3)
        self.topBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.topBtn)

        self.genresBtn = QPushButton(self.frame_2)
        self.genresBtn.setObjectName(u"genresBtn")
        self.genresBtn.setFont(font)
        self.genresBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.genresBtn.setMouseTracking(True)
        self.genresBtn.setFocusPolicy(Qt.StrongFocus)
        self.genresBtn.setLayoutDirection(Qt.LeftToRight)
        self.genresBtn.setAutoFillBackground(False)
        self.genresBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/genre_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.genresBtn.setIcon(icon4)
        self.genresBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.genresBtn)

        self.yearBtn = QPushButton(self.frame_2)
        self.yearBtn.setObjectName(u"yearBtn")
        self.yearBtn.setFont(font)
        self.yearBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.yearBtn.setMouseTracking(True)
        self.yearBtn.setFocusPolicy(Qt.StrongFocus)
        self.yearBtn.setLayoutDirection(Qt.LeftToRight)
        self.yearBtn.setAutoFillBackground(False)
        self.yearBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/year_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yearBtn.setIcon(icon5)
        self.yearBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.yearBtn)

        self.countriesBtn = QPushButton(self.frame_2)
        self.countriesBtn.setObjectName(u"countriesBtn")
        self.countriesBtn.setFont(font)
        self.countriesBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.countriesBtn.setMouseTracking(True)
        self.countriesBtn.setFocusPolicy(Qt.StrongFocus)
        self.countriesBtn.setAutoFillBackground(False)
        self.countriesBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/Earth_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.countriesBtn.setIcon(icon6)
        self.countriesBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.countriesBtn)

        self.actorsBtn = QPushButton(self.frame_2)
        self.actorsBtn.setObjectName(u"actorsBtn")
        self.actorsBtn.setFont(font)
        self.actorsBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.actorsBtn.setMouseTracking(True)
        self.actorsBtn.setFocusPolicy(Qt.StrongFocus)
        self.actorsBtn.setAutoFillBackground(False)
        self.actorsBtn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/actors_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actorsBtn.setIcon(icon7)
        self.actorsBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.actorsBtn)

        self.directorsBtn = QPushButton(self.frame_2)
        self.directorsBtn.setObjectName(u"directorsBtn")
        self.directorsBtn.setFont(font)
        self.directorsBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.directorsBtn.setMouseTracking(True)
        self.directorsBtn.setFocusPolicy(Qt.StrongFocus)
        self.directorsBtn.setAutoFillBackground(False)
        self.directorsBtn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/director_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.directorsBtn.setIcon(icon8)
        self.directorsBtn.setIconSize(QSize(38, 38))

        self.verticalLayout_3.addWidget(self.directorsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.MenuCategories)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.MenuCategories)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.verticalLayout_4 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.centralMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centralMenuSubContainer.setObjectName(u"centralMenuSubContainer")
        self.centralMenuSubContainer.setMinimumSize(QSize(150, 0))
        self.centralMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centralMenuSubContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"#label_2 {\n"
"	color:white;\n"
"	font-size: 16px;\n"
"	font-weight:bold;\n"
"}")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.closeCentralMenu = QPushButton(self.frame_3)
        self.closeCentralMenu.setObjectName(u"closeCentralMenu")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCentralMenu.setIcon(icon9)
        self.closeCentralMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeCentralMenu, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.menuPages = QCustomQStackedWidget(self.centralMenuSubContainer)
        self.menuPages.setObjectName(u"menuPages")
        sizePolicy.setHeightForWidth(self.menuPages.sizePolicy().hasHeightForWidth())
        self.menuPages.setSizePolicy(sizePolicy)
        self.menuPages.setStyleSheet(u"font-size: 16px;\n"
"font-weight:bold;")
        self.filmsMenu = QWidget()
        self.filmsMenu.setObjectName(u"filmsMenu")
        self.verticalLayout_19 = QVBoxLayout(self.filmsMenu)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_6 = QLabel(self.filmsMenu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 30))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_6)

        self.widget_7 = QWidget(self.filmsMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_18 = QVBoxLayout(self.widget_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.byFilmButton = QPushButton(self.widget_7)
        self.byFilmButton.setObjectName(u"byFilmButton")

        self.verticalLayout_18.addWidget(self.byFilmButton)


        self.verticalLayout_19.addWidget(self.widget_7, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.filmsMenu)
        self.serialsMenu = QWidget()
        self.serialsMenu.setObjectName(u"serialsMenu")
        self.verticalLayout_15 = QVBoxLayout(self.serialsMenu)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.serialsMenu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 30))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)

        self.widget_6 = QWidget(self.serialsMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_17 = QVBoxLayout(self.widget_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.serialsButton = QPushButton(self.widget_6)
        self.serialsButton.setObjectName(u"serialsButton")

        self.verticalLayout_17.addWidget(self.serialsButton)


        self.verticalLayout_15.addWidget(self.widget_6, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.serialsMenu)
        self.topFilmMenu = QWidget()
        self.topFilmMenu.setObjectName(u"topFilmMenu")
        self.verticalLayout_16 = QVBoxLayout(self.topFilmMenu)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.topFilmMenu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 30))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_4)

        self.topButton = QPushButton(self.topFilmMenu)
        self.topButton.setObjectName(u"topButton")

        self.verticalLayout_16.addWidget(self.topButton)

        self.lowestRateButton = QPushButton(self.topFilmMenu)
        self.lowestRateButton.setObjectName(u"lowestRateButton")

        self.verticalLayout_16.addWidget(self.lowestRateButton)

        self.widget_5 = QWidget(self.topFilmMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.verticalLayout_16.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.topFilmMenu)
        self.genresMenu = QWidget()
        self.genresMenu.setObjectName(u"genresMenu")
        self.verticalLayout_13 = QVBoxLayout(self.genresMenu)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.genresMenu)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(200, 30))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)

        self.verticalLayout_13.addWidget(self.label_3)

        self.genresMenuBtn = QWidget(self.genresMenu)
        self.genresMenuBtn.setObjectName(u"genresMenuBtn")
        self.verticalLayout_12 = QVBoxLayout(self.genresMenuBtn)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.genre1 = QPushButton(self.genresMenuBtn)
        self.genre1.setObjectName(u"genre1")
        self.genre1.setStyleSheet(u"yearButton")

        self.verticalLayout_12.addWidget(self.genre1)

        self.genre2 = QPushButton(self.genresMenuBtn)
        self.genre2.setObjectName(u"genre2")
        self.genre2.setStyleSheet(u"yearButton")

        self.verticalLayout_12.addWidget(self.genre2)

        self.genre3 = QPushButton(self.genresMenuBtn)
        self.genre3.setObjectName(u"genre3")
        self.genre3.setStyleSheet(u"yearButton")

        self.verticalLayout_12.addWidget(self.genre3)

        self.genre4 = QPushButton(self.genresMenuBtn)
        self.genre4.setObjectName(u"genre4")

        self.verticalLayout_12.addWidget(self.genre4)

        self.genre5 = QPushButton(self.genresMenuBtn)
        self.genre5.setObjectName(u"genre5")

        self.verticalLayout_12.addWidget(self.genre5)

        self.genre6 = QPushButton(self.genresMenuBtn)
        self.genre6.setObjectName(u"genre6")

        self.verticalLayout_12.addWidget(self.genre6)

        self.genre7 = QPushButton(self.genresMenuBtn)
        self.genre7.setObjectName(u"genre7")

        self.verticalLayout_12.addWidget(self.genre7)

        self.genre8 = QPushButton(self.genresMenuBtn)
        self.genre8.setObjectName(u"genre8")

        self.verticalLayout_12.addWidget(self.genre8)

        self.genre9 = QPushButton(self.genresMenuBtn)
        self.genre9.setObjectName(u"genre9")

        self.verticalLayout_12.addWidget(self.genre9)

        self.genre10 = QPushButton(self.genresMenuBtn)
        self.genre10.setObjectName(u"genre10")

        self.verticalLayout_12.addWidget(self.genre10)


        self.verticalLayout_13.addWidget(self.genresMenuBtn, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.genresMenu)
        self.yearMenu = QWidget()
        self.yearMenu.setObjectName(u"yearMenu")
        self.verticalLayout_6 = QVBoxLayout(self.yearMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.yearMenu)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(200, 30))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label)

        self.yearMenuBtn = QWidget(self.yearMenu)
        self.yearMenuBtn.setObjectName(u"yearMenuBtn")
        self.verticalLayout_11 = QVBoxLayout(self.yearMenuBtn)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.year_2024 = QPushButton(self.yearMenuBtn)
        self.year_2024.setObjectName(u"year_2024")
        self.year_2024.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2024)

        self.year_2023 = QPushButton(self.yearMenuBtn)
        self.year_2023.setObjectName(u"year_2023")
        self.year_2023.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2023)

        self.year_2022 = QPushButton(self.yearMenuBtn)
        self.year_2022.setObjectName(u"year_2022")
        self.year_2022.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2022)

        self.year_2021 = QPushButton(self.yearMenuBtn)
        self.year_2021.setObjectName(u"year_2021")
        self.year_2021.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2021)

        self.year_2020 = QPushButton(self.yearMenuBtn)
        self.year_2020.setObjectName(u"year_2020")
        self.year_2020.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2020)

        self.year_2019 = QPushButton(self.yearMenuBtn)
        self.year_2019.setObjectName(u"year_2019")
        self.year_2019.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2019)

        self.year_2018 = QPushButton(self.yearMenuBtn)
        self.year_2018.setObjectName(u"year_2018")
        self.year_2018.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2018)

        self.year_2017 = QPushButton(self.yearMenuBtn)
        self.year_2017.setObjectName(u"year_2017")
        self.year_2017.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2017)

        self.year_2016 = QPushButton(self.yearMenuBtn)
        self.year_2016.setObjectName(u"year_2016")
        self.year_2016.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2016)

        self.year_2015 = QPushButton(self.yearMenuBtn)
        self.year_2015.setObjectName(u"year_2015")
        self.year_2015.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2015)

        self.year_2014 = QPushButton(self.yearMenuBtn)
        self.year_2014.setObjectName(u"year_2014")
        self.year_2014.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_2014)

        self.year_others = QPushButton(self.yearMenuBtn)
        self.year_others.setObjectName(u"year_others")
        self.year_others.setStyleSheet(u"yearButton")

        self.verticalLayout_11.addWidget(self.year_others)


        self.verticalLayout_6.addWidget(self.yearMenuBtn, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.yearMenu)
        self.countryMenu = QWidget()
        self.countryMenu.setObjectName(u"countryMenu")
        self.verticalLayout_20 = QVBoxLayout(self.countryMenu)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_7 = QLabel(self.countryMenu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(200, 30))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_7)

        self.widget_8 = QWidget(self.countryMenu)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_21 = QVBoxLayout(self.widget_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.country1 = QPushButton(self.widget_8)
        self.country1.setObjectName(u"country1")

        self.verticalLayout_21.addWidget(self.country1)

        self.country2 = QPushButton(self.widget_8)
        self.country2.setObjectName(u"country2")

        self.verticalLayout_21.addWidget(self.country2)

        self.country3 = QPushButton(self.widget_8)
        self.country3.setObjectName(u"country3")

        self.verticalLayout_21.addWidget(self.country3)


        self.verticalLayout_20.addWidget(self.widget_8, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.countryMenu)
        self.actorsMenu = QWidget()
        self.actorsMenu.setObjectName(u"actorsMenu")
        self.verticalLayout_22 = QVBoxLayout(self.actorsMenu)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_8 = QLabel(self.actorsMenu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(200, 30))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_8)

        self.widget_9 = QWidget(self.actorsMenu)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_23 = QVBoxLayout(self.widget_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.actorButton = QPushButton(self.widget_9)
        self.actorButton.setObjectName(u"actorButton")

        self.verticalLayout_23.addWidget(self.actorButton)


        self.verticalLayout_22.addWidget(self.widget_9, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.actorsMenu)
        self.directorMenu = QWidget()
        self.directorMenu.setObjectName(u"directorMenu")
        self.verticalLayout_24 = QVBoxLayout(self.directorMenu)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_9 = QLabel(self.directorMenu)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(200, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_9)

        self.widget_10 = QWidget(self.directorMenu)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_25 = QVBoxLayout(self.widget_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.directorButton = QPushButton(self.widget_10)
        self.directorButton.setObjectName(u"directorButton")

        self.verticalLayout_25.addWidget(self.directorButton)


        self.verticalLayout_24.addWidget(self.widget_10, 0, Qt.AlignTop)

        self.menuPages.addWidget(self.directorMenu)

        self.verticalLayout_5.addWidget(self.menuPages)


        self.verticalLayout_4.addWidget(self.centralMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.limitInput = QFrame(self.headerContainer)
        self.limitInput.setObjectName(u"limitInput")
        self.limitInput.setFrameShape(QFrame.StyledPanel)
        self.limitInput.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.limitInput)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.limitBox = QLineEdit(self.limitInput)
        self.limitBox.setObjectName(u"limitBox")
        self.limitBox.setMinimumSize(QSize(51, 20))
        self.limitBox.setMaximumSize(QSize(51, 20))

        self.horizontalLayout_7.addWidget(self.limitBox)

        self.searchMainPushBtn = QPushButton(self.limitInput)
        self.searchMainPushBtn.setObjectName(u"searchMainPushBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchMainPushBtn.setIcon(icon10)
        self.searchMainPushBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.searchMainPushBtn)


        self.horizontalLayout_6.addWidget(self.limitInput, 0, Qt.AlignRight)

        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_6.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerContainer)

        self.popupSearchContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupSearchContainer.setObjectName(u"popupSearchContainer")
        sizePolicy.setHeightForWidth(self.popupSearchContainer.sizePolicy().hasHeightForWidth())
        self.popupSearchContainer.setSizePolicy(sizePolicy)
        self.popupSearchContainer.setMaximumSize(QSize(500, 400))
        self.verticalLayout_9 = QVBoxLayout(self.popupSearchContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.popupSearchSubContainer = QWidget(self.popupSearchContainer)
        self.popupSearchSubContainer.setObjectName(u"popupSearchSubContainer")
        self.verticalLayout_10 = QVBoxLayout(self.popupSearchSubContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.popupSearchSubContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.searchMethod = QLineEdit(self.widget_3)
        self.searchMethod.setObjectName(u"searchMethod")
        sizePolicy.setHeightForWidth(self.searchMethod.sizePolicy().hasHeightForWidth())
        self.searchMethod.setSizePolicy(sizePolicy)
        self.searchMethod.setMinimumSize(QSize(300, 26))

        self.horizontalLayout_3.addWidget(self.searchMethod)

        self.searchPushBtn = QPushButton(self.widget_3)
        self.searchPushBtn.setObjectName(u"searchPushBtn")
        self.searchPushBtn.setIcon(icon10)
        self.searchPushBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.searchPushBtn, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.serachCloseBtn = QPushButton(self.widget_3)
        self.serachCloseBtn.setObjectName(u"serachCloseBtn")
        self.serachCloseBtn.setIcon(icon9)
        self.serachCloseBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.serachCloseBtn)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.popupSearchSubContainer)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 60, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.byFilms = QCheckBox(self.widget_4)
        self.byFilms.setObjectName(u"byFilms")

        self.horizontalLayout_9.addWidget(self.byFilms)

        self.byActors = QCheckBox(self.widget_4)
        self.byActors.setObjectName(u"byActors")

        self.horizontalLayout_9.addWidget(self.byActors)

        self.byDirectors = QCheckBox(self.widget_4)
        self.byDirectors.setObjectName(u"byDirectors")

        self.horizontalLayout_9.addWidget(self.byDirectors)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.searchDbResults = QListWidget(self.popupSearchSubContainer)
        self.searchDbResults.setObjectName(u"searchDbResults")
        self.searchDbResults.setMinimumSize(QSize(0, 0))
        self.searchDbResults.setFont(font)

        self.verticalLayout_10.addWidget(self.searchDbResults)


        self.verticalLayout_9.addWidget(self.popupSearchSubContainer)


        self.verticalLayout_7.addWidget(self.popupSearchContainer)

        self.mainPrint = QListWidget(self.mainBodyContainer)
        self.mainPrint.setObjectName(u"mainPrint")
        self.mainPrint.setFont(font)
        self.mainPrint.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.mainPrint.setIconSize(QSize(140, 210))
        self.mainPrint.setMovement(QListView.Static)
        self.mainPrint.setResizeMode(QListView.Fixed)
        self.mainPrint.setSpacing(5)

        self.verticalLayout_7.addWidget(self.mainPrint)

        self.mainBodyContainer_2 = QWidget(self.mainBodyContainer)
        self.mainBodyContainer_2.setObjectName(u"mainBodyContainer_2")
        self.mainBodyContainer_2.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.mainBodyContainer_2)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.widget = QWidget(self.mainBodyContainer_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.previousButton = QPushButton(self.widget)
        self.previousButton.setObjectName(u"previousButton")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon14)
        self.previousButton.setIconSize(QSize(34, 34))

        self.horizontalLayout_10.addWidget(self.previousButton, 0, Qt.AlignRight)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.nextButton = QPushButton(self.widget)
        self.nextButton.setObjectName(u"nextButton")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon15)
        self.nextButton.setIconSize(QSize(34, 34))

        self.horizontalLayout_10.addWidget(self.nextButton, 0, Qt.AlignLeft)

        self.sizeGrip = QFrame(self.widget)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 20))
        self.sizeGrip.setMaximumSize(QSize(40, 40))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.sizeGrip)


        self.verticalLayout_8.addWidget(self.widget)

        self.footerScroll = QWidget(self.mainBodyContainer_2)
        self.footerScroll.setObjectName(u"footerScroll")
        self.horizontalLayout_8 = QHBoxLayout(self.footerScroll)
        self.horizontalLayout_8.setSpacing(26)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.footerScroll, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.mainBodyContainer_2)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menuPages.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.filmsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Films", None))
#endif // QT_CONFIG(tooltip)
        self.filmsBtn.setText(QCoreApplication.translate("MainWindow", u"Films", None))
#if QT_CONFIG(tooltip)
        self.tvseriesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"TV series", None))
#endif // QT_CONFIG(tooltip)
        self.tvseriesBtn.setText(QCoreApplication.translate("MainWindow", u"TV series", None))
#if QT_CONFIG(tooltip)
        self.topBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Top", None))
#endif // QT_CONFIG(tooltip)
        self.topBtn.setText(QCoreApplication.translate("MainWindow", u"Top", None))
#if QT_CONFIG(tooltip)
        self.genresBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Genres", None))
#endif // QT_CONFIG(tooltip)
        self.genresBtn.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
#if QT_CONFIG(tooltip)
        self.yearBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Year", None))
#endif // QT_CONFIG(tooltip)
        self.yearBtn.setText(QCoreApplication.translate("MainWindow", u"Year", None))
#if QT_CONFIG(tooltip)
        self.countriesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Countries", None))
#endif // QT_CONFIG(tooltip)
        self.countriesBtn.setText(QCoreApplication.translate("MainWindow", u"Countries", None))
#if QT_CONFIG(tooltip)
        self.actorsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Actors", None))
#endif // QT_CONFIG(tooltip)
        self.actorsBtn.setText(QCoreApplication.translate("MainWindow", u"Actors", None))
#if QT_CONFIG(tooltip)
        self.directorsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Directors", None))
#endif // QT_CONFIG(tooltip)
        self.directorsBtn.setText(QCoreApplication.translate("MainWindow", u"Directors", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.closeCentralMenu.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Films", None))
        self.byFilmButton.setText(QCoreApplication.translate("MainWindow", u"by Films", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TV series", None))
        self.serialsButton.setText(QCoreApplication.translate("MainWindow", u"by Series", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Top Films", None))
        self.topButton.setText(QCoreApplication.translate("MainWindow", u"Top rated", None))
        self.lowestRateButton.setText(QCoreApplication.translate("MainWindow", u"Lowest rated", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
        self.genre1.setText(QCoreApplication.translate("MainWindow", u"Comedy", None))
        self.genre2.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.genre3.setText(QCoreApplication.translate("MainWindow", u"Detective", None))
        self.genre4.setText(QCoreApplication.translate("MainWindow", u"Drama", None))
        self.genre5.setText(QCoreApplication.translate("MainWindow", u"Crime", None))
        self.genre6.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.genre7.setText(QCoreApplication.translate("MainWindow", u"Horror", None))
        self.genre8.setText(QCoreApplication.translate("MainWindow", u"Fantasy", None))
        self.genre9.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.genre10.setText(QCoreApplication.translate("MainWindow", u"Cartoons", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.year_2024.setText(QCoreApplication.translate("MainWindow", u"2024", None))
        self.year_2023.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.year_2022.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.year_2021.setText(QCoreApplication.translate("MainWindow", u"2021", None))
        self.year_2020.setText(QCoreApplication.translate("MainWindow", u"2020", None))
        self.year_2019.setText(QCoreApplication.translate("MainWindow", u"2019", None))
        self.year_2018.setText(QCoreApplication.translate("MainWindow", u"2018", None))
        self.year_2017.setText(QCoreApplication.translate("MainWindow", u"2017", None))
        self.year_2016.setText(QCoreApplication.translate("MainWindow", u"2016", None))
        self.year_2015.setText(QCoreApplication.translate("MainWindow", u"2015", None))
        self.year_2014.setText(QCoreApplication.translate("MainWindow", u"2014", None))
        self.year_others.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Countries", None))
        self.country1.setText(QCoreApplication.translate("MainWindow", u"USA", None))
        self.country2.setText(QCoreApplication.translate("MainWindow", u"Spain", None))
        self.country3.setText(QCoreApplication.translate("MainWindow", u"Japan", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Actors", None))
        self.actorButton.setText(QCoreApplication.translate("MainWindow", u"All actors", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Directors", None))
        self.directorButton.setText(QCoreApplication.translate("MainWindow", u"All directors", None))
#if QT_CONFIG(tooltip)
        self.mainBodyContainer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.limitBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10", None))
        self.searchMainPushBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.searchMethod.setText("")
        self.searchMethod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        self.searchPushBtn.setText("")
#if QT_CONFIG(tooltip)
        self.serachCloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close seatch", None))
#endif // QT_CONFIG(tooltip)
        self.serachCloseBtn.setText("")
        self.byFilms.setText(QCoreApplication.translate("MainWindow", u"films", None))
        self.byActors.setText(QCoreApplication.translate("MainWindow", u"actors", None))
        self.byDirectors.setText(QCoreApplication.translate("MainWindow", u"directors", None))
        self.previousButton.setText("")
        self.nextButton.setText("")
    # retranslateUi

