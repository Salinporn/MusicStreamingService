# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSplitter, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 765)
        MainWindow.setStyleSheet(u"\n"
"/* general styles */\n"
"\n"
"* {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#sidebar {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#content * {\n"
"	background-color: #111111;\n"
"}\n"
"\n"
"#sidebar QPushButton {\n"
"	font-size: 16px;\n"
"	padding: 14px;\n"
"	text-align: left;\n"
"	border-radius: 5px;\n"
"	color: #dddddd;\n"
"}\n"
"\n"
"#sidebar QPushButton:hover {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#sidebar QPushButton:checked {\n"
"	background-color: #303030;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QToolButton {\n"
"	border: 0;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 10px\n"
"}\n"
"\n"
"/* sidebar styles */\n"
"\n"
"#thumbnail {\n"
"	background-color: #111111;\n"
"}\n"
"\n"
"\n"
"/* home page styles */\n"
"\n"
"#home_page #home_page_scrollarea_contents > QWidget {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"}	\n"
"\n"
"/* browse page styles */\n"
"#search_bar, #recent_searches_widget {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"}\n"
"\n"
"/* profile page styles */\n"
"#use"
                        "r_profile_button {\n"
"	font-size: 18px;\n"
"	padding: 4px;\n"
"	text-align: left;\n"
"	color: #dddddd;\n"
"	border: 0;\n"
"}\n"
"\n"
"/* playlist page styles */\n"
"#playlist_contents_scrollarea {\n"
"	border: 1px solid #D0D0D0;\n"
"}")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_7 = QHBoxLayout(self.main_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.main_page)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(280, 0))
        self.sidebar.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.sidebar)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.sidebar_button_area = QWidget(self.sidebar)
        self.sidebar_button_area.setObjectName(u"sidebar_button_area")
        self.verticalLayout_24 = QVBoxLayout(self.sidebar_button_area)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.home_button = QPushButton(self.sidebar_button_area)
        self.home_button.setObjectName(u"home_button")
        font = QFont()
        self.home_button.setFont(font)
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/resources/assets/images/homeNotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/resources/assets/images/home.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(24, 24))
        self.home_button.setCheckable(True)
        self.home_button.setChecked(True)
        self.home_button.setAutoExclusive(True)
        self.home_button.setAutoDefault(False)
        self.home_button.setFlat(False)

        self.verticalLayout_24.addWidget(self.home_button)

        self.browse_button = QPushButton(self.sidebar_button_area)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setFont(font)
        self.browse_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/resources/assets/images/browseNotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/resources/assets/images/browse1.png", QSize(), QIcon.Normal, QIcon.On)
        self.browse_button.setIcon(icon1)
        self.browse_button.setIconSize(QSize(24, 24))
        self.browse_button.setCheckable(True)
        self.browse_button.setChecked(False)
        self.browse_button.setAutoExclusive(True)
        self.browse_button.setFlat(False)

        self.verticalLayout_24.addWidget(self.browse_button)

        self.library_button = QPushButton(self.sidebar_button_area)
        self.library_button.setObjectName(u"library_button")
        self.library_button.setFont(font)
        self.library_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.library_button.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/resources/assets/images/libraryNotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/resources/assets/images/library.png", QSize(), QIcon.Normal, QIcon.On)
        self.library_button.setIcon(icon2)
        self.library_button.setIconSize(QSize(24, 24))
        self.library_button.setCheckable(True)
        self.library_button.setChecked(False)
        self.library_button.setAutoExclusive(True)
        self.library_button.setFlat(False)

        self.verticalLayout_24.addWidget(self.library_button)

        self.profile_button = QPushButton(self.sidebar_button_area)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setFont(font)
        self.profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_button.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/resources/assets/images/person1NotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/resources/assets/images/person1.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_button.setIcon(icon3)
        self.profile_button.setIconSize(QSize(24, 24))
        self.profile_button.setCheckable(True)
        self.profile_button.setChecked(False)
        self.profile_button.setAutoExclusive(True)
        self.profile_button.setFlat(False)

        self.verticalLayout_24.addWidget(self.profile_button)


        self.verticalLayout_23.addWidget(self.sidebar_button_area)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.player_widget = QWidget(self.sidebar)
        self.player_widget.setObjectName(u"player_widget")
        self.player_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_25 = QVBoxLayout(self.player_widget)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(18, 18, 18, 18)
        self.thumbnail = QLabel(self.player_widget)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setMinimumSize(QSize(240, 240))

        self.verticalLayout_25.addWidget(self.thumbnail)

        self.player_song_label = QLabel(self.player_widget)
        self.player_song_label.setObjectName(u"player_song_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.player_song_label.setFont(font1)

        self.verticalLayout_25.addWidget(self.player_song_label)

        self.player_artist_label = QLabel(self.player_widget)
        self.player_artist_label.setObjectName(u"player_artist_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Symbol"])
        font2.setPointSize(10)
        self.player_artist_label.setFont(font2)

        self.verticalLayout_25.addWidget(self.player_artist_label)

        self.player_slider = QSlider(self.player_widget)
        self.player_slider.setObjectName(u"player_slider")
        self.player_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_25.addWidget(self.player_slider)

        self.player_duration_widget = QWidget(self.player_widget)
        self.player_duration_widget.setObjectName(u"player_duration_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.player_duration_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player_startdur_label = QLabel(self.player_duration_widget)
        self.player_startdur_label.setObjectName(u"player_startdur_label")
        self.player_startdur_label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.player_startdur_label)

        self.player_enddur_label = QLabel(self.player_duration_widget)
        self.player_enddur_label.setObjectName(u"player_enddur_label")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Symbol"])
        font3.setPointSize(10)
        font3.setItalic(False)
        self.player_enddur_label.setFont(font3)
        self.player_enddur_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.player_enddur_label)


        self.verticalLayout_25.addWidget(self.player_duration_widget)

        self.playback_controls = QWidget(self.player_widget)
        self.playback_controls.setObjectName(u"playback_controls")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playback_controls.sizePolicy().hasHeightForWidth())
        self.playback_controls.setSizePolicy(sizePolicy)
        self.playback_controls.setMinimumSize(QSize(0, 35))
        self.next_btn = QToolButton(self.playback_controls)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setGeometry(QRect(210, 0, 35, 35))
        icon4 = QIcon()
        icon4.addFile(u":/resources/assets/images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon4)
        self.next_btn.setIconSize(QSize(24, 24))
        self.play_pause_btn = QToolButton(self.playback_controls)
        self.play_pause_btn.setObjectName(u"play_pause_btn")
        self.play_pause_btn.setGeometry(QRect(105, 0, 35, 35))
        icon5 = QIcon()
        icon5.addFile(u":/resources/assets/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/resources/assets/images/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_pause_btn.setIcon(icon5)
        self.play_pause_btn.setIconSize(QSize(24, 24))
        self.play_pause_btn.setCheckable(True)
        self.previous_btn = QToolButton(self.playback_controls)
        self.previous_btn.setObjectName(u"previous_btn")
        self.previous_btn.setGeometry(QRect(0, 0, 35, 35))
        icon6 = QIcon()
        icon6.addFile(u":/resources/assets/images/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_btn.setIcon(icon6)
        self.previous_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_25.addWidget(self.playback_controls)


        self.verticalLayout_23.addWidget(self.player_widget)


        self.horizontalLayout_7.addWidget(self.sidebar)

        self.content = QWidget(self.main_page)
        self.content.setObjectName(u"content")
        self.content.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pages_widget = QStackedWidget(self.content)
        self.pages_widget.setObjectName(u"pages_widget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setEnabled(True)
        self.home_page.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.home_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.home_page_scrollarea = QScrollArea(self.home_page)
        self.home_page_scrollarea.setObjectName(u"home_page_scrollarea")
        self.home_page_scrollarea.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_page_scrollarea.sizePolicy().hasHeightForWidth())
        self.home_page_scrollarea.setSizePolicy(sizePolicy1)
        self.home_page_scrollarea.setWidgetResizable(True)
        self.home_page_scrollarea_contents = QWidget()
        self.home_page_scrollarea_contents.setObjectName(u"home_page_scrollarea_contents")
        self.home_page_scrollarea_contents.setGeometry(QRect(0, 0, 788, 205))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_page_scrollarea_contents.sizePolicy().hasHeightForWidth())
        self.home_page_scrollarea_contents.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.home_page_scrollarea_contents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.recent_widget = QWidget(self.home_page_scrollarea_contents)
        self.recent_widget.setObjectName(u"recent_widget")
        sizePolicy2.setHeightForWidth(self.recent_widget.sizePolicy().hasHeightForWidth())
        self.recent_widget.setSizePolicy(sizePolicy2)
        self.recent_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.recent_widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.recent_label = QLabel(self.recent_widget)
        self.recent_label.setObjectName(u"recent_label")
        sizePolicy2.setHeightForWidth(self.recent_label.sizePolicy().hasHeightForWidth())
        self.recent_label.setSizePolicy(sizePolicy2)
        self.recent_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.recent_label)

        self.recent_contents = QWidget(self.recent_widget)
        self.recent_contents.setObjectName(u"recent_contents")
        sizePolicy2.setHeightForWidth(self.recent_contents.sizePolicy().hasHeightForWidth())
        self.recent_contents.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.recent_contents)


        self.verticalLayout_5.addWidget(self.recent_widget)

        self.recommend_widget = QWidget(self.home_page_scrollarea_contents)
        self.recommend_widget.setObjectName(u"recommend_widget")
        sizePolicy2.setHeightForWidth(self.recommend_widget.sizePolicy().hasHeightForWidth())
        self.recommend_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.recommend_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.recommend_label = QLabel(self.recommend_widget)
        self.recommend_label.setObjectName(u"recommend_label")
        sizePolicy2.setHeightForWidth(self.recommend_label.sizePolicy().hasHeightForWidth())
        self.recommend_label.setSizePolicy(sizePolicy2)
        self.recommend_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.recommend_label)

        self.recommend_contents = QWidget(self.recommend_widget)
        self.recommend_contents.setObjectName(u"recommend_contents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recommend_contents.sizePolicy().hasHeightForWidth())
        self.recommend_contents.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.recommend_contents)


        self.verticalLayout_5.addWidget(self.recommend_widget)

        self.categories_widget = QWidget(self.home_page_scrollarea_contents)
        self.categories_widget.setObjectName(u"categories_widget")
        sizePolicy2.setHeightForWidth(self.categories_widget.sizePolicy().hasHeightForWidth())
        self.categories_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_7 = QVBoxLayout(self.categories_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.categories_label = QLabel(self.categories_widget)
        self.categories_label.setObjectName(u"categories_label")
        sizePolicy2.setHeightForWidth(self.categories_label.sizePolicy().hasHeightForWidth())
        self.categories_label.setSizePolicy(sizePolicy2)
        self.categories_label.setFont(font1)

        self.verticalLayout_7.addWidget(self.categories_label)

        self.categories_contents = QWidget(self.categories_widget)
        self.categories_contents.setObjectName(u"categories_contents")
        sizePolicy3.setHeightForWidth(self.categories_contents.sizePolicy().hasHeightForWidth())
        self.categories_contents.setSizePolicy(sizePolicy3)

        self.verticalLayout_7.addWidget(self.categories_contents)


        self.verticalLayout_5.addWidget(self.categories_widget)

        self.home_page_scrollarea.setWidget(self.home_page_scrollarea_contents)

        self.verticalLayout_3.addWidget(self.home_page_scrollarea)

        self.pages_widget.addWidget(self.home_page)
        self.browse_page = QWidget()
        self.browse_page.setObjectName(u"browse_page")
        sizePolicy.setHeightForWidth(self.browse_page.sizePolicy().hasHeightForWidth())
        self.browse_page.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.browse_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.browse_page_scrollarea = QScrollArea(self.browse_page)
        self.browse_page_scrollarea.setObjectName(u"browse_page_scrollarea")
        self.browse_page_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.browse_page_scrollarea.setWidgetResizable(True)
        self.browse_page_scrollearea_contents = QWidget()
        self.browse_page_scrollearea_contents.setObjectName(u"browse_page_scrollearea_contents")
        self.browse_page_scrollearea_contents.setGeometry(QRect(0, 0, 232, 172))
        self.gridLayout = QGridLayout(self.browse_page_scrollearea_contents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_section = QWidget(self.browse_page_scrollearea_contents)
        self.search_section.setObjectName(u"search_section")
        sizePolicy2.setHeightForWidth(self.search_section.sizePolicy().hasHeightForWidth())
        self.search_section.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.search_section)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.search_label = QLabel(self.search_section)
        self.search_label.setObjectName(u"search_label")
        sizePolicy2.setHeightForWidth(self.search_label.sizePolicy().hasHeightForWidth())
        self.search_label.setSizePolicy(sizePolicy2)
        self.search_label.setFont(font1)

        self.verticalLayout_9.addWidget(self.search_label)

        self.search_widget = QWidget(self.search_section)
        self.search_widget.setObjectName(u"search_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.search_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.search_bar = QLineEdit(self.search_widget)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy4)
        self.search_bar.setMinimumSize(QSize(0, 40))
        self.search_bar.setFont(font2)

        self.horizontalLayout_3.addWidget(self.search_bar)

        self.search_button = QToolButton(self.search_widget)
        self.search_button.setObjectName(u"search_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy5)
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/resources/assets/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon7)
        self.search_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.search_button)


        self.verticalLayout_9.addWidget(self.search_widget)


        self.gridLayout.addWidget(self.search_section, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.recent_searches_section = QWidget(self.browse_page_scrollearea_contents)
        self.recent_searches_section.setObjectName(u"recent_searches_section")
        sizePolicy3.setHeightForWidth(self.recent_searches_section.sizePolicy().hasHeightForWidth())
        self.recent_searches_section.setSizePolicy(sizePolicy3)
        self.verticalLayout_10 = QVBoxLayout(self.recent_searches_section)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.recent_searches_label = QLabel(self.recent_searches_section)
        self.recent_searches_label.setObjectName(u"recent_searches_label")
        sizePolicy2.setHeightForWidth(self.recent_searches_label.sizePolicy().hasHeightForWidth())
        self.recent_searches_label.setSizePolicy(sizePolicy2)
        self.recent_searches_label.setFont(font1)

        self.verticalLayout_10.addWidget(self.recent_searches_label)

        self.recent_searches_widget = QWidget(self.recent_searches_section)
        self.recent_searches_widget.setObjectName(u"recent_searches_widget")
        sizePolicy3.setHeightForWidth(self.recent_searches_widget.sizePolicy().hasHeightForWidth())
        self.recent_searches_widget.setSizePolicy(sizePolicy3)
        self.recent_searches_widget.setMinimumSize(QSize(0, 41))
        self.verticalLayout_8 = QVBoxLayout(self.recent_searches_widget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.no_recent_searches_label = QLabel(self.recent_searches_widget)
        self.no_recent_searches_label.setObjectName(u"no_recent_searches_label")

        self.verticalLayout_8.addWidget(self.no_recent_searches_label)


        self.verticalLayout_10.addWidget(self.recent_searches_widget)


        self.gridLayout.addWidget(self.recent_searches_section, 1, 0, 1, 1)

        self.browse_page_scrollarea.setWidget(self.browse_page_scrollearea_contents)

        self.verticalLayout_11.addWidget(self.browse_page_scrollarea)

        self.pages_widget.addWidget(self.browse_page)
        self.library_page = QWidget()
        self.library_page.setObjectName(u"library_page")
        self.verticalLayout_12 = QVBoxLayout(self.library_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.library_header_widget = QWidget(self.library_page)
        self.library_header_widget.setObjectName(u"library_header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.library_header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.library_title_label = QLabel(self.library_header_widget)
        self.library_title_label.setObjectName(u"library_title_label")
        sizePolicy2.setHeightForWidth(self.library_title_label.sizePolicy().hasHeightForWidth())
        self.library_title_label.setSizePolicy(sizePolicy2)
        self.library_title_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.library_title_label)

        self.add_playlist_button = QToolButton(self.library_header_widget)
        self.add_playlist_button.setObjectName(u"add_playlist_button")
        self.add_playlist_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/resources/assets/images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_playlist_button.setIcon(icon8)
        self.add_playlist_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.add_playlist_button)


        self.verticalLayout_12.addWidget(self.library_header_widget)

        self.library_page_scrollarea = QScrollArea(self.library_page)
        self.library_page_scrollarea.setObjectName(u"library_page_scrollarea")
        self.library_page_scrollarea.setWidgetResizable(True)
        self.library_page_scrollarea_contents = QWidget()
        self.library_page_scrollarea_contents.setObjectName(u"library_page_scrollarea_contents")
        self.library_page_scrollarea_contents.setGeometry(QRect(0, 0, 163, 41))
        self.verticalLayout_13 = QVBoxLayout(self.library_page_scrollarea_contents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.library_contents = QWidget(self.library_page_scrollarea_contents)
        self.library_contents.setObjectName(u"library_contents")
        self.verticalLayout_21 = QVBoxLayout(self.library_contents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.no_playlists_label = QLabel(self.library_contents)
        self.no_playlists_label.setObjectName(u"no_playlists_label")

        self.verticalLayout_21.addWidget(self.no_playlists_label)


        self.verticalLayout_13.addWidget(self.library_contents)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.library_page_scrollarea.setWidget(self.library_page_scrollarea_contents)

        self.verticalLayout_12.addWidget(self.library_page_scrollarea)

        self.pages_widget.addWidget(self.library_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_14 = QVBoxLayout(self.profile_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.profile_header = QWidget(self.profile_page)
        self.profile_header.setObjectName(u"profile_header")
        self.horizontalLayout_5 = QHBoxLayout(self.profile_header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profile_title_label = QLabel(self.profile_header)
        self.profile_title_label.setObjectName(u"profile_title_label")
        sizePolicy2.setHeightForWidth(self.profile_title_label.sizePolicy().hasHeightForWidth())
        self.profile_title_label.setSizePolicy(sizePolicy2)
        self.profile_title_label.setFont(font1)
        self.profile_title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.profile_title_label)


        self.verticalLayout_14.addWidget(self.profile_header)

        self.profile_page_scrollarea = QScrollArea(self.profile_page)
        self.profile_page_scrollarea.setObjectName(u"profile_page_scrollarea")
        self.profile_page_scrollarea.setWidgetResizable(True)
        self.profile_page_scrollarea_contents = QWidget()
        self.profile_page_scrollarea_contents.setObjectName(u"profile_page_scrollarea_contents")
        self.profile_page_scrollarea_contents.setGeometry(QRect(0, 0, 788, 698))
        self.verticalLayout_15 = QVBoxLayout(self.profile_page_scrollarea_contents)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.user_profile_button = QPushButton(self.profile_page_scrollarea_contents)
        self.user_profile_button.setObjectName(u"user_profile_button")
        self.user_profile_button.setFont(font)
        self.user_profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_profile_button.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/resources/assets/images/person1NotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_profile_button.setIcon(icon9)
        self.user_profile_button.setIconSize(QSize(40, 40))
        self.user_profile_button.setCheckable(True)
        self.user_profile_button.setChecked(False)
        self.user_profile_button.setAutoExclusive(True)
        self.user_profile_button.setFlat(False)

        self.verticalLayout_15.addWidget(self.user_profile_button)

        self.profile_settings = QWidget(self.profile_page_scrollarea_contents)
        self.profile_settings.setObjectName(u"profile_settings")
        self.verticalLayout_19 = QVBoxLayout(self.profile_settings)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.settings_heading = QWidget(self.profile_settings)
        self.settings_heading.setObjectName(u"settings_heading")
        self.settings_heading.setMinimumSize(QSize(0, 50))
        self.settings_label_before = QWidget(self.settings_heading)
        self.settings_label_before.setObjectName(u"settings_label_before")
        self.settings_label_before.setGeometry(QRect(20, 10, 5, 30))
        self.settings_label_before.setStyleSheet(u"background: #D0D0D0;")
        self.settings_label = QLabel(self.settings_heading)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(40, 10, 91, 31))
        self.settings_label.setFont(font1)
        self.settings_label.setStyleSheet(u"border:none;\n"
"background: transparent;\n"
"color: #D0D0D0;")

        self.verticalLayout_19.addWidget(self.settings_heading)

        self.settings_contents = QWidget(self.profile_settings)
        self.settings_contents.setObjectName(u"settings_contents")
        self.verticalLayout_20 = QVBoxLayout(self.settings_contents)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_19.addWidget(self.settings_contents)


        self.verticalLayout_15.addWidget(self.profile_settings)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.profile_page_scrollarea.setWidget(self.profile_page_scrollarea_contents)

        self.verticalLayout_14.addWidget(self.profile_page_scrollarea)

        self.pages_widget.addWidget(self.profile_page)
        self.playlist_page = QWidget()
        self.playlist_page.setObjectName(u"playlist_page")
        self.verticalLayout_16 = QVBoxLayout(self.playlist_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.splitter = QSplitter(self.playlist_page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.playlist_image_widget = QWidget(self.splitter)
        self.playlist_image_widget.setObjectName(u"playlist_image_widget")
        self.gridLayout_3 = QGridLayout(self.playlist_image_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter.addWidget(self.playlist_image_widget)
        self.playlist_contents_widget = QWidget(self.splitter)
        self.playlist_contents_widget.setObjectName(u"playlist_contents_widget")
        self.verticalLayout_17 = QVBoxLayout(self.playlist_contents_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.playlist_contents_header = QWidget(self.playlist_contents_widget)
        self.playlist_contents_header.setObjectName(u"playlist_contents_header")
        self.horizontalLayout_6 = QHBoxLayout(self.playlist_contents_header)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.playlist_name_label = QLabel(self.playlist_contents_header)
        self.playlist_name_label.setObjectName(u"playlist_name_label")
        sizePolicy2.setHeightForWidth(self.playlist_name_label.sizePolicy().hasHeightForWidth())
        self.playlist_name_label.setSizePolicy(sizePolicy2)
        self.playlist_name_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.playlist_name_label)

        self.playlist_shuffle_button = QToolButton(self.playlist_contents_header)
        self.playlist_shuffle_button.setObjectName(u"playlist_shuffle_button")
        self.playlist_shuffle_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/resources/assets/images/shuffle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_shuffle_button.setIcon(icon10)
        self.playlist_shuffle_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.playlist_shuffle_button)

        self.playlist_play_button = QToolButton(self.playlist_contents_header)
        self.playlist_play_button.setObjectName(u"playlist_play_button")
        self.playlist_play_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/resources/assets/images/play_ver2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_play_button.setIcon(icon11)
        self.playlist_play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.playlist_play_button)


        self.verticalLayout_17.addWidget(self.playlist_contents_header)

        self.playlist_contents_scrollarea = QScrollArea(self.playlist_contents_widget)
        self.playlist_contents_scrollarea.setObjectName(u"playlist_contents_scrollarea")
        self.playlist_contents_scrollarea.setWidgetResizable(True)
        self.playlist_contents_scrollarea_contents = QWidget()
        self.playlist_contents_scrollarea_contents.setObjectName(u"playlist_contents_scrollarea_contents")
        self.playlist_contents_scrollarea_contents.setGeometry(QRect(0, 0, 770, 598))
        self.verticalLayout_18 = QVBoxLayout(self.playlist_contents_scrollarea_contents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.playlist_contents = QWidget(self.playlist_contents_scrollarea_contents)
        self.playlist_contents.setObjectName(u"playlist_contents")
        self.verticalLayout = QVBoxLayout(self.playlist_contents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.playlist_no_songs_label = QLabel(self.playlist_contents)
        self.playlist_no_songs_label.setObjectName(u"playlist_no_songs_label")

        self.verticalLayout.addWidget(self.playlist_no_songs_label)


        self.verticalLayout_18.addWidget(self.playlist_contents)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.playlist_contents_scrollarea.setWidget(self.playlist_contents_scrollarea_contents)

        self.verticalLayout_17.addWidget(self.playlist_contents_scrollarea)

        self.splitter.addWidget(self.playlist_contents_widget)

        self.verticalLayout_16.addWidget(self.splitter)

        self.pages_widget.addWidget(self.playlist_page)

        self.gridLayout_2.addWidget(self.pages_widget, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.content)

        self.stackedWidget.addWidget(self.main_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout_26 = QVBoxLayout(self.login_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.login_content = QWidget(self.login_page)
        self.login_content.setObjectName(u"login_content")
        self.login_form_container = QWidget(self.login_content)
        self.login_form_container.setObjectName(u"login_form_container")
        self.login_form_container.setGeometry(QRect(320, 220, 391, 311))
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.login_form_container.sizePolicy().hasHeightForWidth())
        self.login_form_container.setSizePolicy(sizePolicy6)
        self.verticalLayout_27 = QVBoxLayout(self.login_form_container)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.username_container = QWidget(self.login_form_container)
        self.username_container.setObjectName(u"username_container")
        sizePolicy2.setHeightForWidth(self.username_container.sizePolicy().hasHeightForWidth())
        self.username_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_28 = QVBoxLayout(self.username_container)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.username_label = QLabel(self.username_container)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_28.addWidget(self.username_label)

        self.username_input = QLineEdit(self.username_container)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout_28.addWidget(self.username_input)


        self.verticalLayout_27.addWidget(self.username_container)

        self.widget = QWidget(self.login_form_container)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_29 = QVBoxLayout(self.widget)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.username_label_2 = QLabel(self.widget)
        self.username_label_2.setObjectName(u"username_label_2")

        self.verticalLayout_29.addWidget(self.username_label_2)

        self.username_input_2 = QLineEdit(self.widget)
        self.username_input_2.setObjectName(u"username_input_2")

        self.verticalLayout_29.addWidget(self.username_input_2)


        self.verticalLayout_27.addWidget(self.widget)

        self.widget_2 = QWidget(self.login_form_container)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy7)
        self.checkBox.setChecked(False)

        self.horizontalLayout_8.addWidget(self.checkBox)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_27.addWidget(self.widget_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.pushButton = QPushButton(self.login_form_container)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_27.addWidget(self.pushButton)

        self.sign_up_label = QLabel(self.login_form_container)
        self.sign_up_label.setObjectName(u"sign_up_label")
        self.sign_up_label.setMinimumSize(QSize(0, 30))
        self.sign_up_label.setMaximumSize(QSize(16777215, 16777215))
        self.sign_up_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.sign_up_label)


        self.verticalLayout_26.addWidget(self.login_content)

        self.stackedWidget.addWidget(self.login_page)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.home_button.setDefault(False)
        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"  Browse", None))
        self.library_button.setText(QCoreApplication.translate("MainWindow", u"  Library", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"  Profile", None))
        self.thumbnail.setText("")
        self.player_song_label.setText(QCoreApplication.translate("MainWindow", u"Song Title", None))
        self.player_artist_label.setText(QCoreApplication.translate("MainWindow", u"Artist Name", None))
        self.player_startdur_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.player_enddur_label.setText(QCoreApplication.translate("MainWindow", u"-99:99", None))
        self.next_btn.setText("")
        self.play_pause_btn.setText("")
        self.previous_btn.setText("")
        self.recent_label.setText(QCoreApplication.translate("MainWindow", u"Recently Played", None))
        self.recommend_label.setText(QCoreApplication.translate("MainWindow", u"Songs that you might like", None))
        self.categories_label.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"What do you want to listen to?", None))
        self.search_button.setText("")
        self.recent_searches_label.setText(QCoreApplication.translate("MainWindow", u"Recent Searches", None))
        self.no_recent_searches_label.setText(QCoreApplication.translate("MainWindow", u"You have no recent searches.", None))
        self.library_title_label.setText(QCoreApplication.translate("MainWindow", u"Your Library", None))
        self.add_playlist_button.setText("")
        self.no_playlists_label.setText(QCoreApplication.translate("MainWindow", u"You have no playlists.", None))
        self.profile_title_label.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.user_profile_button.setText(QCoreApplication.translate("MainWindow", u"  Profile Name", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.playlist_name_label.setText(QCoreApplication.translate("MainWindow", u"Playlist Name", None))
        self.playlist_shuffle_button.setText("")
        self.playlist_play_button.setText("")
        self.playlist_no_songs_label.setText(QCoreApplication.translate("MainWindow", u"This playlist has no songs.", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remember me", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.sign_up_label.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? Click here to sign up", None))
    # retranslateUi

