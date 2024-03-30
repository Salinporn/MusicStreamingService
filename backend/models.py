
class Playlist:
    def __init__(self, name, artist, image_path) -> None:
        self.name = name
        self.songs = []
        self.artist = artist
        self.image_path = image_path

class Song:
    def __init__(self, title: str, artist: str, playlist: Playlist, duration: float):
        self.title = title
        self.artist = artist
        self.playlist = playlist
        self.duration = duration

class Category:
    def __init__(self, name: str, color: str, image_path: str):
        self.name = name
        self.color = color
        self.image_path = image_path
        