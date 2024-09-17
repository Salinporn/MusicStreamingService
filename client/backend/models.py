from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap

class User:
    def __init__(self, uuid, name, email, playlists, recently_played):
        self.uuid: str = uuid
        self.name: str = name
        self.email: str = email
        self.playlists: list[str] = playlists
        self.recently_played: list[str] = recently_played
    
    def get_uuid(self) -> str:
        return self.uuid
    
    def get_name(self) -> str:
        return self.name
        
    def get_email(self) -> str:
        return self.email
    
    def get_playlists(self) -> list[str]:
        return self.playlists
    
    def get_recently_played(self) -> list[str]:
        return self.recently_played

class Playlist:
    def __init__(self, uuid, name, author, songs=None, image=None) -> None:
        self.uuid: str = uuid
        self.name: str = name
        self.author: str = author
        self.image: QPixmap = image
        self.songs: list[str] = [song for song in songs if song] if songs else []
    
    def get_uuid(self):
        return self.uuid
    
    def get_name(self):
        return self.name
    
    def get_songs(self):
        return self.songs
    
    def set_name(self, name):
        self.name = name
    
    def set_image(self, image):
        self.image = image
    
    def get_song_at_index(self, index):
        if 0 <= index < len(self.songs):
            return self.songs[index]
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        self.songs.remove(song)

    def move_song_up(self, song_id):
        index = self.songs.index(song_id)
        if index != 0:
            self.songs[index], self.songs[index-1] = self.songs[index-1], self.songs[index]

    def move_song_down(self, song_id):
        index = self.songs.index(song_id)
        if index != len(self.songs)-1:
            self.songs[index], self.songs[index+1] = self.songs[index+1], self.songs[index]

class Song:
    def __init__(self, uuid, title, artists, album, duration, image = None):
        self.uuid: str = uuid
        self.title: str = title
        self.artists: list[str] = artists
        self.album: str = album
        self.duration: float = duration
        self.image: QPixmap = image
        
        self.observers: list[QWidget] = []

    def get_uuid(self) -> str:
        return self.uuid

    def get_duration(self) -> int:
        return self.duration
    
    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image
        
        for observer in self.observers:
            observer.update_image()
    
    def add_observer(self, observer):
        self.observers.append(observer)

class Album:
    def __init__(self, uuid, title, artists, songs, image=None):
        self.uuid: str = uuid
        self.title: str = title
        self.artists: list[str] = artists
        self.songs: list[str] = songs
        self.image: QPixmap = image

    def get_uuid(self) -> str:
        return self.uuid

    def get_title(self) -> str:
        return self.title

    def get_artists(self) -> list[str]:
        return self.artists

    def get_songs(self) -> list[str]:
        return self.songs
    
    def get_image(self) -> QPixmap:
        return self.image

    def set_image(self, image):
        self.image = image

class Category:
    def __init__(self, uuid, name, color, songs, image):
        self.uuid: str = uuid
        self.name: str = name
        self.color: str = color
        self.songs: list[str] = songs
        self.image: QByteArray = image
        
    def get_songs(self):
        return self.songs