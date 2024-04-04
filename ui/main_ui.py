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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 775)
        MainWindow.setStyleSheet(u"/* general styles */\n"
"\n"
"* {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#sidebar {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"QMenu {\n"
"	background-color: #1e1e1e\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"#content *, #login_content, #register_content, #player_page {\n"
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
"QSlider::groove:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #606060, stop:1 #909090);\n"
"    border: 1px solid #2e2e2e;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
""
                        "\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #b5bdc8, stop:1 #65717d);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 10px;\n"
"    margin: -4px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #d9d9d9, stop:1 #808080);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 10px;\n"
"    margin: -4px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(118, 118, 118);\n"
"    border: 1px solid #2e2e2e;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(221, 221, 221);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* login page & register page styles */\n"
"#login_content #login_page_label, #register_content #register_page_l"
                        "abel {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"#login_content *, #register_content * {\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#login_content #login_form_container, #register_content #register_form_container {\n"
"	background-color: #303030;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#login_content QLineEdit, #register_content QLineEdit {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#login_content #login_button, #register_content #register_button {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 175, 0);\n"
"	padding: 5px; \n"
"	margin: 0 8px 0 8px;\n"
"}\n"
"\n"
"#login_content #login_button:hover, #register_content #register_button:hover {\n"
"	background-color:rgb(0, 158, 0);\n"
"}\n"
"\n"
"#login_content #sign_up_container #sign_up_button,\n"
"#register_content #sign_in_container #sign_in_button {\n"
"	background-color: #303030;\n"
"	border: none;\n"
"	text-align: left;\n"
"}\n"
"\n"
"#login_content #sign_up_container #sign_up_button:hover,\n"
"#register_content #s"
                        "ign_in_container #sign_in_button:hover {\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"/* sidebar styles */\n"
"\n"
"#player_thumbnail {\n"
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
"#search_bar, #recent_searches_widget, #song_result_scrollarea, #album_result_scrollarea {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"}\n"
"\n"
"/* profile page styles */\n"
"#user_profile_button {\n"
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
"}\n"
"\n"
"/* settings page styles */\n"
"#settings_language_page QComboBox,  \n"
"#settings_theme_page QComboBox {\n"
"	background-color: white;\n"
"	padding: 2px;\n"
"	color: black;\n"
"	border: none;\n"
"}\n"
"\n"
""
                        "#settings_language_page QPushButton, \n"
"#settings_theme_page QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: #1e1e1e;\n"
"	padding: 5px 20px;\n"
"	color: #dddddd;\n"
"}\n"
"\n"
"#settings_language_page QPushButton:hover,\n"
"#settings_theme_page QPushButton:hover {\n"
"	background-color: #303030;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#settings_theme_page #settings_theme_content #theme_scrollArea #settings_theme_widget #theme_preview_content {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"}	\n"
"\n"
"#settings_about_page #about_page_content #about_page_scrollArea #about_content #about_us_label {\n"
"	margin: 10px 0;\n"
"	padding: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#settings_about_page #about_page_content #about_page_scrollArea #about_content #team_member_label\n"
"{\n"
"	margin: 10px 0;\n"
"	padding: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* generic page styles */\n"
"/*\n"
"#generic_page #generic_scroll"
                        "area {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #D0D0D0;\n"
