from PySide6.QtCore import QByteArray

class User:
    def __init__(self, uuid, name, email, playlists):
        self.uuid: str = uuid
        self.name: str = name
        self.email: str = email
        self.playlists: list[str] = playlists
    
    def get_name(self) -> str:
        return self.name

class Playlist:
    def __init__(self, name, author, image_path="") -> None:
        self.name = name
        self.author = author
        if image_path == "":
            image_path = ":resources/assets/images/playlist_placeholder.jpg"
        self.image_path = image_path
        self.songs = []

class Song:
    def __init__(self, uuid: str, title: str, artist: str, duration: float):
        self.uuid = uuid
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_uuid(self) -> str:
        return self.uuid

    def get_duration(self) -> int:
        return self.duration

class Category:
    def __init__(self, uuid: str, name: str, color:str, songs: list[str], image: QByteArray):
        self.uuid = uuid
        self.name = name
        self.color = color
        self.songs = songs
        self.image = image
        