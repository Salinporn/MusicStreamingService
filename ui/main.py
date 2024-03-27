from PySide6.QtWidgets import (
    QWidget, QMainWindow, QApplication,
    QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy,
    QPushButton, QToolButton,
    QLabel)
from PySide6.QtGui import (QIcon, QCursor, QPixmap)
from PySide6.QtCore import (Qt, QSize)
from ui.main_ui import Ui_MainWindow
import sys

from backend.playlist import Playlist

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # switching pages
        self.home_button.clicked.connect(lambda: self.pages_widget.setCurrentIndex(0))
        self.browse_button.clicked.connect(lambda: self.pages_widget.setCurrentIndex(1))
        self.library_button.clicked.connect(lambda: self.pages_widget.setCurrentIndex(2))
        self.profile_button.clicked.connect(lambda: self.pages_widget.setCurrentIndex(3))
        
        # setup
        self.setup_home_page()
        self.setup_browse_page()
        self.setup_library_page()
        self.setup_profile_page()

    # -- home page --
    def setup_home_page(self):
        self.recent_contents.setLayout(QVBoxLayout())
        self.recommend_contents.setLayout(QHBoxLayout())
        
        # -- TEST --
        self.recent_contents.layout().addWidget(SmallThumbnailItem("test", "assets/images/1989.jpg"))

        self.recommend_contents.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.recommend_contents.layout().addWidget(BigThumbnailItem(
            heading="heading",
            subheading="subheading",
            image_path="assets/images/1989.jpg"
        ))

    # -- browse page --
    def setup_browse_page(self):
        self.search_button.clicked.connect(self.search)
        self.recent_searches = []
        
    def search_query(self, query):
        print(f"query: {query}")
        
    def search(self):
        query = self.search_bar.text()
        
        result = self.search_query(query)
        
        self.add_recent_search(query)
        
    def add_recent_search(self, query: str):
        if len(self.recent_searches) == 0:
            self.no_recent_searches_label.hide()
        
        item = RecentSearchItem(query, self)
        self.recent_searches.append(item)
        self.recent_searches_widget.layout().insertWidget(0, item)
        if len(self.recent_searches) > 5:
            self.remove_recent_search(self.recent_searches[0])
    
    def remove_recent_search(self, recent_search_item: "RecentSearchItem"):
        recent_search_item.deleteLater()
        self.recent_searches.remove(recent_search_item)
        self.recent_searches_widget.layout().removeWidget(recent_search_item)

        if len(self.recent_searches) == 0:
            self.no_recent_searches_label.show()
            
    # -- library page --
    def setup_library_page(self):
        self.library_playlists = []
        
        # self.add_playlist_button.clicked.connect()
        
        
        # --TEST--
        self.add_playlist_button.clicked.connect(lambda: self.add_playlist(Playlist("test", "assets/images/1989.jpg")))

    
    def add_playlist(self, playlist: Playlist):
        if len(self.library_playlists) == 0:
            self.no_playlists_label.hide()
        
        item = LibraryItem(playlist.name, playlist.image_path)
        self.library_playlists.append(item)
        self.library_contents.layout().addWidget(item)

    # -- profile page --
    def setup_profile_page(self):
        # todo: change page when clicked
        self.settings_contents.layout().addWidget(ProfileItem("Languages", parent=self))
        self.settings_contents.layout().addWidget(ProfileItem("Theme", parent=self))
        self.settings_contents.layout().addWidget(ProfileItem("Notifications", parent=self))
        self.settings_contents.layout().addWidget(ProfileItem("About", parent=self))
        self.settings_contents.layout().addWidget(ProfileItem("Log Out", parent=self))
        
# -- components --
class SmallThumbnailItem(QPushButton):
    def __init__(self, text: str, image_path: str, parent=None):
        super().__init__(parent)

        # self.setObjectName("recent_playlist")
        self.setMinimumSize(QSize(250, 64))
        self.setText("  " + text)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)

        icon = QIcon()
        icon.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(64, 64))

        self.setProperty("class", "SmallThumbnailItem")
        self.setStyleSheet("""
            .SmallThumbnailItem {
                background-color: #1e1e1e;
                font-size: 16px;
                padding: 0px;
                text-align: left;
                color: #dddddd;
                border-radius: 5px;
            }
        
            .SmallThumbnailItem:hover {
                color: #ffffff;
                background-color: #303030;
            }
        """)

class BigThumbnailItem(QPushButton):
    def __init__(self, heading="No Title", subheading="", image_path="", parent=None):
        super().__init__(parent)

        self.setFixedSize(QSize(140, 180))
        self.setCursor(Qt.PointingHandCursor)
        self.setAutoFillBackground(False)

        icon_label = QLabel(self)
        icon_label.setFixedSize(120, 120)
        icon_label.setAlignment(Qt.AlignCenter)
        if image_path:
            pixmap = QPixmap(image_path).scaled(120, 120)
            icon_label.setPixmap(pixmap)

        heading_label = QLabel(self)
        heading_label.setText(heading)
        heading_label.setAlignment(Qt.AlignLeft)
        heading_label.setStyleSheet("color: #ffffff; font-size: 14px; background-color: transparent;")

        subheading_label = QLabel(self)
        subheading_label.setText(subheading)
        subheading_label.setAlignment(Qt.AlignLeft)
        subheading_label.setStyleSheet("color: #cccccc; font-size: 12px; background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.addWidget(icon_label)
        layout.addWidget(heading_label)
        if subheading:
            layout.addWidget(subheading_label)
        self.setLayout(layout)
        
        self.setProperty("class", "BigThumbnailItem")
        self.setStyleSheet("""
            .BigThumbnailItem {
                background-color: #1e1e1e;
                font-size: 14px;
                padding: 0px;
                text-align: center;
                border-radius: 5px;
            }
            .BigThumbnailItem:hover {
                color: #ffffff;
                background-color: #303030;
            }
        """)

        self.clicked.connect(self.show_playlist)

    def show_playlist(self):
        print("clicked")

class LongLabelButton(QWidget):
    def __init__(self, text: str, parent: MainWindow = None) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.setMinimumHeight(40)
                
        self.label = QPushButton(text)
        self.label.setMinimumHeight(35)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

        self.tool_button = QToolButton(self)
        self.tool_button.setCursor(QCursor(Qt.PointingHandCursor))

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.label)
        layout.addWidget(self.tool_button)
        
        self.setLayout(layout)
        
        self.setProperty("class", "LongLabelButton")
        self.setStyleSheet("""
            .LongLabelButton QPushButton {
                text-align: left;
                border: 0;
            }
        """)

# -- browse page --
class RecentSearchItem(LongLabelButton):
    def __init__(self, text: str, parent: MainWindow = None) -> None:
        super().__init__(text, parent)
        
        self.label.clicked.connect(lambda: parent.search_query(text))
        
        self.tool_button.setIcon(QIcon(":/resources/assets/images/cancel.png"))
        self.tool_button.clicked.connect(lambda: parent.remove_recent_search(self))

# -- library page --
class LibraryItem(SmallThumbnailItem):
    def __init__(self, text: str, image_path: str, parent=None):
        super().__init__(text, image_path, parent)
        
        

# -- profile page --
class ProfileItem(LongLabelButton):
    def __init__(self, text: str, parent: MainWindow = None) -> None:
        super().__init__(text, parent)
        
        self.tool_button.setIcon(QIcon(":/resources/assets/images/enter.png"))

def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    run()