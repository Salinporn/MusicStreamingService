from PySide6.QtWidgets import (
    QWidget, QMainWindow, QApplication, QDialog,
    QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy, QLayout,
    QPushButton, QToolButton, QMenu, QLineEdit, QFileDialog,
    QLabel, QMessageBox)
from PySide6.QtGui import (QIcon, QCursor, QRegion, QMouseEvent, QPixmap, QImage, QAction)
from PySide6.QtCore import (
    QObject, Qt, QSize, QUrl, QEventLoop, QUrlQuery, QTemporaryFile, QCoreApplication,
    QTimer, Signal, QByteArray, QDateTime, QDir, QThread, QFile, QByteArray, QBuffer, QIODevice,
    QJsonDocument, QSettings, QProcess)
from PySide6.QtNetwork import (
    QNetworkCookieJar, QNetworkCookie,
    QNetworkAccessManager, QHttpMultiPart, QHttpPart,
    QNetworkRequest, QNetworkReply,
    QSslConfiguration, QSsl)
from PySide6.QtMultimedia import (QMediaPlayer, QAudioOutput)
from ui.flow_layout import FlowLayout
from ui.main_ui import Ui_MainWindow
from ui.custom_widgets import ClickableLabel
from types import FunctionType
import sys
import base64
import random

from backend.models import *

