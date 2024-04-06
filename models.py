import persistent
from persistent.list import PersistentList
import abc
import uuid

class User(persistent.Persistent):
    def __init__(self, uuid, email, name, password_hash, is_admin=False):
        self.uuid: str = uuid
        self.email: str = email
        self.name: str = name
        self.password_hash: str = password_hash
        self.is_admin: bool = is_admin
        
        self.playlists: list[Playlist] = PersistentList()
        self.recently_played: list[Playlist] = PersistentList()
    
    def get_uuid(self):
        return self.uuid
    
    def get_email(self):
        return self.email
    
    def get_password_hash(self):
        return self.password_hash
    
    def get_playlists(self):
        return self.playlists
    
    def get_recently_played(self):
        return self.recently_played
        
    def get_json(self):
        for playlist in self.recently_played:
            if type(playlist) == str:
                self.recently_played.remove(playlist)
            if playlist == None:
                self.recently_played.remove(playlist)
        
        return {
            "uuid": self.uuid,
            "email": self.email,
            "name": self.name,
            "playlists": [playlist.get_json() for playlist in self.playlists],
            "recently_played": [playlist.get_json() for playlist in self.recently_played ]
        }
    
    def edit(self, new_uuid, new_email, new_name, new_password_hash, new_is_admin):
        self.uuid = new_uuid
        self.email = new_email
        self.name = new_name
        self.password_hash = new_password_hash
        self.is_admin = new_is_admin

    def add_playlist(self, playlist: "Playlist"):
        self.playlists.append(playlist)

    def delete_playlist(self, playlist: "Playlist"):
        self.playlists.remove(playlist)

    def add_recently_played(self, playlist: "Playlist"):
        if playlist in self.recently_played:
            self.recently_played.remove(playlist)
        self.recently_played.insert(0, playlist)
        if len(self.recently_played) > 6:
            self.recently_played.pop()

class Song(persistent.Persistent):
    def __init__(self, uuid, title, genres, artists):
        self.uuid: str = uuid
        self.title: str = title
        self.genres: list[Genre] = PersistentList(genres)
        self.artists: list[Artist] = PersistentList(artists)
        self.album: Album = None
        self.listens: int = 0
        self.file_name: str = None
        self.duration_ms: int = -1
    
    def get_uuid(self):
        return self.uuid
    
    def get_title(self):
        return self.title
    
    def get_genres(self):
        return self.genres
    
    def get_artists(self):
        return self.artists
    
    def get_album(self) -> "Album":
        return self.album
    
    def get_listens(self):
        return self.listens
    
    def get_file_name(self):
        return self.file_name
    
    def get_json(self):
        for genre in self.genres:
            if type(genre) == str:
                self.genres.remove(genre)
        for artist in self.artists:
            if type(artist) == str:
                self.artists.remove(artist)

        return {
            "uuid": self.uuid,
            "title": self.title,
            "genres": [genre.name for genre in self.genres],
            "artists": [artist.name for artist in self.artists],
            "album": None if self.album is None else self.album.get_uuid(),
            "album_title": None if self.album is None else self.album.get_title(),
            "duration": self.duration_ms
        }

    def set_album(self, album: "Album"):
        self.album = album
    
    def set_file_name(self, file_name):
        self.file_name = file_name
        
    def set_duration(self, duration):
        self.duration_ms = int(duration)

    def edit(self, title, genres, artists):        
        self.title = title
        for g in self.genres:
            g.delete_song(self)
        for a in self.artists:
            a.delete_song(self)
        
        for g in genres:
            g.add_song(self)
        for a in artists:
            a.add_song(self)
        
        self.genres = genres
        self.artists = artists
    
    def delete_artist(self, artist: "Artist"):
        self.artists.remove(artist)
    
    def delete_album(self):
        self.album = None
    
    def delete_genre(self, genre: "Genre"):
        if genre in self.genres:
            self.genres.remove(genre)
        
class Artist(persistent.Persistent):
    def __init__(self, uuid, name):
        self.uuid: str = uuid
        self.name: str = name
        self.songs: list[Song] = PersistentList()
        self.albums: list[Album] = PersistentList()
    
    def get_uuid(self):
        return self.uuid
    
    def get_name(self):
        return self.name    

    def get_songs(self):
        return self.songs
    
    def get_albums(self):
        return self.albums
    
    def edit(self, name):
        self.name = name

    def delete_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)

    def delete_album(self, album: "Album"):
        self.albums.remove(album)

    def add_song(self, song: Song):
        self.songs.append(song)
    
    def add_album(self, album: "Album"):
        self.albums.append(album)
        
class Album(persistent.Persistent):
    def __init__(self, uuid, title, artists, songs):
        self.uuid: str = uuid
        self.title: str = title
        self.artists: list[Artist] = PersistentList(artists)
        self.songs: list[Song] = PersistentList(songs)
        self.file_name: str = None

    def get_uuid(self):
        return self.uuid
    
    def get_title(self):
        return self.title
    
    def get_artists(self):
        return self.artists
        
    def get_songs(self):
        return self.songs
    
    def get_file_name(self):
        return self.file_name
    
    def get_json(self):
        return {
            "uuid": self.uuid,
            "title": self.title,
            "artists": [artist.get_name() for artist in self.artists],
            "songs": [song.get_uuid() for song in self.songs],
        }
    
    def set_file_name(self, file_name):
        self.file_name = file_name
        
    def edit(self, title, artists, songs):
        self.title = title
        self.artists = artists
        self.songs = songs
        
    def delete_artist(self, artist: Artist):
        self.artists.remove(artist)
    
    def delete_song(self, song: Song):
        self.songs.remove(song)
    
    def add_song(self, song: Song):
        self.songs.append(song)
        
class Library(persistent.Persistent):
    def __init__(self):
        pass

class Playlist(persistent.Persistent):
    def __init__(self, uuid, name, author):
        self.uuid: str = uuid
        self.name: str = name
        self.author: User = author
        self.songs: list[Song] = PersistentList()
        self.file_name: str = None
    
    def get_uuid(self) -> str:
        return self.uuid

    def get_file_name(self) -> str:
        try:
            return self.file_name
        except AttributeError:
            self.file_name = None
        
    def get_songs(self):
        return self.songs
        
    def get_json(self) -> dict:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "songs": [ song.get_uuid() for song in self.songs ]
        }
        
    def set_name(self, name):
        self.name = name
    
    def set_file_name(self, file_name):
        self.file_name = file_name
        
    def add_song(self, song: Song):
        self.songs.append(song)

    def delete_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)

    def move_song_up(self, song: Song):
        index = self.songs.index(song)
        if index > 0:
            self.songs[index], self.songs[index - 1] = self.songs[index - 1], self.songs[index]

    def move_song_down(self, song: Song):
        index = self.songs.index(song)
        if index < len(self.songs) - 1:
            self.songs[index], self.songs[index + 1] = self.songs[index + 1], self.songs[index]
        
class Genre(persistent.Persistent):
    def __init__(self, uuid, name, color):
        self.uuid: str = uuid 
        self.name: str = name
        self.color: str = color
        self.songs: list[Song] = PersistentList()
        self.file_name: str = None
        
    def get_uuid(self):
        return self.uuid
    
    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def set_file_name(self, file_name):
        self.file_name = file_name
        
    def edit(self, name, color):
        self.name = name
        self.color = color
        
    def add_song(self, song: Song):
        self.songs.append(song)
        
    def delete_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)

    def get_json(self) -> dict:        
        return {
            "uuid": self.uuid,
            "name": self.name,
            "color": self.color,
            "songs": [ song.uuid for song in self.songs ]
        }