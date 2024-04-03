from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap

class User:
    def __init__(self, uuid, name, email, playlists, recently_played):
        self.uuid: str = uuid
        self.name: str = name
        self.email: str = email
        self.playlists: list[Playlist] = playlists
        self.recently_played: list[Playlist] = recently_played
    
    def get_uuid(self) -> str:
        return self.uuid
    
    def get_name(self) -> str:
        return self.name
        
    def get_email(self) -> str:
        return self.email
    
    def get_playlists(self) -> list["Playlist"]:
        return self.playlists
    
    def get_recently_played(self) -> list["Playlist"]:
        return self.recently_played

class Playlist:
    def __init__(self, uuid, name, author, songs, image=None) -> None:
        self.uuid = uuid
        self.name = name
        self.author = author
        self.image = image
        self.songs = songs
    
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

class Song:
    def __init__(self, uuid: str, title: str, artists: list[str], duration: float, image: QPixmap = None):
        self.uuid = uuid
        self.title = title
        self.artists = artists
        self.duration = duration
        self.image = image

    def get_uuid(self) -> str:
        return self.uuid

    def get_duration(self) -> int:
        return self.duration
    
    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image
    
class Category:
    def __init__(self, uuid: str, name: str, color:str, songs: list[str], image: QByteArray):
        self.uuid = uuid
        self.name = name
        self.color = color
        self.songs = songs
        self.image = image
        
    def get_songs(self):
        return self.songs