class MainWindow(QMainWindow, Ui_MainWindow):
    SERVER_URL = "http://localhost/"
    SERVER_PORT = 8000
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Music Streaming Client")
        
        # switching pages
        self.home_button.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.home_page))
        self.browse_button.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.browse_page))
        self.library_button.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.library_page))
        self.profile_button.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.profile_page))
        
        self.sign_in_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login_page))
        self.sign_up_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.register_page))
                
        # setup
        self.setup_settings()
        self.setup_networking()
        self.setup_home_page()
        self.setup_browse_page()
        self.setup_library_page()
        self.setup_profile_page()
        self.setup_player()
        self.setup_playlists()
        self.setup_generic_page()
        
        self.setup_login()
        self.setup_register()

    def clear_widget(self, widget: QWidget):
        for i in reversed(range(widget.layout().count())): 
            widget.layout().itemAt(i).widget().setParent(None)

    # ----------------
    # -- NETWORKING --
    # ----------------
    def setup_networking(self):
        self.network_manager = QNetworkAccessManager(self)
        self.ssl_config = QSslConfiguration()
        self.ssl_config.setProtocol(QSsl.SslProtocol.TlsV1_2OrLater)
        
        self.cookie_jar = QNetworkCookieJar()
        self.network_manager.setCookieJar(self.cookie_jar)

    def perform_get_request_sync(self, url: str, data: dict=None, headers: dict=None) -> QNetworkReply:
        request_url = QUrl(url)
        request_url.setPort(self.SERVER_PORT)
        
        if data is not None:
            query_params = QUrlQuery()
            for key, value in data.items():
                query_params.addQueryItem(key, value)
            request_url.setQuery(query_params.query())

        request = QNetworkRequest(request_url)
        if headers:
            for key, value in headers.items():
                request.setHeader(key, value)

        request.setSslConfiguration(self.ssl_config)
                
        reply = self.network_manager.get(request)
        
        # wait for reply...
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec()
        
        # check for errors
        self.check_reply_for_errors(reply)
        
        return reply

    def perform_post_request_sync(self, url: str, data: dict | QByteArray=None, headers: dict=None, is_json: bool=True) -> QNetworkReply:
        request_url = QUrl(url)
        request_url.setPort(self.SERVER_PORT)

        request = QNetworkRequest(request_url)
        request.setSslConfiguration(self.ssl_config)
        
        if headers:
            for key, value in headers.items():
                request.setHeader(key, value)
        
        if data is None:
            data = {}
        if is_json:
            request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
            request_body: QByteArray = QJsonDocument(data).toJson()
        else:
            request_body: QByteArray = data

        reply = self.network_manager.post(request, request_body)
        
        # wait for reply...
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec()
        
        # check for errors
        self.check_reply_for_errors(reply)
        
        return reply

    def check_reply_for_errors(self, reply: QNetworkReply):
        err = reply.error()
        if err == QNetworkReply.NetworkError.AuthenticationRequiredError:
            print("Session cookie invalid, logging out...")
            self.handle_logout()
        elif err != QNetworkReply.NetworkError.NoError:
            print(f"Error: {err}")
            print(reply.errorString())
            
            print(QJsonDocument.fromJson(reply.readAll()).object())
            
            raise Exception(err)

    def perform_get_request_async(self, url: str, callback: FunctionType, data: dict=None, headers: dict=None):
        request_url = QUrl(url)
        request_url.setPort(self.SERVER_PORT)

        request = QNetworkRequest(request_url)
        request.setSslConfiguration(self.ssl_config)
        
        if headers:
            for key, value in headers:
                request.setHeader(key, value)
        
        if data is not None:
            query_params = QUrlQuery()
            for key, value in data.items():
                query_params.addQueryItem(key, value)
            request_url.setQuery(query_params)

        self.network_manager.finished.connect(lambda reply: self.handle_response(reply, callback))
        self.network_manager.get(request)
        
    def perform_post_request_async(self, url: str, callback: FunctionType, data: dict=None, headers: dict=None):
        request_url = QUrl(url)
        request_url.setPort(self.SERVER_PORT)

        request = QNetworkRequest(request_url)
        request.setSslConfiguration(self.ssl_config)
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        if headers:
            for key, value in headers:
                request.setHeader(key, value)
                
        if data is None:
            data = {}
        request_body = QJsonDocument(data).toJson()
        
        # maybe? check for errors and call callback
        self.network_manager.finished.connect(lambda reply: self.handle_response(reply, callback))
        
        request_body = QJsonDocument(data).toJson()
        self.network_manager.post(request, request_body)
        
    def handle_response(self, reply: QNetworkReply, callback: FunctionType):
        self.check_reply_for_errors(reply)
        
        callback(reply)
        
        reply.deleteLater()
        
        self.network_manager.finished.disconnect()

    # -----------
    # -- LOGIN --
    # -----------
    LOGIN_ENDPOINT = "client-login"
    USER_DATA_ENDPOINT = "user-data"
    def setup_login(self):
        self.login_button.clicked.connect(self.handle_login)
        self.session = None

        # if we have a saved session cookie, use it
        self.settings.beginGroup("Authentication")

        loaded_cookies = QNetworkCookie.parseCookies(self.settings.value("session"))
        
        if loaded_cookies:
            self.session = loaded_cookies[0]
            
            # check if cookie is expired
            time_to_expiry = QDateTime.currentDateTimeUtc().secsTo(self.session.expirationDate())
            print(time_to_expiry)
            if time_to_expiry <= 0:
                self.settings.setValue("session", None)
                self.session = None
            else:
                # add session cookie to cookie jar
                self.network_manager.cookieJar().insertCookie(self.session)
                self.settings.endGroup()
                
                self.on_authenticated()
        
        if not self.session:
            self.settings.endGroup()
            self.stackedWidget.setCurrentWidget(self.login_page)

    def handle_login(self):
        data = {
            "email": self.login_email_input.text(),
            "password": self.login_password_input.text(),
            "remember": self.remember_checkbox.isChecked()
        }
        self.login_button.setDisabled(True)
        reply = self.perform_post_request_sync(self.SERVER_URL + self.LOGIN_ENDPOINT, data)
    
        cookies = self.cookie_jar.allCookies()

        session_cookie = None
        for cookie in cookies:
            if cookie.name() == "session":
                session_cookie = cookie
                break

        if session_cookie:
            # authenticated successfully
            
            self.session = session_cookie
            
            # store cookie with persistence            
            self.settings.beginGroup("Authentication")
            self.settings.setValue("session", session_cookie.toRawForm())
            self.settings.endGroup()

            self.on_authenticated()
        else:
            pass
        
        self.login_email_input.clear()
        self.login_password_input.clear()
        self.remember_checkbox.setChecked(False)
        
        self.login_button.setDisabled(False)
        
        reply.deleteLater()

    def handle_logout(self):
        self.settings.beginGroup("Authentication")
        self.settings.setValue("session", None)
        self.settings.endGroup()
        
        self.settings.sync()
        
        # restart app
        QCoreApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

    # -------------
    # -- LOADING --
    # -------------
    def get_user_data(self):
        reply = self.perform_get_request_sync(self.SERVER_URL + self.USER_DATA_ENDPOINT)
        
        user_data = QJsonDocument.fromJson(reply.readAll()).object()

        reply.deleteLater()
        
        return user_data
    
    def data_to_pixmap(self, data: QByteArray):
        pixmap = QPixmap()
        pixmap.loadFromData(data, format=None, flags=Qt.ImageConversionFlag.AutoColor)
        return pixmap
    
    ALBUM_IMAGE_ENDPOINT = "get-album-image/"
    ALBUMS_ENDPOINT = "get-album/"
    def load_song(self, song_id):
        # load data and image
        
        song_reply = self.perform_get_request_sync(
            url=self.SERVER_URL + self.SONGS_ENDPOINT + song_id,
            data=None
        )
        song_data = song_reply.readAll()
        response_json = QJsonDocument.fromJson(song_data).object()

        """
        response_json:
            uuid
            title
            genres
            artists
            album
            duration
        """
        if not response_json:
            return
        
        song = Song(
            uuid=response_json["uuid"],
            title=response_json["title"],
            artists=response_json["artists"],
            album=response_json["album"],
            duration=response_json["duration"]
        )
        
        self.songs[song_id] = song
        
        if response_json["album"] is None:
            # load placeholder image
            image = QPixmap(":/resources/assets/images/song_placeholder.jpg")
            song.set_image(image)
        else:
            # load album image
            if response_json["album"] not in self.albums:
                self.load_album(response_json["album"])
                
        return song
    
    def load_album(self, album_id):
        album_reply = self.perform_get_request_sync(
            url=self.SERVER_URL + self.ALBUMS_ENDPOINT + album_id,
            data=None
        )
        album_data = album_reply.readAll()
        response_json = QJsonDocument.fromJson(album_data).object()

        """
        response_json:
            uuid
            title
            artists
            songs
        """

        album = Album(
            uuid=response_json["uuid"],
            title=response_json["title"],
            artists=response_json["artists"],
            songs=response_json["songs"]
        )
        
        for song_id in response_json["songs"]:
            if song_id not in self.songs:
                self.load_song(song_id)
        
        self.albums[album_id] = album
        
        # load album image
        album_image_reply = self.perform_get_request_sync(
            url=self.SERVER_URL + self.ALBUM_IMAGE_ENDPOINT + album_id,
            data=None
        )
        
    # def load_album_image(self, album_image_reply: QNetworkReply, album: Album):
        image_data = album_image_reply.readAll()
        image = self.data_to_pixmap(image_data)
        
        album.set_image(image)
        
        for song_id in album.get_songs():
            self.songs[song_id].set_image(image)
    
        return album
    
    CATEGORIES_ENDPOINT = "get-categories/"
    SONGS_ENDPOINT = "get-songs/"
    PLAYLIST_IMAGE_ENDPOINT = "get-playlist-image/"
    RECOMMENDED_SONGS_ENDPOINT = "get-recommended/"
    def load_home_page(self):
        self.pages_widget.setCurrentIndex(0)
        
        self.recommend_contents.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.categories_contents.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # recently played
        recently_played = self.user.get_recently_played()

        if len(recently_played) > 6:
            recently_played = recently_played[:6]
            
        for playlist in recently_played:
            playlist_obj = self.playlists[playlist]
            self.recent_contents.layout().addWidget(
                SmallPlaylistItem(playlist_obj, self)
            )
            
        # recommended songs
        reply = self.perform_get_request_sync(self.SERVER_URL + self.RECOMMENDED_SONGS_ENDPOINT)
        response_data = reply.readAll()
        response_json = QJsonDocument.fromJson(response_data).object()

        recommended_songs = response_json["results"]
        
        for song_id in recommended_songs:
            if song_id not in self.songs:
                self.load_song(song_id)
            
            self.recommend_contents.layout().addWidget(
                BigSongItem(self.songs[song_id], parent=self)
            )

        # categories
        reply = self.perform_get_request_sync(self.SERVER_URL + self.CATEGORIES_ENDPOINT)
        response_data = reply.readAll()
        response_json = QJsonDocument.fromJson(response_data).object()

        categories = response_json["data"]
        
        for category in categories:
            image_reply = self.perform_get_request_sync(self.SERVER_URL + self.CATEGORIES_ENDPOINT + category["uuid"], None)
            image_data = image_reply.readAll()
        
            category["image"] = self.data_to_pixmap(image_data)

            for song in category["songs"]:
                if song not in self.songs:
                    self.load_song(song)

            category = Category(**category)
            self.categories_contents.layout().addWidget(
                CategoryItem(category, self)
            )
        
    def update_home_page(self):
        self.clear_home_page()
        
        # update recently played
        recently_played = self.user.get_recently_played()
        
        if len(recently_played) > 6:
            recently_played = recently_played[:6]
        
        for playlist in recently_played:
            playlist_obj = self.playlists[playlist]
            self.recent_contents.layout().addWidget(
                SmallPlaylistItem(playlist_obj, self)
            )
        
        # update recommended songs
        reply = self.perform_get_request_sync(self.SERVER_URL + self.RECOMMENDED_SONGS_ENDPOINT)
        response_data = reply.readAll()
        response_json = QJsonDocument.fromJson(response_data).object()

        recommended_songs = response_json["results"]
        
        for song_id in recommended_songs:
            if song_id not in self.songs:
                self.load_song(song_id)
            
            self.recommend_contents.layout().addWidget(
                BigSongItem(self.songs[song_id], parent=self)
            )

    def clear_home_page(self):
        self.clear_widget(self.recent_contents)
        self.clear_widget(self.recommend_contents)
                
    def on_authenticated(self):
        # authenticated successfully, now use session cookie to get info
        
        user_data = self.get_user_data()
        
        self.songs: dict[str, Song] = {}
        self.playlists: dict[str, Playlist] = {}
        self.categories: dict[str, Category] = {}
        self.albums: dict[str, Album] = {}
        
        playlists = []
        for playlist in user_data["playlists"]:
            playlists.append(playlist["uuid"])
            if playlist["uuid"] not in self.playlists:
                playlist_obj = Playlist(
                    uuid=playlist["uuid"],
                    name=playlist["name"],
                    author=user_data["name"],
                    songs=playlist["songs"]
                )
                
                image_reply = self.perform_get_request_sync(self.SERVER_URL + self.PLAYLIST_IMAGE_ENDPOINT + playlist["uuid"], None)
                image_data = image_reply.readAll()
                
                if image_data == b"null":
                    image = QPixmap(":/resources/assets/images/playlist_placeholder.png")
                else:
                    image = self.data_to_pixmap(image_data)
                
                playlist_obj.set_image(image)
                
                self.playlists[playlist["uuid"]] = playlist_obj

                for song in playlist_obj.get_songs():
                    self.songs[song] = self.load_song(song)
        
        recently_played = []
        for playlist in user_data["recently_played"]:
            if playlist["uuid"] not in recently_played:
                recently_played.append(playlist["uuid"])
            
        self.user = User(
            uuid=user_data["uuid"],
            name=user_data["name"],
            email=user_data["email"],
            playlists=playlists,
            recently_played=recently_played
        )
        
        self.user_profile_button.setText(self.user.get_name())
        
        self.load_home_page()
        self.load_library_page()

        self.stackedWidget.setCurrentWidget(self.main_page)

    # --------------
    # -- REGISTER --
    # --------------
    REGISTER_ENDPOINT = "client-register"
    def setup_register(self):
        self.register_button.clicked.connect(self.handle_register)

    def handle_register(self):
        data = {
            "email": self.register_email_input.text(),
            "name": self.display_name_input.text(),
            "password": self.register_password_input.text(),
            "repassword": self.register_confirm_password_input.text()
        }
        self.register_button.setDisabled(True)
        
        reply = self.perform_post_request_sync(self.SERVER_URL + self.REGISTER_ENDPOINT, data)
        response_data = reply.readAll()
        response_json = QJsonDocument.fromJson(response_data).object()

        if reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute) == 200:
            self.stackedWidget.setCurrentWidget(self.login_page)
        
        self.register_button.setDisabled(False)
        
        reply.deleteLater()

    # ---------------
    # -- HOME PAGE --
    # ---------------
    def setup_home_page(self):
        self.recent_contents.setLayout(QHBoxLayout())
        self.recommend_contents.setLayout(QHBoxLayout())
        self.categories_contents.setLayout(QHBoxLayout())
        
    # -----------------
    # -- BROWSE PAGE --
    # -----------------
    def setup_browse_page(self):
        self.search_button.clicked.connect(self.search)
        self.recent_searches = []
        
        self.song_result_scrollarea_contents.setLayout(FlowLayout())
        self.album_result_scrollarea_contents.setLayout(FlowLayout())
        self.song_suggestions_scrollarea_contents.setLayout(FlowLayout())
        
        self.song_suggestions_section.hide()

    SEARCH_ENDPOINT = "search"
    def search_query(self, query):
        
        reply = self.perform_get_request_sync(self.SERVER_URL + self.SEARCH_ENDPOINT, data={"query": query})
        
        reply_data = reply.readAll()
        reply_json = QJsonDocument.fromJson(reply_data).object()
        
        return reply_json
        
    def perform_search_query(self, query):
        reply_json = self.search_query(query)
        
        results = reply_json["results"]
        suggestions = reply_json["suggestions"]
        
        """
        results:
            album
            artists
            title
            uuid
        """
        
        self.display_search_results(results, suggestions)
        
    def display_search_results(self, results: list[dict[str]], suggestions: list[dict[str]]):
        self.clear_search_results()

        song_ids: list[str] = []
        album_ids: list[str] = []
        for result in results:
            song_uuid = result["uuid"]
            if song_uuid not in song_ids:
                song_ids.append(song_uuid)
            if "album" in result:
                album_uuid = result["album"]
                if album_uuid not in album_ids:
                    album_ids.append(album_uuid)
        
        suggested_song_ids: list[str] = []
        for suggested_song in suggestions:
            song_uuid = suggested_song["uuid"]
            if song_uuid not in suggested_song_ids:
                suggested_song_ids.append(song_uuid)
        
        for song_id in song_ids:
            if song_id not in self.songs:
                self.load_song(song_uuid)
            self.add_song_result(song_id)

        for album_id in album_ids:
            if album_id not in self.albums:
                self.load_album(album_id)
            self.add_album_result(album_id)
        
        for song_id in suggested_song_ids:
            if song_id not in self.songs:
                self.load_song(song_uuid)
            self.add_suggested_song_result(song_id)
        
        self.no_songs_found_label.hide()
        if len(song_ids) > 5:
            self.song_result_container.setFixedHeight(440)
        elif len(song_ids) >= 1:
            self.song_result_container.setFixedHeight(220)
        else:
            self.song_result_container.setFixedHeight(100)            
            self.no_songs_found_label.show()
        
        self.no_albums_found_label.hide()
        if len(album_ids) > 5:
            self.album_result_container.setFixedHeight(440)
        elif len(album_ids) >= 1:
            self.album_result_container.setFixedHeight(220)
        else:
            self.album_result_container.setFixedHeight(100)
            self.no_albums_found_label.show()
        
        self.song_suggestions_section.show()
        if len(suggested_song_ids) > 5:
            self.song_suggestions_container.setFixedHeight(440)
        elif len(album_ids) >= 1:
            self.song_suggestions_container.setFixedHeight(220)
        else:
            self.song_suggestions_section.hide()
            
    def add_song_result(self, song_id: str):
        layout = self.song_result_scrollarea_contents.layout()

        song = self.songs[song_id]
        layout.addWidget(BigSongItem(song, self))

    def add_album_result(self, album_id: str):
        layout = self.album_result_scrollarea_contents.layout()

        album = self.albums[album_id]
        layout.addWidget(AlbumItem(album, self))
            
    def add_suggested_song_result(self, song_id: str):
        layout = self.song_suggestions_scrollarea_contents.layout()

        song = self.songs[song_id]
        layout.addWidget(BigSongItem(song, self))
        
    def search(self):        
        query = self.search_bar.text()
        
        # self.result_section.show()
        
        self.perform_search_query(query)
        
        self.add_recent_search(query)

    def clear_search_results(self):
        self.clear_widget(self.song_result_scrollarea_contents)
        self.clear_widget(self.album_result_scrollarea_contents)
        self.clear_widget(self.song_suggestions_scrollarea_contents)

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

    # ------------------
    # -- LIBRARY PAGE --
    # ------------------
    ADD_USER_PLAYLIST_ENDPOINT = "add-playlist/"
    def setup_library_page(self):
        self.library_playlists: list[SmallPlaylistItem] = []
        
        self.add_playlist_button.clicked.connect(self.add_new_playlist)

    def load_library_page(self):
        for playlist in self.user.playlists:
            self.add_playlist(self.playlists[playlist])

    def add_new_playlist(self):
        reply = self.perform_post_request_sync(self.SERVER_URL + self.ADD_USER_PLAYLIST_ENDPOINT, None)
        
        reply_data = reply.readAll()
        reply_json = QJsonDocument.fromJson(reply_data).object()

        playlist = Playlist(reply_json["uuid"], reply_json["name"], self.user.get_name(), None, QPixmap(":/resources/assets/images/playlist_placeholder.png"))
        
        self.user.playlists.append(reply_json["uuid"])
        self.playlists[reply_json["uuid"]] = playlist
        self.add_playlist(playlist)

    def add_playlist(self, playlist: Playlist):
        if len(self.library_playlists) == 0:
            self.no_playlists_label.hide()
        
        item = LibraryItem(playlist=playlist, parent=self)

        self.library_playlists.append(item)
        self.library_contents.layout().addWidget(item)
        
    def clear_library_page(self):
        for i in reversed(range(len(self.library_playlists))):
            self.recent_contents.layout().removeWidget(self.library_playlists[i])
            self.library_playlists[i].deleteLater()
            self.library_playlists.pop(i)
        
        self.no_playlists_label.show()

    def update_library_page(self):
        self.clear_library_page()
        
        self.load_library_page()

    # ------------------
    # -- PROFILE PAGE --
    # ------------------
    def setup_profile_page(self):
        self.settings_contents.layout().addWidget(
            ProfileItem(
                text="Languages",
                parent=self,
                on_click=lambda: self.open_page_with_back_button(self.settings_language_page)
            )
        )
        self.settings_contents.layout().addWidget(
            ProfileItem(
                text="Theme",
                parent=self,
                on_click=lambda: self.open_page_with_back_button(self.settings_theme_page)
            )
        )
        self.settings_contents.layout().addWidget(
            ProfileItem(
                text="About",
                parent=self,
                on_click=lambda: self.open_page_with_back_button(self.settings_about_page)
            )
        )
        self.settings_contents.layout().addWidget(
            ProfileItem(
                text="Log Out",
                parent=self,
                on_click=self.handle_logout
            )
        )

    def open_page_with_back_button(self, page: QWidget, previous_page: QWidget=None):
        if previous_page is None:
            previous_page = self.pages_widget.currentWidget()
            
        self.pages_widget.setCurrentWidget(page)
        
        back_button = QToolButton(page)
        back_button.setGeometry(10, 10, 40, 40)
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.setIcon(QIcon(":resources/assets/images/go_back.png"))
        back_button.setStyleSheet("background-color: RGBA(0,0,0,0)")
        back_button.show()

        back_button.clicked.connect(lambda: self.pages_widget.setCurrentWidget(previous_page))

    # --------------
    # -- SETTINGS --
    # --------------
    def setup_settings(self):
        self.settings = QSettings()

    # ------------
    # -- PLAYER --
    # ------------
    # AUDIO_ENDPOINT = "stream-audio/"
    AUDIO_ENDPOINT = "get-audio/"

    UPDATE_INTERVAL = 100
    
    DEFAULT_PLAYER_TITLE = "Not Playing"
    DEFAULT_PLAYER_ARTIST = ""
    DEFAULT_START_DUR = "0:00"
    DEFAULT_END_DUR = "-99:99"
    def setup_player(self):
        # set up media player
        self.audio_output = QAudioOutput()
        
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status_changed)
        
        # player ui + logic
        self.is_playing = False
        self.cur_song = None
        self.cur_playlist = None
        self.cur_playlist_index = -1
        
        self.is_slider_pressed = False
        self.was_playing = False

        self.is_shuffle_on = False
        self.is_loop_on = False

        self.settings.beginGroup("player")

        # shuffle
        self.shuffle_order = None
        
        self.sidebar_player_shuffle_button.clicked.connect(self.toggle_shuffle)
        self.player_page_shuffle_button.clicked.connect(self.toggle_shuffle)

        shuffle_on: str = self.settings.value("shuffle")
        if shuffle_on:
            self.is_shuffle_on = bool(shuffle_on.title())
            self.sidebar_player_shuffle_button.setChecked(self.is_shuffle_on)
            self.player_page_shuffle_button.setChecked(self.is_shuffle_on)

        # loop
        self.sidebar_player_loop_button.clicked.connect(self.toggle_loop)
        self.player_page_loop_button.clicked.connect(self.toggle_loop)

        loop_on: str = self.settings.value("loop")
        print(loop_on)
        if loop_on:
            self.is_loop_on = bool(loop_on.title())
            self.sidebar_player_loop_button.setChecked(self.is_shuffle_on)
            self.player_page_loop_button.setChecked(self.is_shuffle_on)
            
        # volume
        slider_pos = self.settings.value("volume")
        
        self.settings.endGroup()

        if slider_pos:
            self.set_volume(int(slider_pos))
        else:
            self.set_volume(50)

        # sidebar
        self.player_thumbnail.setStyleSheet(self.player_thumbnail.styleSheet() + """\n
            border: none;
            margin: 0px;
            padding: 0px;                                    
        """)
        
        self.sidebar_player_play_pause_button.clicked.connect(self.toggle_pause_play)
        self.sidebar_player_previous_button.clicked.connect(self.previous_clicked)
        self.sidebar_player_next_button.clicked.connect(self.next_clicked)
        
        # player slider
        self.player_slider.sliderPressed.connect(self.slider_pressed)
        self.player_slider.valueChanged.connect(self.slider_value_changed)
        self.player_slider.sliderReleased.connect(self.slider_released)

        self.player_page_play_pause_button.clicked.connect(self.toggle_pause_play)
        self.player_page_previous_button.clicked.connect(self.previous_clicked)
        self.player_page_next_button.clicked.connect(self.next_clicked)
        
        self.player_page_slider.sliderPressed.connect(self.slider_pressed)
        self.player_page_slider.valueChanged.connect(self.slider_value_changed)
        self.player_page_slider.sliderReleased.connect(self.slider_released)
        
        # volume controls
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.volume_up_button.clicked.connect(self.volume_up)
        self.volume_down_button.clicked.connect(self.volume_down)
        
        self.player_page_volume_slider.valueChanged.connect(self.set_volume)
        self.player_page_volume_up_button.clicked.connect(self.volume_up)
        self.player_page_volume_down_button.clicked.connect(self.volume_down)
        
        # logic for updating player
        self.timer = QTimer(self)
        self.timer.setInterval(self.UPDATE_INTERVAL)
        self.timer.timeout.connect(self.update_player)
        
        # player page
        self.player_thumbnail.clicked.connect(self.open_player)
        
        self.clear_player()
    
    def clear_player(self):
        self.is_playing = False
        self.cur_song = None
        self.cur_playlist = None
        self.shuffle_order = None
        
        self.player_slider.setDisabled(True)
        self.player_page_slider.setDisabled(True)
    
        self.player_slider.setSliderPosition(0)
        self.player_page_slider.setSliderPosition(0)
    
        self.sidebar_player_play_pause_button.setCheckable(False)
        self.player_page_play_pause_button.setCheckable(False)
        
        self.player_song_label.setText(self.DEFAULT_PLAYER_TITLE)
        self.player_artist_label.setText(self.DEFAULT_PLAYER_ARTIST)
        self.player_startdur_label.setText(self.DEFAULT_START_DUR)
        self.player_enddur_label.setText(self.DEFAULT_END_DUR)
        self.player_thumbnail.setIcon(QIcon())
                
        self.player_page_song_label.setText(self.DEFAULT_PLAYER_TITLE)
        self.player_page_artist_label.setText(self.DEFAULT_PLAYER_ARTIST)
        self.player_page_startdur_label.setText(self.DEFAULT_START_DUR)
        self.player_page_enddur_label.setText(self.DEFAULT_END_DUR)
        self.player_page_thumbnail.setPixmap(QPixmap(":/resources/assets/images/thumbnail_placeholder.png"))
        self.player_page_playlist_label.setText("")
        
        self.timer.stop()

    def open_player(self):
        previous_page = self.stackedWidget.currentWidget()
        
        self.stackedWidget.setCurrentWidget(self.player_page)

        self.player_page_back_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(previous_page))
        if self.cur_song:
            self.player_page_song_label.setText(self.cur_song.title)
            self.player_page_artist_label.setText(self.cur_song.artists[0])

    def play_song(self, song: Song):
        if self.media_player.isPlaying():
            self.media_player.stop()
        
        self.cur_song = song
        
        self.sidebar_player_play_pause_button.setCheckable(True)
        self.player_page_play_pause_button.setCheckable(True)
        
        # set audio source
        self.player_slider.setDisabled(False)
        self.player_page_slider.setDisabled(False)
        
        # FIXME: this works but it's very slow; make async?
        reply = self.perform_get_request_sync(self.SERVER_URL + self.AUDIO_ENDPOINT + song.get_uuid())
        audio_data = reply.readAll()
        
        # write to temporary file
        self.temp_file = QTemporaryFile()
        self.temp_file.open()
        self.temp_file.write(audio_data)
        
        new_url = QUrl.fromLocalFile(self.temp_file.fileName())
        
        self.media_player.setSource(new_url)
        
        # set player ui to song info
        self.player_song_label.setText(song.title)
        self.player_artist_label.setText(", ".join(song.artists))

        self.player_thumbnail.setIcon(QIcon(song.image))
        self.player_page_thumbnail.setPixmap(song.image.scaled(350, 350))
        
        self.update_duration_text(song.get_duration())

    ADD_RECENTLY_PLAYED_ENDPOINT = "add-recently-played/"
    def play_playlist(self, playlist: Playlist, start_index=0, add_to_recent=True):
        if len(playlist.get_songs()) == 0:
            return
        
        # set shuffle order
        self.shuffle_order = list(range(len(playlist.get_songs())))
        random.shuffle(self.shuffle_order)
        
        if add_to_recent:
            # add to recently played
            self.perform_post_request_async(self.SERVER_URL + self.ADD_RECENTLY_PLAYED_ENDPOINT + playlist.get_uuid(), callback=lambda reply: None)
            if playlist.get_uuid() in self.user.recently_played:
                self.user.recently_played.remove(playlist.get_uuid())
            self.user.recently_played.insert(0, playlist.get_uuid())
            
            self.update_home_page()
        
        # play the playlist in sequence
        self.cur_playlist = playlist
        self.cur_playlist_index = start_index
        
        self.player_page_playlist_label.setText(self.cur_playlist.get_name())
        
        if self.is_shuffle_on:
            self.play_song(self.songs[self.cur_playlist.get_song_at_index(self.shuffle_order[self.cur_playlist_index])])
        else:
            self.play_song(self.songs[self.cur_playlist.get_song_at_index(self.cur_playlist_index)])
    
    def play_playlist_shuffle(self, playlist: Playlist, add_to_recent=True):
        self.is_shuffle_on = True
        self.play_playlist(playlist, add_to_recent=add_to_recent)

    def handle_media_status_changed(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.play()
        elif status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.cur_playlist:
                self.cur_playlist_index += 1
                if self.cur_playlist_index == len(self.cur_playlist.songs):
                    if self.is_loop_on:
                        self.cur_playlist_index = 0
                    else:
                        self.cur_playlist_index = -1
                        self.clear_player()
                        return
                
                if self.is_shuffle_on and self.shuffle_order:
                    random_index = self.shuffle_order[self.cur_playlist_index]
                    self.play_song(self.songs[self.cur_playlist.get_song_at_index(random_index)])
                else:
                    self.play_song(self.songs[self.cur_playlist.get_song_at_index(self.cur_playlist_index)])
            else:
                if self.is_loop_on:
                    self.play_song(self.cur_song)
                else:
                    self.clear_player()
        elif status == QMediaPlayer.MediaStatus.InvalidMedia:
            pass

    def pause(self):
        if self.cur_song is None:
            return
        self.media_player.pause()
        self.timer.stop()
        self.is_playing = False
    
    def play(self):
        if self.cur_song is None:
            return
        self.media_player.play()
        self.timer.start()
        self.is_playing = True

    def toggle_pause_play(self):
        if self.cur_song is None:
            return
        if self.is_playing:
            self.pause()
        else:
            self.play()

    PREVIOUS_THRESHOLD = 5000
    def previous_clicked(self):
        # before this threshold, go to previous track
        # otherwise, seek to beginning
    
        if self.media_player.position() <= self.PREVIOUS_THRESHOLD:
            if self.cur_playlist and self.cur_playlist_index != 0:
                self.cur_playlist_index -= 1
                self.play_song(self.songs[self.cur_playlist.get_song_at_index(self.cur_playlist_index)])
        else:
            self.media_player.setPosition(0)

    def next_clicked(self):
        if self.cur_playlist and self.cur_playlist_index != len(self.cur_playlist.get_songs())-1:
            self.cur_playlist_index += 1
            self.play_song(self.songs[self.cur_playlist.get_song_at_index(self.cur_playlist_index)])

    def set_volume(self, slider_position):
        self.volume_slider.setSliderPosition(slider_position)
        self.player_page_volume_slider.setSliderPosition(slider_position)
        
        self.audio_output.setVolume(slider_position/100)
        
        self.settings.beginGroup("player")
        self.settings.setValue("volume", slider_position)
        self.settings.endGroup()

    def volume_up(self):
        new_volume = min(self.volume_slider.sliderPosition() + 5, 100)
        self.set_volume(new_volume)

    def volume_down(self):
        new_volume = max(self.volume_slider.sliderPosition() - 5, 0)
        self.set_volume(new_volume)
        
    def set_player_position(self, position):
        if self.cur_song is None:
            return
        
        duration = self.cur_song.get_duration()
        
        player_position = duration * (position / 100)

        self.media_player.setPosition(int(player_position))

    def slider_pressed(self):
        if self.is_playing:
            self.was_playing = True
            self.pause()
        else:
            self.was_playing = False
        
        self.is_slider_pressed = True
    
    def slider_released(self):
        if self.was_playing:
            self.play()
        
        self.is_slider_pressed = False
        
    def slider_value_changed(self, position):
        if self.is_slider_pressed:
            self.set_player_position(position)

    def toggle_shuffle(self):
        self.is_shuffle_on = not self.is_shuffle_on
        print("Shuffle:", self.is_shuffle_on)

        self.settings.beginGroup("player")
        self.settings.setValue("shuffle", self.is_shuffle_on)
        self.settings.endGroup()

    def toggle_loop(self):
        self.is_loop_on = not self.is_loop_on
        print("Loop:", self.is_loop_on)

        self.settings.beginGroup("player")
        self.settings.setValue("loop", self.is_loop_on)
        self.settings.endGroup()
        
    def update_duration_text(self, duration: int):
        cur_milliseconds = self.media_player.position()
        cur_seconds = cur_milliseconds // 1000
        remaining_seconds = duration // 1000 - cur_seconds
        
        start_dur = seconds_to_time(cur_seconds)
        end_dur = "-" + seconds_to_time(remaining_seconds)
        
        self.player_startdur_label.setText(start_dur)
        self.player_enddur_label.setText(end_dur)
        
        self.player_page_startdur_label.setText(start_dur)
        self.player_page_enddur_label.setText(end_dur)

    def update_player(self):        
        # set text for duration
        duration = self.cur_song.get_duration()
        
        self.update_duration_text(duration)
                
        # update slider
        
        # slider goes from 0 to 100
        player_position = (self.media_player.position() / duration) * 100
        self.player_slider.setSliderPosition(int(player_position))
        self.player_page_slider.setSliderPosition(int(player_position))
        
        # update player ui
        self.sidebar_player_play_pause_button.setChecked(self.media_player.isPlaying())
        self.player_page_play_pause_button.setChecked(self.media_player.isPlaying())
        
        self.sidebar_player_shuffle_button.setChecked(self.is_shuffle_on)
        self.player_page_shuffle_button.setChecked(self.is_shuffle_on)
        
        self.sidebar_player_loop_button.setChecked(self.is_loop_on)
        self.player_page_loop_button.setChecked(self.is_loop_on)
        if not self.media_player.isPlaying():
            self.timer.stop()
            self.is_playing = False

    # ---------------
    # -- PLAYLISTS --
    # ---------------
    ADD_SONG_PLAYLIST_ENDPOINT = "add-playlist-song/"
    def setup_playlists(self):
        self.song_items: list[SongItem] = []
        self.opened_playlist: Playlist = None
        self.playlist_image_label = QLabel()
        self.playlist_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.playlist_image_widget.layout().addWidget(self.playlist_image_label)

    def open_playlist(self, playlist: Playlist):
        self.opened_playlist = playlist

        self.playlist_no_songs_label.show()

        self.playlist_name_label.setText(playlist.name)
        
        self.playlist_play_button.clicked.connect(lambda: self.play_playlist(self.opened_playlist))
        self.playlist_edit_button.show()
        self.playlist_edit_button.clicked.connect(self.edit_playlist)
        self.playlist_shuffle_button.clicked.connect(lambda: self.play_playlist_shuffle(self.opened_playlist))
        
        image = playlist.image
        if image:
            pixmap = QPixmap(image).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            # self.playlist_image_label.setScaledContents(True)
            self.playlist_image_label.setPixmap(pixmap)
        
        for song in playlist.get_songs():
            if song not in self.songs:
                self.load_song(song)
            self.add_playlist_item(self.songs[song])

    def open_playlist_page(self, playlist: Playlist):
        self.clear_playlist_page()

        self.open_playlist(playlist)

        self.open_page_with_back_button(self.playlist_page)
    
    def update_playlist_page(self):
        cur_playlist = self.opened_playlist
        
        self.clear_playlist_page()
        
        self.open_playlist(cur_playlist)

    def edit_playlist(self):
        style_sheet = "background-color: white; color: black; border: 1px solid black; padding: 5px; border-radius: 5px;"
        edit_playlist_popup = QWidget(self, Qt.Dialog)
        edit_playlist_popup.setWindowTitle('Edit Playlist Details')
        edit_playlist_popup.resize(200, 150)

        edit_playlist_contents = QVBoxLayout(edit_playlist_popup)
        edit_playlist_contents.addWidget(QLabel("Playlist Name:"))

        playlist_name = QLineEdit(self.opened_playlist.get_name())
        playlist_name.setStyleSheet(style_sheet)
        edit_playlist_contents.addWidget(playlist_name)
        
        edit_playlist_contents.addWidget(QLabel("Playlist Cover:"))

        image_layout = QHBoxLayout()

        self.image_label = QLabel("Choose Playlist Image")
        self.image_label.setStyleSheet(style_sheet)
        image_layout.addWidget(self.image_label)

        button_style_sheet = """
            QPushButton {
                background-color: #505050;
                padding: 5px;
                border-radius: 5px;
                color: #dddddd;
            }
            
            QPushButton:hover {
                background-color: #303030;
                color: #ffffff;
            }"""
        choose_image_button = QPushButton()
        choose_image_button.setFixedSize(20,20)
        choose_image_button.clicked.connect(self.choose_image)
        search_image_icon = QIcon()
        search_image_icon.addFile(":/resources/assets/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        choose_image_button.setIcon(search_image_icon)
        choose_image_button.setIconSize(QSize(20,20))
        choose_image_button.setStyleSheet("background-color: RGB(0,0,0,0); border: 0px; padding: 0px;")

        self.new_image_path = None
        image_layout.addWidget(choose_image_button)

        edit_playlist_contents.addLayout(image_layout)

        buttons_layout = QHBoxLayout()

        cancel_button = QPushButton("Cancel")
        buttons_layout.addWidget(cancel_button)
        cancel_button.setStyleSheet(button_style_sheet)
        cancel_button.clicked.connect(edit_playlist_popup.close)
        
        save_button = QPushButton("Save")
        buttons_layout.addWidget(save_button)
        save_button.clicked.connect(lambda: self.save_new_playlist_details(playlist_name.text(), self.new_image_path))
        save_button.setStyleSheet(button_style_sheet)
        save_button.clicked.connect(edit_playlist_popup.close)
        
        edit_playlist_contents.addLayout(buttons_layout)

        edit_playlist_popup.show()

    def choose_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        image_path, _ = file_dialog.getOpenFileName(self, "Choose Playlist Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        if image_path:
            image_name = image_path.split('/')[-1]
            self.image_label.setText(image_name)
            self.new_image_path = image_path

    PLAYLIST_EDIT_ENDPOINT = "edit-playlist/"
    DELETE_PLAYLIST_ENDPOINT = "delete-playlist/"
    def save_new_playlist_details(self, playlist_name: str, playlist_image_path: str):
        
        if playlist_image_path:
            playlist_image = QPixmap(playlist_image_path).scaled(200, 200)
            
            with open(playlist_image_path, "rb") as image_file:
                image_base64 = base64.urlsafe_b64encode(image_file.read()).decode()
                
            data = {
                "playlist_name": playlist_name,
                "playlist_image": image_base64,
                "image_filename": playlist_image_path.split("/")[-1]
            }
        else:
            data = {
                "playlist_name": playlist_name
            }
        
        reply = self.perform_post_request_sync(
            url=self.SERVER_URL + self.PLAYLIST_EDIT_ENDPOINT + self.opened_playlist.get_uuid(),
            data=data
        )
        reply_data = reply.readAll()
        reply_json = QJsonDocument.fromJson(reply_data).object()
        
        self.opened_playlist.set_name(playlist_name)
        self.playlist_name_label.setText(playlist_name)
        
        if playlist_image_path:
            self.opened_playlist.set_image(playlist_image)
            self.playlist_image_label.setPixmap(playlist_image)
        
        self.update_home_page()
        self.update_library_page()

    def clear_playlist_page(self):
        # for i in reversed(range(self.playlist_contents_scrollarea_contents.layout().count())): 
        #     self.playlist_contents_scrollarea_contents.layout().itemAt(i).widget().setParent(None)
        self.opened_playlist = None
        try:
            self.playlist_edit_button.clicked.disconnect()
        except RuntimeError:
            pass
        try:
            self.playlist_shuffle_button.clicked.disconnect()
        except RuntimeError:
            pass
        try:
            self.playlist_play_button.clicked.disconnect()
        except RuntimeError:
            pass
        
        for i in reversed(range(len(self.song_items))):
            self.playlist_contents.layout().removeWidget(self.song_items[i])
            self.song_items[i].deleteLater()
            self.song_items.remove(self.song_items[i])

    SONG_IMAGE_ENDPOINT = "get-song-image/"
    def add_playlist_item(self, song: Song, is_album=False):
        if len(self.song_items) == 0:
            self.playlist_no_songs_label.hide()
        
        item = SongItem(song, len(self.song_items), self.opened_playlist, is_album=is_album, parent=self)
        self.song_items.append(item)
        self.playlist_contents.layout().addWidget(item)

    # -----------
    # -- ALBUM --
    # -----------
    def open_album(self, album: Album):
        self.clear_playlist_page()
        
        temp_playlist = Playlist("temp", album.get_title(), album.get_artists()[0], album.get_songs(), album.get_image())
        
        self.opened_playlist = temp_playlist
        
        self.playlist_no_songs_label.show()

        self.playlist_name_label.setText(album.get_title())
        
        self.playlist_play_button.clicked.connect(lambda: self.play_playlist(self.opened_playlist, add_to_recent=False))
        self.playlist_edit_button.hide()
        self.playlist_shuffle_button.clicked.connect(lambda: self.play_playlist_shuffle(self.opened_playlist, add_to_recent=False))
        
        image = album.get_image()
        if image:
            pixmap = QPixmap(image).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            # self.playlist_image_label.setScaledContents(True)
            self.playlist_image_label.setPixmap(pixmap)
        
        for song in album.get_songs():
            if song not in self.songs:
                self.load_song(song)
            self.add_playlist_item(self.songs[song], is_album=True)
        
        self.open_page_with_back_button(self.playlist_page)

    # ------------------
    # -- GENERIC PAGE --
    # ------------------
    def setup_generic_page(self):
        self.generic_scrollarea_contents.setLayout(FlowLayout())
        
    def open_generic_page(self, title: str, items: list[QObject]):
        self.open_page_with_back_button(self.generic_page)
        self.generic_title.setText(title)
        
        self.clear_widget(self.generic_scrollarea_contents)
        
        for item in items:
            self.generic_scrollarea_contents.layout().addWidget(item)
    
# ----------------
# -- COMPONENTS --
# ----------------
class SmallThumbnailItem(QPushButton):
    def __init__(self, text: str, image: QPixmap, parent=None):
        super().__init__(parent)

        # self.setObjectName("recent_playlist")
        self.setMinimumSize(QSize(250, 64))
        self.setText("  " + text)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)

        icon = QIcon()
        if image:
            icon.addPixmap(image, QIcon.Normal, QIcon.Off)
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
    def __init__(self, heading="No Title", subheading="", image=None, parent=None):
        super().__init__(parent)

        self.setMinimumSize(QSize(140, 180))
        self.setMaximumSize(QSize(140, 180))
        self.setFixedSize(QSize(140, 180))
        self.setCursor(Qt.PointingHandCursor)
        self.setAutoFillBackground(False)
        
        self.icon_label = QLabel(self)
        self.icon_label.setFixedSize(120, 120)
        self.icon_label.setAlignment(Qt.AlignCenter)
        if image:
            pixmap = QPixmap(image).scaled(120, 120)
            self.icon_label.setPixmap(pixmap)

        heading_label = QLabel(self)
        heading_label.setText(heading)
        heading_label.setAlignment(Qt.AlignLeft)
        heading_label.setStyleSheet("color: #ffffff; font-size: 14px; background-color: transparent;")

        subheading_label = QLabel(self)
        subheading_label.setText(subheading)
        subheading_label.setAlignment(Qt.AlignLeft)
        subheading_label.setStyleSheet("color: #cccccc; font-size: 12px; background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.icon_label)
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

class LongLabelButton(QWidget):
    def __init__(self, text: str, parent: MainWindow = None) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.setMinimumHeight(40)

        self.main_window = parent

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

class SmallPlaylistItem(SmallThumbnailItem):
    def __init__(self, playlist: Playlist, parent: MainWindow):
        super().__init__(playlist.name, playlist.image, parent)
        
        self.playlist = playlist
        self.main_window = parent
                
        self.clicked.connect(self.show_playlist)

    def show_playlist(self):
        self.main_window.open_playlist_page(self.playlist)

class BigPlaylistItem(BigThumbnailItem):
    def __init__(self, playlist: Playlist, parent: MainWindow):
        super().__init__(playlist.name, playlist.author, playlist.image, parent)
        
        self.playlist = playlist
        self.main_window = parent
        
        self.clicked.connect(self.show_playlist)

    def show_playlist(self):
        self.main_window.open_playlist_page(self.playlist)

class AlbumItem(BigThumbnailItem):
    def __init__(self, album: Album, parent: MainWindow):
        super().__init__(album.get_title(), album.get_artists()[0], album.get_image(), parent)

        self.main_window = parent
        self.album = album

        self.menu_button = QToolButton(self)
        # self.menu_button.setText("...")
        menu_icon = QIcon()
        menu_icon.addFile(":/resources/assets/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(menu_icon)
        self.menu_button.setIconSize(QSize(16, 16))
        
        self.menu_button.clicked.connect(self.show_menu)
        self.menu_button.setStyleSheet("background-color: rgba(0,0,0,0)")
        
        geometry = self.geometry()
        self.menu_button.setGeometry(geometry.right()-24, geometry.bottom()-24, 16, 16)
    
        self.clicked.connect(self.on_click)
    
    def on_click(self):
        # TODO: open the album and play starting
        print("test")
        self.main_window.open_album(self.album)

    def show_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("background-color: #1e1e1e")

        # TODO: add to library?
        menu.setStyleSheet("background-color: #1e1e1e")
        add_to_playlist_action = QAction("Add to Library", self)
        add_to_playlist_action.triggered.connect(self.add_to_library)
        menu.addAction(add_to_playlist_action)
        
        menu.exec_(self.menu_button.mapToGlobal(self.menu_button.rect().bottomRight()))

    def add_to_library(self):
        pass

class BigSongItem(BigThumbnailItem):
    def __init__(self, song: Song, parent: MainWindow):
        super().__init__(song.title, song.artists[0], song.image, parent)

        self.main_window = parent
        self.song = song
        
        song.add_observer(self)

        self.menu_button = QToolButton(self)
        # self.menu_button.setText("...")
        menu_icon = QIcon()
        menu_icon.addFile(":/resources/assets/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(menu_icon)
        self.menu_button.setIconSize(QSize(16, 16))
        
        self.menu_button.clicked.connect(self.show_menu)
        self.menu_button.setStyleSheet("background-color: rgba(0,0,0,0)")
        
        geometry = self.geometry()
        self.menu_button.setGeometry(geometry.right()-24, geometry.bottom()-24, 16, 16)
    
        self.clicked.connect(self.play_song)

    def update_image(self):
        pixmap = QPixmap(self.song.get_image()).scaled(120, 120)
        self.icon_label.setPixmap(pixmap)
        
    def play_song(self):
        self.main_window.play_song(self.song)

    def show_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("background-color: #1e1e1e")
        add_to_playlist_action = QAction("Add to Playlist", self)
        add_to_playlist_action.triggered.connect(self.show_playlists_menu)
        menu.addAction(add_to_playlist_action)

        # go_to_artist_action = QAction("Go to Artist", self)
        # go_to_artist_action.triggered.connect(self.show_artist_page)
        # menu.addAction(go_to_artist_action)

        # go_to_album_action = QAction("Go to Album", self)
        # go_to_album_action.triggered.connect(self.show_album_page)
        # menu.addAction(go_to_album_action)
        menu.exec_(self.menu_button.mapToGlobal(self.menu_button.rect().bottomRight()))

    def show_playlists_menu(self):
        playlists = self.main_window.user.playlists
        menu = QMenu(self)
        menu.setStyleSheet("background-color: #1e1e1e")
        if playlists:
            for playlist in playlists:
                playlist_obj = self.main_window.playlists[playlist]
                action = QAction(playlist_obj.get_name(), self)
                action.setData(playlist_obj.get_uuid())
                action.triggered.connect(self.add_to_playlist)
                menu.addAction(action)
        else:
            action = QAction("No playlists", self)
            action.setEnabled(False)
            menu.addAction(action)
        menu.exec_(self.menu_button.mapToGlobal(self.menu_button.rect().bottomRight()))

    def add_to_playlist(self):
        
        action: QAction = self.sender()
        
        playlist = self.main_window.playlists[action.data()]

        self.main_window.perform_post_request_sync(
            self.main_window.SERVER_URL + self.main_window.ADD_SONG_PLAYLIST_ENDPOINT + playlist.get_uuid() + "/" + self.song.get_uuid())
        
        playlist.add_song(self.song.get_uuid())
        
class CategoryItem(QPushButton):
    def __init__(self, category: Category, parent: MainWindow):
        super().__init__(parent)
        
        self.main_window = parent
        self.category = category
        
        self.clicked.connect(self.open_category)
        
        self.setFixedSize(QSize(140, 180))
        self.setCursor(Qt.PointingHandCursor)
        self.setAutoFillBackground(False)

        icon_label = QLabel(self)
        icon_label.setFixedSize(120, 120)
        icon_label.setAlignment(Qt.AlignCenter)

        if category.image:
            scaled_pixmap = category.image.scaled(120, 120)
            icon_label.setPixmap(scaled_pixmap)

        heading_label = QLabel(self)
        heading_label.setText(category.name)
        heading_label.setAlignment(Qt.AlignLeft)
        heading_label.setStyleSheet(f"color: red; font-size: 14px; background-color: transparent;")
        heading_label.setStyleSheet(f"color: {category.color}; font-size: 14px; background-color: transparent;")

        # subheading_label = QLabel(self)
        # subheading_label.setAlignment(Qt.AlignLeft)
        # subheading_label.setStyleSheet("color: #cccccc; font-size: 12px; background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.addWidget(icon_label)
        layout.addWidget(heading_label)
        self.setLayout(layout)
        
        self.setProperty("class", "CategoryItem")
        self.setStyleSheet("""
            .CategoryItem {
                background-color: #1e1e1e;
                font-size: 14px;
                padding: 0px;
                text-align: center;
                border-radius: 5px;
            }
            .CategoryItem:hover {
                color: #ffffff;
                background-color: #303030;
            }
        """)
        
    def open_category(self):
        items = []
        for song in self.category.get_songs():
            items.append(BigSongItem(
                self.main_window.songs[song],
                self.main_window
            ))
        
        self.main_window.open_generic_page(
            title=self.category.name,
            items=items
        )

# -- browse page --
class RecentSearchItem(LongLabelButton):
    def __init__(self, text: str, parent: MainWindow = None) -> None:
        super().__init__(text, parent)
        
        self.label.clicked.connect(lambda: parent.perform_search_query(text))
        
        self.tool_button.setIcon(QIcon(":/resources/assets/images/cancel.png"))
        self.tool_button.clicked.connect(lambda: parent.remove_recent_search(self))

# -- library page --
class LibraryItem(QWidget):
    def __init__(self, playlist: Playlist, parent: MainWindow) -> None:
        super().__init__(parent)
        
        self.main_window = parent
        self.playlist = playlist
        
        layout = QHBoxLayout()
        layout.addWidget(SmallPlaylistItem(playlist, parent))
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.delete_button = QToolButton(self)
        self.delete_button.setIcon(QIcon(":/resources/assets/images/delete.png"))
        self.delete_button.setIconSize(QSize(40, 40))
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.clicked.connect(self.show_delete_playlist_popup)
        layout.addWidget(self.delete_button)
        
        self.setLayout(layout)
        
    def show_delete_playlist_popup(self):
        delete_playlist_popup = QMessageBox(self.main_window)
        delete_playlist_popup.setWindowTitle("Delete Playlist")
        
        delete_playlist_popup.setIcon(QMessageBox.Icon.Warning)

        delete_playlist_popup.setText(f"Delete <{self.playlist.get_name()}> from your library?")

        delete_playlist_popup.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        
        ret = delete_playlist_popup.exec()
        if ret == QMessageBox.StandardButton.Ok:
            self.delete_playlist()

        # buttons_layout = QHBoxLayout()
        # cancel_button = QPushButton("Cancel")

        # cancel_button.clicked.connect(delete_playlist_popup.close)
        # buttons_layout.addWidget(cancel_button)

        # confirm_delete_button = QPushButton("Delete")
        # confirm_delete_button.clicked.connect(self.delete_playlist)
        # confirm_delete_button.clicked.connect(delete_playlist_popup.close)
        # buttons_layout.addWidget(confirm_delete_button)

        # layout.addLayout(buttons_layout)
        # delete_playlist_popup.setLayout(layout)

        # delete_playlist_popup.show()

    def delete_playlist(self):
        self.main_window.perform_post_request_sync(self.main_window.SERVER_URL + self.main_window.DELETE_PLAYLIST_ENDPOINT + self.playlist.get_uuid())
        self.playlist.remove_song(self.song.get_uuid())
        self.main_window.update_library_page()

# -- profile page --
class ProfileItem(LongLabelButton):
    def __init__(self, text: str, on_click: FunctionType, parent: MainWindow = None) -> None:
        super().__init__(text, parent)
        
        self.tool_button.setIcon(QIcon(":/resources/assets/images/enter.png"))
        
        self.label.clicked.connect(on_click)
        self.tool_button.clicked.connect(on_click)

# -- playlists page --
class SongItem(QWidget):
    def __init__(self, song: Song, index: int, playlist: Playlist, is_album: bool=False, parent: MainWindow=None) -> None:
        super().__init__(parent)
        
        self.main_window = parent
        
        self.song = song
        self.playlist = playlist
        
        icon_label = QLabel(self)
        icon_label.setFixedSize(60, 60)
        icon_label.setAlignment(Qt.AlignCenter)
        if song.image:
            pixmap = QPixmap(song.image).scaled(60, 60)
            icon_label.setPixmap(pixmap)
        
        labels_widget = QWidget(self)
        labels_widget.setLayout(QVBoxLayout())

        heading_label = QLabel(self)
        heading_label.setText(song.title)
        heading_label.setAlignment(Qt.AlignLeft)
        heading_label.setStyleSheet("color: #ffffff; font-size: 14px; background-color: transparent;")

        subheading_label = QLabel(self)
        subheading_label.setText(song.artists[0])
        subheading_label.setAlignment(Qt.AlignLeft)
        subheading_label.setStyleSheet("color: #cccccc; font-size: 12px; background-color: transparent;")
        
        labels_widget.layout().addWidget(heading_label)
        labels_widget.layout().addWidget(subheading_label)
        
        duration_label = QLabel(self)
        duration_label.setText(ms_to_time(song.get_duration()))
        
        play_button = QToolButton(self)
        play_button.setIcon(QIcon(":/resources/assets/images/play.png"))
        play_button.setCursor(QCursor(Qt.PointingHandCursor))

        play_button.clicked.connect(lambda: self.main_window.play_playlist(playlist, index, add_to_recent=(not is_album)))

        layout = QHBoxLayout(self)
        layout.addWidget(icon_label)
        layout.addWidget(labels_widget)
        layout.addWidget(duration_label)
        layout.addWidget(play_button)

        if not is_album:
            self.song_menu_button = QToolButton(self)
            self.song_menu_button.setIcon(QIcon(":/resources/assets/images/menu.png"))
            self.song_menu_button.setCursor(QCursor(Qt.PointingHandCursor))
            self.song_menu_button.clicked.connect(self.show_song_menu)
            layout.addWidget(self.song_menu_button)
    
        self.setLayout(layout)
        
        self.setProperty("class", "PlaylistItem")
        self.setStyleSheet("""
            .PlaylistItem {
                background-color: #1e1e1e;
                font-size: 14px;
                padding: 0px;
                text-align: center;
                border-radius: 5px;
            }
        """)

    def show_song_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("background-color: #1e1e1e")
        
        delete_from_playlist_action = QAction("Delete from this playlist", self)
        delete_from_playlist_action.triggered.connect(self.delete_song_confirm)
        menu.addAction(delete_from_playlist_action)
            
        move_song_up_action = QAction("Move Up", self)
        move_song_up_action.triggered.connect(self.move_song_up)
        menu.addAction(move_song_up_action)

        move_song_down_action = QAction("Move Down", self)
        move_song_down_action.triggered.connect(self.move_song_down)
        menu.addAction(move_song_down_action)
        
        menu.exec_(self.song_menu_button.mapToGlobal(self.song_menu_button.rect().bottomRight()))

    MOVE_PLAYLIST_SONG_ENDPOINT = "move-playlist-song/"
    def move_song_up(self):
        self.playlist.move_song_up(self.song.get_uuid())
        self.main_window.update_playlist_page()
        self.main_window.perform_post_request_sync(
            url=self.main_window.SERVER_URL + self.MOVE_PLAYLIST_SONG_ENDPOINT + self.playlist.get_uuid() + "/" + self.song.get_uuid(),
            data={"direction": "up"}
        )

    def move_song_down(self):
        self.playlist.move_song_down(self.song.get_uuid())
        self.main_window.update_playlist_page()
        self.main_window.perform_post_request_sync(
            url=self.main_window.SERVER_URL + self.MOVE_PLAYLIST_SONG_ENDPOINT + self.playlist.get_uuid() + "/" + self.song.get_uuid(),
            data={"direction": "down"}
        )

    def delete_song_confirm(self):
        delete_song_popup = QMessageBox(self.main_window)
        delete_song_popup.setWindowTitle("Delete Song")
        
        delete_song_popup.setIcon(QMessageBox.Icon.Warning)

        delete_song_popup.setText(f"Delete <{self.song.title}> from <{self.playlist.get_name()}>?")

        delete_song_popup.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
        
        ret = delete_song_popup.exec()
        if ret == QMessageBox.StandardButton.Ok:
            self.delete_song_from_playlist()
        
    def delete_song_from_playlist(self):
        self.main_window.perform_post_request_sync(
            self.main_window.SERVER_URL + self.main_window.DELETE_PLAYLIST_ENDPOINT + self.playlist.get_uuid() + "/" + self.song.get_uuid()
        )
        self.playlist.remove_song(self.song.get_uuid())
        self.main_window.update_playlist_page()

# -- utility --
def ms_to_time(duration_ms: float):
    total_seconds = duration_ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:01}:{seconds:02}"

def seconds_to_time(duration_s: float):
    return ms_to_time(duration_s*1000)