"}	\n"
"*/")
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
        self.player_thumbnail = QPushButton(self.player_widget)
        self.player_thumbnail.setObjectName(u"player_thumbnail")
        self.player_thumbnail.setMinimumSize(QSize(240, 240))
        self.player_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.player_thumbnail.setIconSize(QSize(240, 240))
        self.player_thumbnail.setFlat(True)

        self.verticalLayout_25.addWidget(self.player_thumbnail)

        self.player_contents_widget = QWidget(self.player_widget)
        self.player_contents_widget.setObjectName(u"player_contents_widget")
        self.verticalLayout_43 = QVBoxLayout(self.player_contents_widget)
        self.verticalLayout_43.setSpacing(9)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.player_song_label = QLabel(self.player_contents_widget)
        self.player_song_label.setObjectName(u"player_song_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.player_song_label.setFont(font1)

        self.verticalLayout_43.addWidget(self.player_song_label)

        self.player_artist_label = QLabel(self.player_contents_widget)
        self.player_artist_label.setObjectName(u"player_artist_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Symbol"])
        font2.setPointSize(10)
        self.player_artist_label.setFont(font2)

        self.verticalLayout_43.addWidget(self.player_artist_label)

        self.player_slider = QSlider(self.player_contents_widget)
        self.player_slider.setObjectName(u"player_slider")
        self.player_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_43.addWidget(self.player_slider)

        self.player_duration_widget = QWidget(self.player_contents_widget)
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


        self.verticalLayout_43.addWidget(self.player_duration_widget)

        self.playback_controls = QWidget(self.player_contents_widget)
        self.playback_controls.setObjectName(u"playback_controls")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playback_controls.sizePolicy().hasHeightForWidth())
        self.playback_controls.setSizePolicy(sizePolicy)
        self.playback_controls.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_20 = QHBoxLayout(self.playback_controls)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.sidebar_player_shuffle_button = QToolButton(self.playback_controls)
        self.sidebar_player_shuffle_button.setObjectName(u"sidebar_player_shuffle_button")
        icon4 = QIcon()
        icon4.addFile(u":/resources/assets/images/shuffle_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/resources/assets/images/shuffle.png", QSize(), QIcon.Normal, QIcon.On)
        self.sidebar_player_shuffle_button.setIcon(icon4)
        self.sidebar_player_shuffle_button.setIconSize(QSize(24, 24))
        self.sidebar_player_shuffle_button.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.sidebar_player_shuffle_button)

        self.sidebar_player_previous_button = QToolButton(self.playback_controls)
        self.sidebar_player_previous_button.setObjectName(u"sidebar_player_previous_button")
        icon5 = QIcon()
        icon5.addFile(u":/resources/assets/images/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_player_previous_button.setIcon(icon5)
        self.sidebar_player_previous_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.sidebar_player_previous_button)

        self.sidebar_player_play_pause_button = QToolButton(self.playback_controls)
        self.sidebar_player_play_pause_button.setObjectName(u"sidebar_player_play_pause_button")
        icon6 = QIcon()
        icon6.addFile(u":/resources/assets/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/resources/assets/images/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.sidebar_player_play_pause_button.setIcon(icon6)
        self.sidebar_player_play_pause_button.setIconSize(QSize(24, 24))
        self.sidebar_player_play_pause_button.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.sidebar_player_play_pause_button)

        self.sidebar_player_next_button = QToolButton(self.playback_controls)
        self.sidebar_player_next_button.setObjectName(u"sidebar_player_next_button")
        icon7 = QIcon()
        icon7.addFile(u":/resources/assets/images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_player_next_button.setIcon(icon7)
        self.sidebar_player_next_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.sidebar_player_next_button)

        self.sidebar_player_loop_button = QToolButton(self.playback_controls)
        self.sidebar_player_loop_button.setObjectName(u"sidebar_player_loop_button")
        icon8 = QIcon()
        icon8.addFile(u":/resources/assets/images/loop_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/resources/assets/images/loop.png", QSize(), QIcon.Normal, QIcon.On)
        self.sidebar_player_loop_button.setIcon(icon8)
        self.sidebar_player_loop_button.setIconSize(QSize(24, 24))
        self.sidebar_player_loop_button.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.sidebar_player_loop_button)


        self.verticalLayout_43.addWidget(self.playback_controls)


        self.verticalLayout_25.addWidget(self.player_contents_widget)

        self.volume_contents = QWidget(self.player_widget)
        self.volume_contents.setObjectName(u"volume_contents")
        self.horizontalLayout_21 = QHBoxLayout(self.volume_contents)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)

        self.volume_down_button = QToolButton(self.volume_contents)
        self.volume_down_button.setObjectName(u"volume_down_button")
        icon9 = QIcon()
        icon9.addFile(u":/resources/assets/images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volume_down_button.setIcon(icon9)
        self.volume_down_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.volume_down_button)

        self.volume_slider = QSlider(self.volume_contents)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.volume_slider)

        self.volume_up_button = QToolButton(self.volume_contents)
        self.volume_up_button.setObjectName(u"volume_up_button")
        icon10 = QIcon()
        icon10.addFile(u":/resources/assets/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volume_up_button.setIcon(icon10)
        self.volume_up_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.volume_up_button)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)


        self.verticalLayout_25.addWidget(self.volume_contents)


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
        self.home_page_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.home_page_scrollarea.setWidgetResizable(True)
        self.home_page_scrollarea_contents = QWidget()
        self.home_page_scrollarea_contents.setObjectName(u"home_page_scrollarea_contents")
        self.home_page_scrollarea_contents.setGeometry(QRect(0, 0, 820, 680))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_page_scrollarea_contents.sizePolicy().hasHeightForWidth())
        self.home_page_scrollarea_contents.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.home_page_scrollarea_contents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.recent_widget = QWidget(self.home_page_scrollarea_contents)
        self.recent_widget.setObjectName(u"recent_widget")
        sizePolicy.setHeightForWidth(self.recent_widget.sizePolicy().hasHeightForWidth())
        self.recent_widget.setSizePolicy(sizePolicy)
        self.recent_widget.setMinimumSize(QSize(0, 150))
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

        self.recent_scrollarea = QScrollArea(self.recent_widget)
        self.recent_scrollarea.setObjectName(u"recent_scrollarea")
        self.recent_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recent_scrollarea.setWidgetResizable(True)
        self.recent_contents = QWidget()
        self.recent_contents.setObjectName(u"recent_contents")
        self.recent_contents.setGeometry(QRect(0, 0, 782, 97))
        self.recent_scrollarea.setWidget(self.recent_contents)

        self.verticalLayout_4.addWidget(self.recent_scrollarea)


        self.verticalLayout_5.addWidget(self.recent_widget)

        self.recommend_widget = QWidget(self.home_page_scrollarea_contents)
        self.recommend_widget.setObjectName(u"recommend_widget")
        sizePolicy2.setHeightForWidth(self.recommend_widget.sizePolicy().hasHeightForWidth())
        self.recommend_widget.setSizePolicy(sizePolicy2)
        self.recommend_widget.setMinimumSize(QSize(0, 250))
        self.verticalLayout_6 = QVBoxLayout(self.recommend_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.recommend_label = QLabel(self.recommend_widget)
        self.recommend_label.setObjectName(u"recommend_label")
        sizePolicy2.setHeightForWidth(self.recommend_label.sizePolicy().hasHeightForWidth())
        self.recommend_label.setSizePolicy(sizePolicy2)
        self.recommend_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.recommend_label)

        self.recommend_scrollarea = QScrollArea(self.recommend_widget)
        self.recommend_scrollarea.setObjectName(u"recommend_scrollarea")
        self.recommend_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recommend_scrollarea.setWidgetResizable(True)
        self.recommend_contents = QWidget()
        self.recommend_contents.setObjectName(u"recommend_contents")
        self.recommend_contents.setGeometry(QRect(0, 0, 782, 201))
        self.recommend_scrollarea.setWidget(self.recommend_contents)

        self.verticalLayout_6.addWidget(self.recommend_scrollarea)


        self.verticalLayout_5.addWidget(self.recommend_widget)

        self.categories_widget = QWidget(self.home_page_scrollarea_contents)
        self.categories_widget.setObjectName(u"categories_widget")
        sizePolicy.setHeightForWidth(self.categories_widget.sizePolicy().hasHeightForWidth())
        self.categories_widget.setSizePolicy(sizePolicy)
        self.categories_widget.setMinimumSize(QSize(0, 250))
        self.verticalLayout_7 = QVBoxLayout(self.categories_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.categories_label = QLabel(self.categories_widget)
        self.categories_label.setObjectName(u"categories_label")
        sizePolicy2.setHeightForWidth(self.categories_label.sizePolicy().hasHeightForWidth())
        self.categories_label.setSizePolicy(sizePolicy2)
        self.categories_label.setFont(font1)

        self.verticalLayout_7.addWidget(self.categories_label)

        self.categories_scrollarea = QScrollArea(self.categories_widget)
        self.categories_scrollarea.setObjectName(u"categories_scrollarea")
        self.categories_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.categories_scrollarea.setWidgetResizable(True)
        self.categories_contents = QWidget()
        self.categories_contents.setObjectName(u"categories_contents")
        self.categories_contents.setGeometry(QRect(0, 0, 782, 201))
        self.categories_scrollarea.setWidget(self.categories_contents)

        self.verticalLayout_7.addWidget(self.categories_scrollarea)


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
        self.browse_page_scrollearea_contents.setGeometry(QRect(0, 0, 820, 755))
        self.verticalLayout_45 = QVBoxLayout(self.browse_page_scrollearea_contents)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy3)
        self.search_bar.setMinimumSize(QSize(0, 40))
        self.search_bar.setFont(font2)

        self.horizontalLayout_3.addWidget(self.search_bar)

        self.search_button = QToolButton(self.search_widget)
        self.search_button.setObjectName(u"search_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy4)
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/resources/assets/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon11)
        self.search_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.search_button)


        self.verticalLayout_9.addWidget(self.search_widget)


        self.verticalLayout_45.addWidget(self.search_section)

        self.recent_searches_section = QWidget(self.browse_page_scrollearea_contents)
        self.recent_searches_section.setObjectName(u"recent_searches_section")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.recent_searches_section.sizePolicy().hasHeightForWidth())
        self.recent_searches_section.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.recent_searches_widget.sizePolicy().hasHeightForWidth())
        self.recent_searches_widget.setSizePolicy(sizePolicy5)
        self.recent_searches_widget.setMinimumSize(QSize(0, 41))
        self.verticalLayout_8 = QVBoxLayout(self.recent_searches_widget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.no_recent_searches_label = QLabel(self.recent_searches_widget)
        self.no_recent_searches_label.setObjectName(u"no_recent_searches_label")

        self.verticalLayout_8.addWidget(self.no_recent_searches_label)


        self.verticalLayout_10.addWidget(self.recent_searches_widget)


        self.verticalLayout_45.addWidget(self.recent_searches_section)

        self.song_result_label = QLabel(self.browse_page_scrollearea_contents)
        self.song_result_label.setObjectName(u"song_result_label")
        sizePolicy2.setHeightForWidth(self.song_result_label.sizePolicy().hasHeightForWidth())
        self.song_result_label.setSizePolicy(sizePolicy2)
        self.song_result_label.setFont(font1)

        self.verticalLayout_45.addWidget(self.song_result_label)

        self.song_result_scrollarea = QScrollArea(self.browse_page_scrollearea_contents)
        self.song_result_scrollarea.setObjectName(u"song_result_scrollarea")
        self.song_result_scrollarea.setFrameShape(QFrame.Box)
        self.song_result_scrollarea.setFrameShadow(QFrame.Plain)
        self.song_result_scrollarea.setLineWidth(0)
        self.song_result_scrollarea.setWidgetResizable(True)
        self.song_result_scrollarea_contents = QWidget()
        self.song_result_scrollarea_contents.setObjectName(u"song_result_scrollarea_contents")
        self.song_result_scrollarea_contents.setGeometry(QRect(0, 0, 800, 258))
        self.song_result_scrollarea.setWidget(self.song_result_scrollarea_contents)

        self.verticalLayout_45.addWidget(self.song_result_scrollarea)

        self.album_result_label = QLabel(self.browse_page_scrollearea_contents)
        self.album_result_label.setObjectName(u"album_result_label")
        sizePolicy2.setHeightForWidth(self.album_result_label.sizePolicy().hasHeightForWidth())
        self.album_result_label.setSizePolicy(sizePolicy2)
        self.album_result_label.setFont(font1)

        self.verticalLayout_45.addWidget(self.album_result_label)

        self.album_result_scrollarea = QScrollArea(self.browse_page_scrollearea_contents)
        self.album_result_scrollarea.setObjectName(u"album_result_scrollarea")
        self.album_result_scrollarea.setFrameShape(QFrame.Box)
        self.album_result_scrollarea.setFrameShadow(QFrame.Plain)
        self.album_result_scrollarea.setLineWidth(0)
        self.album_result_scrollarea.setWidgetResizable(True)
        self.album_result_scrollarea_contents = QWidget()
        self.album_result_scrollarea_contents.setObjectName(u"album_result_scrollarea_contents")
        self.album_result_scrollarea_contents.setGeometry(QRect(0, 0, 800, 257))
        self.album_result_scrollarea.setWidget(self.album_result_scrollarea_contents)

        self.verticalLayout_45.addWidget(self.album_result_scrollarea)

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
        icon12 = QIcon()
        icon12.addFile(u":/resources/assets/images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_playlist_button.setIcon(icon12)
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
        self.profile_page_scrollarea_contents.setGeometry(QRect(0, 0, 820, 708))
        self.verticalLayout_15 = QVBoxLayout(self.profile_page_scrollarea_contents)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.user_profile_button = QPushButton(self.profile_page_scrollarea_contents)
        self.user_profile_button.setObjectName(u"user_profile_button")
        self.user_profile_button.setFont(font)
        self.user_profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_profile_button.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/resources/assets/images/person1NotActive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_profile_button.setIcon(icon13)
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
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        self.playlist_image_widget = QWidget(self.splitter)
        self.playlist_image_widget.setObjectName(u"playlist_image_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.playlist_image_widget.sizePolicy().hasHeightForWidth())
        self.playlist_image_widget.setSizePolicy(sizePolicy6)
        self.gridLayout_3 = QGridLayout(self.playlist_image_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter.addWidget(self.playlist_image_widget)
        self.playlist_contents_widget = QWidget(self.splitter)
        self.playlist_contents_widget.setObjectName(u"playlist_contents_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.playlist_contents_widget.sizePolicy().hasHeightForWidth())
        self.playlist_contents_widget.setSizePolicy(sizePolicy7)
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

        self.playlist_edit_button = QToolButton(self.playlist_contents_header)
        self.playlist_edit_button.setObjectName(u"playlist_edit_button")
        self.playlist_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/resources/assets/images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_edit_button.setIcon(icon14)
        self.playlist_edit_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.playlist_edit_button)

        self.playlist_shuffle_button = QToolButton(self.playlist_contents_header)
        self.playlist_shuffle_button.setObjectName(u"playlist_shuffle_button")
        self.playlist_shuffle_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/resources/assets/images/shuffle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_shuffle_button.setIcon(icon15)
        self.playlist_shuffle_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.playlist_shuffle_button)

        self.playlist_play_button = QToolButton(self.playlist_contents_header)
        self.playlist_play_button.setObjectName(u"playlist_play_button")
        self.playlist_play_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/resources/assets/images/play_ver2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_play_button.setIcon(icon16)
        self.playlist_play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.playlist_play_button)


        self.verticalLayout_17.addWidget(self.playlist_contents_header)

        self.playlist_contents_scrollarea = QScrollArea(self.playlist_contents_widget)
        self.playlist_contents_scrollarea.setObjectName(u"playlist_contents_scrollarea")
        self.playlist_contents_scrollarea.setWidgetResizable(True)
        self.playlist_contents_scrollarea_contents = QWidget()
        self.playlist_contents_scrollarea_contents.setObjectName(u"playlist_contents_scrollarea_contents")
        self.playlist_contents_scrollarea_contents.setGeometry(QRect(0, 0, 802, 678))
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
        self.settings_about_page = QWidget()
        self.settings_about_page.setObjectName(u"settings_about_page")
        self.verticalLayout_2 = QVBoxLayout(self.settings_about_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.about_page_content = QWidget(self.settings_about_page)
        self.about_page_content.setObjectName(u"about_page_content")
        font4 = QFont()
        font4.setPointSize(9)
        self.about_page_content.setFont(font4)
        self.verticalLayout_41 = QVBoxLayout(self.about_page_content)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.settings_theme_page_label_2 = QLabel(self.about_page_content)
        self.settings_theme_page_label_2.setObjectName(u"settings_theme_page_label_2")
        sizePolicy2.setHeightForWidth(self.settings_theme_page_label_2.sizePolicy().hasHeightForWidth())
        self.settings_theme_page_label_2.setSizePolicy(sizePolicy2)
        self.settings_theme_page_label_2.setFont(font1)
        self.settings_theme_page_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.settings_theme_page_label_2)

        self.about_page_scrollArea = QScrollArea(self.about_page_content)
        self.about_page_scrollArea.setObjectName(u"about_page_scrollArea")
        self.about_page_scrollArea.setFrameShape(QFrame.NoFrame)
        self.about_page_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.about_page_scrollArea.setWidgetResizable(True)
        self.about_content = QWidget()
        self.about_content.setObjectName(u"about_content")
        self.about_content.setGeometry(QRect(0, 0, 319, 406))
        self.verticalLayout_42 = QVBoxLayout(self.about_content)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.about_us_label = QLabel(self.about_content)
        self.about_us_label.setObjectName(u"about_us_label")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.about_us_label.setFont(font5)
        self.about_us_label.setFrameShape(QFrame.Box)

        self.verticalLayout_42.addWidget(self.about_us_label)

        self.about_us_2 = QLabel(self.about_content)
        self.about_us_2.setObjectName(u"about_us_2")
        font6 = QFont()
        font6.setPointSize(12)
        self.about_us_2.setFont(font6)
        self.about_us_2.setWordWrap(True)
        self.about_us_2.setMargin(4)

        self.verticalLayout_42.addWidget(self.about_us_2)

        self.team_member_label = QLabel(self.about_content)
        self.team_member_label.setObjectName(u"team_member_label")
        self.team_member_label.setFont(font5)
        self.team_member_label.setFrameShape(QFrame.Box)

        self.verticalLayout_42.addWidget(self.team_member_label)

        self.member = QLabel(self.about_content)
        self.member.setObjectName(u"member")
        self.member.setFont(font6)
        self.member.setMargin(4)

        self.verticalLayout_42.addWidget(self.member)

        self.member_2 = QLabel(self.about_content)
        self.member_2.setObjectName(u"member_2")
        self.member_2.setFont(font6)
        self.member_2.setMargin(4)

        self.verticalLayout_42.addWidget(self.member_2)

        self.member_3 = QLabel(self.about_content)
        self.member_3.setObjectName(u"member_3")
        self.member_3.setFont(font6)
        self.member_3.setMargin(4)

        self.verticalLayout_42.addWidget(self.member_3)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_13)

        self.about_page_scrollArea.setWidget(self.about_content)

        self.verticalLayout_41.addWidget(self.about_page_scrollArea)


        self.verticalLayout_2.addWidget(self.about_page_content)

        self.pages_widget.addWidget(self.settings_about_page)
        self.settings_language_page = QWidget()
        self.settings_language_page.setObjectName(u"settings_language_page")
        self.verticalLayout_26 = QVBoxLayout(self.settings_language_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.settings_language_content = QWidget(self.settings_language_page)
        self.settings_language_content.setObjectName(u"settings_language_content")
        self.verticalLayout_31 = QVBoxLayout(self.settings_language_content)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.setting_language_page_label = QLabel(self.settings_language_content)
        self.setting_language_page_label.setObjectName(u"setting_language_page_label")
        sizePolicy2.setHeightForWidth(self.setting_language_page_label.sizePolicy().hasHeightForWidth())
        self.setting_language_page_label.setSizePolicy(sizePolicy2)
        self.setting_language_page_label.setFont(font1)
        self.setting_language_page_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.setting_language_page_label)

        self.language_header = QWidget(self.settings_language_content)
        self.language_header.setObjectName(u"language_header")
        self.horizontalLayout_14 = QHBoxLayout(self.language_header)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.apply_language_button = QPushButton(self.language_header)
        self.apply_language_button.setObjectName(u"apply_language_button")
        self.apply_language_button.setFont(font6)
        self.apply_language_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.apply_language_button)


        self.verticalLayout_31.addWidget(self.language_header)

        self.langauge_content = QWidget(self.settings_language_content)
        self.langauge_content.setObjectName(u"langauge_content")
        self.horizontalLayout_15 = QHBoxLayout(self.langauge_content)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.language_label = QLabel(self.langauge_content)
        self.language_label.setObjectName(u"language_label")
        self.language_label.setFont(font6)

        self.horizontalLayout_15.addWidget(self.language_label)

        self.language_comboBox = QComboBox(self.langauge_content)
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.setObjectName(u"language_comboBox")
        self.language_comboBox.setFont(font6)
        self.language_comboBox.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_15.addWidget(self.language_comboBox)


        self.verticalLayout_31.addWidget(self.langauge_content)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_10)


        self.verticalLayout_26.addWidget(self.settings_language_content)

        self.pages_widget.addWidget(self.settings_language_page)
        self.settings_theme_page = QWidget()
        self.settings_theme_page.setObjectName(u"settings_theme_page")
        self.verticalLayout_30 = QVBoxLayout(self.settings_theme_page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.settings_theme_content = QWidget(self.settings_theme_page)
        self.settings_theme_content.setObjectName(u"settings_theme_content")
        self.verticalLayout_37 = QVBoxLayout(self.settings_theme_content)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.settings_theme_page_label = QLabel(self.settings_theme_content)
        self.settings_theme_page_label.setObjectName(u"settings_theme_page_label")
        sizePolicy2.setHeightForWidth(self.settings_theme_page_label.sizePolicy().hasHeightForWidth())
        self.settings_theme_page_label.setSizePolicy(sizePolicy2)
        self.settings_theme_page_label.setFont(font1)
        self.settings_theme_page_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.settings_theme_page_label)

        self.theme_header = QWidget(self.settings_theme_content)
        self.theme_header.setObjectName(u"theme_header")
        self.horizontalLayout_16 = QHBoxLayout(self.theme_header)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.apply_theme_button = QPushButton(self.theme_header)
        self.apply_theme_button.setObjectName(u"apply_theme_button")
        self.apply_theme_button.setFont(font6)
        self.apply_theme_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.apply_theme_button)


        self.verticalLayout_37.addWidget(self.theme_header)

        self.theme_scrollArea = QScrollArea(self.settings_theme_content)
        self.theme_scrollArea.setObjectName(u"theme_scrollArea")
        self.theme_scrollArea.setFrameShape(QFrame.NoFrame)
        self.theme_scrollArea.setLineWidth(0)
        self.theme_scrollArea.setWidgetResizable(True)
        self.settings_theme_widget = QWidget()
        self.settings_theme_widget.setObjectName(u"settings_theme_widget")
        self.settings_theme_widget.setGeometry(QRect(0, 0, 231, 124))
        self.verticalLayout_39 = QVBoxLayout(self.settings_theme_widget)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.settings_theme_content_2 = QWidget(self.settings_theme_widget)
        self.settings_theme_content_2.setObjectName(u"settings_theme_content_2")
        self.horizontalLayout_18 = QHBoxLayout(self.settings_theme_content_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.current_theme_label = QLabel(self.settings_theme_content_2)
        self.current_theme_label.setObjectName(u"current_theme_label")
        self.current_theme_label.setFont(font6)

        self.horizontalLayout_18.addWidget(self.current_theme_label)

        self.theme_comboBox_ = QComboBox(self.settings_theme_content_2)
        self.theme_comboBox_.addItem("")
        self.theme_comboBox_.setObjectName(u"theme_comboBox_")
        self.theme_comboBox_.setFont(font6)
        self.theme_comboBox_.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_18.addWidget(self.theme_comboBox_)


        self.verticalLayout_39.addWidget(self.settings_theme_content_2)

        self.theme_preview_label = QLabel(self.settings_theme_widget)
        self.theme_preview_label.setObjectName(u"theme_preview_label")
        self.theme_preview_label.setFont(font6)
        self.theme_preview_label.setMargin(9)

        self.verticalLayout_39.addWidget(self.theme_preview_label)

        self.theme_preview_content = QWidget(self.settings_theme_widget)
        self.theme_preview_content.setObjectName(u"theme_preview_content")

        self.verticalLayout_39.addWidget(self.theme_preview_content)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_12)

        self.theme_scrollArea.setWidget(self.settings_theme_widget)

        self.verticalLayout_37.addWidget(self.theme_scrollArea)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_11)


        self.verticalLayout_30.addWidget(self.settings_theme_content)

        self.pages_widget.addWidget(self.settings_theme_page)
        self.generic_page = QWidget()
        self.generic_page.setObjectName(u"generic_page")
        self.verticalLayout_40 = QVBoxLayout(self.generic_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.generic_page_contents = QWidget(self.generic_page)
        self.generic_page_contents.setObjectName(u"generic_page_contents")
        self.verticalLayout_44 = QVBoxLayout(self.generic_page_contents)
        self.verticalLayout_44.setSpacing(12)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.generic_title = QLabel(self.generic_page_contents)
        self.generic_title.setObjectName(u"generic_title")
        sizePolicy2.setHeightForWidth(self.generic_title.sizePolicy().hasHeightForWidth())
        self.generic_title.setSizePolicy(sizePolicy2)
        self.generic_title.setFont(font1)
        self.generic_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.generic_title)

        self.generic_scrollarea = QScrollArea(self.generic_page_contents)
        self.generic_scrollarea.setObjectName(u"generic_scrollarea")
        self.generic_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.generic_scrollarea.setWidgetResizable(True)
        self.generic_scrollarea_contents = QWidget()
        self.generic_scrollarea_contents.setObjectName(u"generic_scrollarea_contents")
        self.generic_scrollarea_contents.setGeometry(QRect(0, 0, 802, 702))
        self.generic_scrollarea.setWidget(self.generic_scrollarea_contents)

        self.verticalLayout_44.addWidget(self.generic_scrollarea)


        self.verticalLayout_40.addWidget(self.generic_page_contents)

        self.pages_widget.addWidget(self.generic_page)

        self.gridLayout_2.addWidget(self.pages_widget, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.content)

        self.stackedWidget.addWidget(self.main_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.gridLayout_6 = QGridLayout(self.login_page)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.login_content = QWidget(self.login_page)
        self.login_content.setObjectName(u"login_content")
        self.gridLayout_4 = QGridLayout(self.login_content)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.login_form_container = QWidget(self.login_content)
        self.login_form_container.setObjectName(u"login_form_container")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.login_form_container.sizePolicy().hasHeightForWidth())
        self.login_form_container.setSizePolicy(sizePolicy8)
        self.verticalLayout_27 = QVBoxLayout(self.login_form_container)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.login_page_label = QLabel(self.login_form_container)
        self.login_page_label.setObjectName(u"login_page_label")
        font7 = QFont()
        font7.setBold(True)
        self.login_page_label.setFont(font7)
        self.login_page_label.setAlignment(Qt.AlignCenter)
        self.login_page_label.setMargin(5)

        self.verticalLayout_27.addWidget(self.login_page_label)

        self.login_email_container = QWidget(self.login_form_container)
        self.login_email_container.setObjectName(u"login_email_container")
        sizePolicy2.setHeightForWidth(self.login_email_container.sizePolicy().hasHeightForWidth())
        self.login_email_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_28 = QVBoxLayout(self.login_email_container)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.login_email_label = QLabel(self.login_email_container)
        self.login_email_label.setObjectName(u"login_email_label")
        self.login_email_label.setFont(font)

        self.verticalLayout_28.addWidget(self.login_email_label)

        self.login_email_input = QLineEdit(self.login_email_container)
        self.login_email_input.setObjectName(u"login_email_input")

        self.verticalLayout_28.addWidget(self.login_email_input)


        self.verticalLayout_27.addWidget(self.login_email_container)

        self.login_password_container = QWidget(self.login_form_container)
        self.login_password_container.setObjectName(u"login_password_container")
        sizePolicy2.setHeightForWidth(self.login_password_container.sizePolicy().hasHeightForWidth())
        self.login_password_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_29 = QVBoxLayout(self.login_password_container)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.login_password_label = QLabel(self.login_password_container)
        self.login_password_label.setObjectName(u"login_password_label")
        self.login_password_label.setFont(font)
        self.login_password_label.setCursor(QCursor(Qt.UpArrowCursor))

        self.verticalLayout_29.addWidget(self.login_password_label)

        self.login_password_input = QLineEdit(self.login_password_container)
        self.login_password_input.setObjectName(u"login_password_input")
        self.login_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_29.addWidget(self.login_password_input)


        self.verticalLayout_27.addWidget(self.login_password_container)

        self.remember_container = QWidget(self.login_form_container)
        self.remember_container.setObjectName(u"remember_container")
        self.horizontalLayout_8 = QHBoxLayout(self.remember_container)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 4, 0)
        self.remember_checkbox = QCheckBox(self.remember_container)
        self.remember_checkbox.setObjectName(u"remember_checkbox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.remember_checkbox.sizePolicy().hasHeightForWidth())
        self.remember_checkbox.setSizePolicy(sizePolicy9)
        self.remember_checkbox.setChecked(False)

        self.horizontalLayout_8.addWidget(self.remember_checkbox)

        self.remember_label = QLabel(self.remember_container)
        self.remember_label.setObjectName(u"remember_label")
        self.remember_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.remember_label)


        self.verticalLayout_27.addWidget(self.remember_container)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.login_button = QPushButton(self.login_form_container)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(0, 40))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setFocusPolicy(Qt.TabFocus)

        self.verticalLayout_27.addWidget(self.login_button)

        self.sign_up_container = QWidget(self.login_form_container)
        self.sign_up_container.setObjectName(u"sign_up_container")
        self.horizontalLayout_11 = QHBoxLayout(self.sign_up_container)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 4, 4)
        self.sign_up_label = QLabel(self.sign_up_container)
        self.sign_up_label.setObjectName(u"sign_up_label")
        self.sign_up_label.setMinimumSize(QSize(0, 30))
        self.sign_up_label.setMaximumSize(QSize(16777215, 16777215))
        self.sign_up_label.setFont(font)
        self.sign_up_label.setLineWidth(1)
        self.sign_up_label.setAlignment(Qt.AlignCenter)
        self.sign_up_label.setMargin(0)
        self.sign_up_label.setIndent(-1)

        self.horizontalLayout_11.addWidget(self.sign_up_label)

        self.sign_up_button = QPushButton(self.sign_up_container)
        self.sign_up_button.setObjectName(u"sign_up_button")
        font8 = QFont()
        font8.setKerning(False)
        self.sign_up_button.setFont(font8)
        self.sign_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_up_button.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.sign_up_button)


        self.verticalLayout_27.addWidget(self.sign_up_container)


        self.gridLayout_4.addWidget(self.login_form_container, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.login_content, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.gridLayout_8 = QGridLayout(self.register_page)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.register_content = QWidget(self.register_page)
        self.register_content.setObjectName(u"register_content")
        self.gridLayout_7 = QGridLayout(self.register_content)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.register_form_container = QWidget(self.register_content)
        self.register_form_container.setObjectName(u"register_form_container")
        sizePolicy8.setHeightForWidth(self.register_form_container.sizePolicy().hasHeightForWidth())
        self.register_form_container.setSizePolicy(sizePolicy8)
        self.verticalLayout_33 = QVBoxLayout(self.register_form_container)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.register_email_container = QWidget(self.register_form_container)
        self.register_email_container.setObjectName(u"register_email_container")
        sizePolicy2.setHeightForWidth(self.register_email_container.sizePolicy().hasHeightForWidth())
        self.register_email_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_34 = QVBoxLayout(self.register_email_container)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.register_page_label = QLabel(self.register_email_container)
        self.register_page_label.setObjectName(u"register_page_label")
        self.register_page_label.setFont(font7)
        self.register_page_label.setAlignment(Qt.AlignCenter)
        self.register_page_label.setMargin(4)

        self.verticalLayout_34.addWidget(self.register_page_label)

        self.register_email_label = QLabel(self.register_email_container)
        self.register_email_label.setObjectName(u"register_email_label")
        self.register_email_label.setFont(font)

        self.verticalLayout_34.addWidget(self.register_email_label)

        self.register_email_input = QLineEdit(self.register_email_container)
        self.register_email_input.setObjectName(u"register_email_input")

        self.verticalLayout_34.addWidget(self.register_email_input)


        self.verticalLayout_33.addWidget(self.register_email_container)

        self.display_name_container = QWidget(self.register_form_container)
        self.display_name_container.setObjectName(u"display_name_container")
        sizePolicy2.setHeightForWidth(self.display_name_container.sizePolicy().hasHeightForWidth())
        self.display_name_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_35 = QVBoxLayout(self.display_name_container)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.display_name_label = QLabel(self.display_name_container)
        self.display_name_label.setObjectName(u"display_name_label")
        self.display_name_label.setFont(font)
        self.display_name_label.setCursor(QCursor(Qt.UpArrowCursor))

        self.verticalLayout_35.addWidget(self.display_name_label)

        self.display_name_input = QLineEdit(self.display_name_container)
        self.display_name_input.setObjectName(u"display_name_input")

        self.verticalLayout_35.addWidget(self.display_name_input)


        self.verticalLayout_33.addWidget(self.display_name_container)

        self.register_password_container = QWidget(self.register_form_container)
        self.register_password_container.setObjectName(u"register_password_container")
        sizePolicy2.setHeightForWidth(self.register_password_container.sizePolicy().hasHeightForWidth())
        self.register_password_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_36 = QVBoxLayout(self.register_password_container)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.register_password_label = QLabel(self.register_password_container)
        self.register_password_label.setObjectName(u"register_password_label")
        self.register_password_label.setFont(font)
        self.register_password_label.setCursor(QCursor(Qt.UpArrowCursor))

        self.verticalLayout_36.addWidget(self.register_password_label)

        self.register_password_input = QLineEdit(self.register_password_container)
        self.register_password_input.setObjectName(u"register_password_input")
        self.register_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_36.addWidget(self.register_password_input)


        self.verticalLayout_33.addWidget(self.register_password_container)

        self.register_confirm_password_container = QWidget(self.register_form_container)
        self.register_confirm_password_container.setObjectName(u"register_confirm_password_container")
        sizePolicy2.setHeightForWidth(self.register_confirm_password_container.sizePolicy().hasHeightForWidth())
        self.register_confirm_password_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_38 = QVBoxLayout(self.register_confirm_password_container)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.register_confirm_password_label = QLabel(self.register_confirm_password_container)
        self.register_confirm_password_label.setObjectName(u"register_confirm_password_label")
        self.register_confirm_password_label.setFont(font)
        self.register_confirm_password_label.setCursor(QCursor(Qt.UpArrowCursor))

        self.verticalLayout_38.addWidget(self.register_confirm_password_label)

        self.register_confirm_password_input = QLineEdit(self.register_confirm_password_container)
        self.register_confirm_password_input.setObjectName(u"register_confirm_password_input")
        self.register_confirm_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_38.addWidget(self.register_confirm_password_input)


        self.verticalLayout_33.addWidget(self.register_confirm_password_container)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_9)

        self.register_button = QPushButton(self.register_form_container)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setMinimumSize(QSize(0, 40))
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_33.addWidget(self.register_button)

        self.sign_in_container = QWidget(self.register_form_container)
        self.sign_in_container.setObjectName(u"sign_in_container")
        self.horizontalLayout_13 = QHBoxLayout(self.sign_in_container)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 4, 4)
        self.sign_in_label = QLabel(self.sign_in_container)
        self.sign_in_label.setObjectName(u"sign_in_label")
        self.sign_in_label.setMinimumSize(QSize(0, 30))
        self.sign_in_label.setMaximumSize(QSize(16777215, 16777215))
        self.sign_in_label.setFont(font)
        self.sign_in_label.setLineWidth(1)
        self.sign_in_label.setAlignment(Qt.AlignCenter)
        self.sign_in_label.setMargin(0)
        self.sign_in_label.setIndent(-1)

        self.horizontalLayout_13.addWidget(self.sign_in_label)

        self.sign_in_button = QPushButton(self.sign_in_container)
        self.sign_in_button.setObjectName(u"sign_in_button")
        self.sign_in_button.setFont(font8)
        self.sign_in_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_in_button.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.sign_in_button)


        self.verticalLayout_33.addWidget(self.sign_in_container)


        self.gridLayout_7.addWidget(self.register_form_container, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.register_content, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.register_page)
        self.player_page = QWidget()
        self.player_page.setObjectName(u"player_page")
        self.horizontalLayout = QHBoxLayout(self.player_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.player_page_contents = QWidget(self.player_page)
        self.player_page_contents.setObjectName(u"player_page_contents")
        self.verticalLayout_22 = QVBoxLayout(self.player_page_contents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.player_page_header = QWidget(self.player_page_contents)
        self.player_page_header.setObjectName(u"player_page_header")
        self.horizontalLayout_9 = QHBoxLayout(self.player_page_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.player_page_back_button = QToolButton(self.player_page_header)
        self.player_page_back_button.setObjectName(u"player_page_back_button")
        self.player_page_back_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/resources/assets/images/go_back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.player_page_back_button.setIcon(icon17)
        self.player_page_back_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.player_page_back_button)

        self.player_page_playlist_label = QLabel(self.player_page_header)
        self.player_page_playlist_label.setObjectName(u"player_page_playlist_label")
        sizePolicy2.setHeightForWidth(self.player_page_playlist_label.sizePolicy().hasHeightForWidth())
        self.player_page_playlist_label.setSizePolicy(sizePolicy2)
        self.player_page_playlist_label.setFont(font1)
        self.player_page_playlist_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.player_page_playlist_label)

        self.share_button = QToolButton(self.player_page_header)
        self.share_button.setObjectName(u"share_button")
        self.share_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/resources/assets/images/share.png", QSize(), QIcon.Normal, QIcon.Off)
        self.share_button.setIcon(icon18)
        self.share_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.share_button)


        self.verticalLayout_22.addWidget(self.player_page_header)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer)

        self.player_page_content = QWidget(self.player_page_contents)
        self.player_page_content.setObjectName(u"player_page_content")
        self.horizontalLayout_10 = QHBoxLayout(self.player_page_content)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget = QWidget(self.player_page_content)
        self.widget.setObjectName(u"widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy10)
        self.verticalLayout_46 = QVBoxLayout(self.widget)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.player_page_thumbnail = QLabel(self.widget)
        self.player_page_thumbnail.setObjectName(u"player_page_thumbnail")
        sizePolicy.setHeightForWidth(self.player_page_thumbnail.sizePolicy().hasHeightForWidth())
        self.player_page_thumbnail.setSizePolicy(sizePolicy)
        self.player_page_thumbnail.setMinimumSize(QSize(350, 347))
        self.player_page_thumbnail.setMaximumSize(QSize(350, 350))
        self.player_page_thumbnail.setPixmap(QPixmap(u":/resources/assets/images/thumbnail_placeholder.png"))
        self.player_page_thumbnail.setScaledContents(True)

        self.verticalLayout_46.addWidget(self.player_page_thumbnail, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.widget)

        self.player_page_container = QWidget(self.player_page_content)
        self.player_page_container.setObjectName(u"player_page_container")
        sizePolicy3.setHeightForWidth(self.player_page_container.sizePolicy().hasHeightForWidth())
        self.player_page_container.setSizePolicy(sizePolicy3)
        self.verticalLayout_32 = QVBoxLayout(self.player_page_container)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.player_page_song_label = QLabel(self.player_page_container)
        self.player_page_song_label.setObjectName(u"player_page_song_label")
        self.player_page_song_label.setFont(font1)

        self.verticalLayout_32.addWidget(self.player_page_song_label)

        self.player_page_artist_label = QLabel(self.player_page_container)
        self.player_page_artist_label.setObjectName(u"player_page_artist_label")
        self.player_page_artist_label.setFont(font2)

        self.verticalLayout_32.addWidget(self.player_page_artist_label)

        self.player_page_slider = QSlider(self.player_page_container)
        self.player_page_slider.setObjectName(u"player_page_slider")
        self.player_page_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_32.addWidget(self.player_page_slider)

        self.player_duration_container = QWidget(self.player_page_container)
        self.player_duration_container.setObjectName(u"player_duration_container")
        self.horizontalLayout_12 = QHBoxLayout(self.player_duration_container)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.player_page_startdur_label = QLabel(self.player_duration_container)
        self.player_page_startdur_label.setObjectName(u"player_page_startdur_label")
        self.player_page_startdur_label.setFont(font2)

        self.horizontalLayout_12.addWidget(self.player_page_startdur_label)

        self.player_page_enddur_label = QLabel(self.player_duration_container)
        self.player_page_enddur_label.setObjectName(u"player_page_enddur_label")
        self.player_page_enddur_label.setFont(font3)
        self.player_page_enddur_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.player_page_enddur_label)


        self.verticalLayout_32.addWidget(self.player_duration_container)

        self.player_page_buttons = QWidget(self.player_page_container)
        self.player_page_buttons.setObjectName(u"player_page_buttons")
        self.horizontalLayout_17 = QHBoxLayout(self.player_page_buttons)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.player_page_shuffle_button = QToolButton(self.player_page_buttons)
        self.player_page_shuffle_button.setObjectName(u"player_page_shuffle_button")
        self.player_page_shuffle_button.setIcon(icon4)
        self.player_page_shuffle_button.setIconSize(QSize(24, 24))
        self.player_page_shuffle_button.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.player_page_shuffle_button)

        self.player_page_previous_button = QToolButton(self.player_page_buttons)
        self.player_page_previous_button.setObjectName(u"player_page_previous_button")
        self.player_page_previous_button.setIcon(icon5)
        self.player_page_previous_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.player_page_previous_button)

        self.player_page_play_pause_button = QToolButton(self.player_page_buttons)
        self.player_page_play_pause_button.setObjectName(u"player_page_play_pause_button")
        self.player_page_play_pause_button.setIcon(icon6)
        self.player_page_play_pause_button.setIconSize(QSize(24, 24))
        self.player_page_play_pause_button.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.player_page_play_pause_button)

        self.player_page_next_button = QToolButton(self.player_page_buttons)
        self.player_page_next_button.setObjectName(u"player_page_next_button")
        self.player_page_next_button.setIcon(icon7)
        self.player_page_next_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.player_page_next_button)

        self.player_page_loop_button = QToolButton(self.player_page_buttons)
        self.player_page_loop_button.setObjectName(u"player_page_loop_button")
        self.player_page_loop_button.setIcon(icon8)
        self.player_page_loop_button.setIconSize(QSize(24, 24))
        self.player_page_loop_button.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.player_page_loop_button)


        self.verticalLayout_32.addWidget(self.player_page_buttons)

        self.player_page_volume_controls = QWidget(self.player_page_container)
        self.player_page_volume_controls.setObjectName(u"player_page_volume_controls")
        self.horizontalLayout_22 = QHBoxLayout(self.player_page_volume_controls)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_3 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.player_page_volume_down_button = QToolButton(self.player_page_volume_controls)
        self.player_page_volume_down_button.setObjectName(u"player_page_volume_down_button")
        self.player_page_volume_down_button.setIcon(icon9)
        self.player_page_volume_down_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.player_page_volume_down_button)

        self.player_page_volume_slider = QSlider(self.player_page_volume_controls)
        self.player_page_volume_slider.setObjectName(u"player_page_volume_slider")
        self.player_page_volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_22.addWidget(self.player_page_volume_slider)

        self.player_page_volume_up_button = QToolButton(self.player_page_volume_controls)
        self.player_page_volume_up_button.setObjectName(u"player_page_volume_up_button")
        self.player_page_volume_up_button.setIcon(icon10)
        self.player_page_volume_up_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.player_page_volume_up_button)

        self.horizontalSpacer_4 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_4)


        self.verticalLayout_32.addWidget(self.player_page_volume_controls)


        self.horizontalLayout_10.addWidget(self.player_page_container)


        self.verticalLayout_22.addWidget(self.player_page_content)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_8)


        self.horizontalLayout.addWidget(self.player_page_contents)

        self.stackedWidget.addWidget(self.player_page)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.home_button.setDefault(False)
        self.pages_widget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"  Browse", None))
        self.library_button.setText(QCoreApplication.translate("MainWindow", u"  Library", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"  Profile", None))
        self.player_thumbnail.setText("")
        self.player_song_label.setText(QCoreApplication.translate("MainWindow", u"Song Title", None))
        self.player_artist_label.setText(QCoreApplication.translate("MainWindow", u"Artist Name", None))
        self.player_startdur_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.player_enddur_label.setText(QCoreApplication.translate("MainWindow", u"-99:99", None))
        self.sidebar_player_shuffle_button.setText("")
        self.sidebar_player_previous_button.setText("")
        self.sidebar_player_play_pause_button.setText("")
        self.sidebar_player_next_button.setText("")
        self.sidebar_player_loop_button.setText("")
        self.volume_down_button.setText("")
        self.volume_up_button.setText("")
        self.recent_label.setText(QCoreApplication.translate("MainWindow", u"Recently Played", None))
        self.recommend_label.setText(QCoreApplication.translate("MainWindow", u"Songs that you might like", None))
        self.categories_label.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"What do you want to listen to?", None))
        self.search_button.setText("")
        self.recent_searches_label.setText(QCoreApplication.translate("MainWindow", u"Recent Searches", None))
        self.no_recent_searches_label.setText(QCoreApplication.translate("MainWindow", u"You have no recent searches.", None))
        self.song_result_label.setText(QCoreApplication.translate("MainWindow", u"Songs", None))
        self.album_result_label.setText(QCoreApplication.translate("MainWindow", u"Albums", None))
        self.library_title_label.setText(QCoreApplication.translate("MainWindow", u"Your Library", None))
        self.add_playlist_button.setText("")
        self.no_playlists_label.setText(QCoreApplication.translate("MainWindow", u"You have no playlists.", None))
        self.profile_title_label.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.user_profile_button.setText(QCoreApplication.translate("MainWindow", u"  Profile Name", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.playlist_name_label.setText(QCoreApplication.translate("MainWindow", u"Playlist Name", None))
        self.playlist_edit_button.setText("")
        self.playlist_shuffle_button.setText("")
        self.playlist_play_button.setText("")
        self.playlist_no_songs_label.setText(QCoreApplication.translate("MainWindow", u"This playlist has no songs.", None))
        self.settings_theme_page_label_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.about_us_label.setText(QCoreApplication.translate("MainWindow", u"About Music Streaming Service", None))
        self.about_us_2.setText(QCoreApplication.translate("MainWindow", u"Music Streaming Service is a project developed as part of the 01286232 Software Engineering Principles course in the second semester of the second year of the Software Engineering program at King Mongkut's Institute of Technology Ladkrabang.", None))
        self.team_member_label.setText(QCoreApplication.translate("MainWindow", u"Team Members", None))
        self.member.setText(QCoreApplication.translate("MainWindow", u"65011466    Phyo Thi Khaing", None))
        self.member_2.setText(QCoreApplication.translate("MainWindow", u"65011514    Salinporn Rattanaprapaporn", None))
        self.member_3.setText(QCoreApplication.translate("MainWindow", u"65011527    Sirapob    Sriviriyahphaiboon", None))
        self.setting_language_page_label.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.apply_language_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.language_label.setText(QCoreApplication.translate("MainWindow", u"Choose Your Language", None))
        self.language_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English (US)", None))
        self.language_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Thai", None))

        self.settings_theme_page_label.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.apply_theme_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.current_theme_label.setText(QCoreApplication.translate("MainWindow", u"Theme Options", None))
        self.theme_comboBox_.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))

        self.theme_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.generic_title.setText(QCoreApplication.translate("MainWindow", u"Untitled Page", None))
        self.login_page_label.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.login_email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.login_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.remember_checkbox.setText("")
        self.remember_label.setText(QCoreApplication.translate("MainWindow", u"Remember me", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.sign_up_label.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? ", None))
        self.sign_up_button.setText(QCoreApplication.translate("MainWindow", u"Click here to sign up", None))
        self.register_page_label.setText(QCoreApplication.translate("MainWindow", u"Create Your Account", None))
        self.register_email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.display_name_label.setText(QCoreApplication.translate("MainWindow", u"Display Name", None))
        self.register_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.register_confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.sign_in_label.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.sign_in_button.setText(QCoreApplication.translate("MainWindow", u"Click here to Log in", None))
        self.player_page_back_button.setText("")
        self.player_page_playlist_label.setText(QCoreApplication.translate("MainWindow", u"Playlist Name", None))
        self.share_button.setText("")
        self.player_page_thumbnail.setText("")
        self.player_page_song_label.setText(QCoreApplication.translate("MainWindow", u"Song Title", None))
        self.player_page_artist_label.setText(QCoreApplication.translate("MainWindow", u"Artist Name", None))
        self.player_page_startdur_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.player_page_enddur_label.setText(QCoreApplication.translate("MainWindow", u"-99:99", None))
        self.player_page_shuffle_button.setText("")
        self.player_page_previous_button.setText("")
        self.player_page_play_pause_button.setText("")
        self.player_page_next_button.setText("")
        self.player_page_loop_button.setText("")
        self.player_page_volume_down_button.setText("")
        self.player_page_volume_up_button.setText("")
    # retranslateUi

