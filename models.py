import persistent
from persistent.list import PersistentList
import abc

class User(persistent.Persistent):
    def __init__(self, uuid, email, name, password_hash, is_admin=False):
        self.uuid: str = uuid
        self.email: str = email
        self.name: str = name
        self.password_hash: str = password_hash
        self.is_admin: bool = is_admin
        
        self.playlists = PersistentList()
        self.recently_played = PersistentList()
    
    def get_uuid(self):
        return self.uuid
    
    def get_email(self):
        return self.email
    
    def get_password_hash(self):
        return self.password_hash
    
    def edit(self, new_uuid, new_email, new_name, new_password_hash, new_is_admin):
        self.uuid = new_uuid
        self.email = new_email
        self.name = new_name
        self.password_hash = new_password_hash
        self.is_admin = new_is_admin

# maybe
# class Release(abc.ABC):
#     def __init__(self):
#         pass

class Song(persistent.Persistent):
    def __init__(self, uuid, title, genres, artists):
        self.uuid: str = uuid
        self.title: str = title
        self.genres: PersistentList[Genre] = PersistentList(genres)
        self.artists: PersistentList[Artist] = PersistentList(artists)
        self.album: PersistentList[Album] = None
        self.listens: int = 0
    
    def get_uuid(self):
        return self.uuid
    
    def get_title(self):
        return self.title
    
    def get_genres(self):
        return self.genres
    
    def get_artists(self):
        return self.artists
    
    def get_album(self):
        return self.album
    
    def get_listens(self):
        return self.listens

    def set_album(self, album: "Album"):
        self.album = album

    def edit(self, title, genres, artists):
        self.title = title
        self.genres = genres
        self.artists = artists
    
    def delete_artist(self, artist: "Artist"):
        self.artists.remove(artist)
        
class Artist(persistent.Persistent):
    def __init__(self, uuid, name):
        self.uuid: str = uuid
        self.name: str = name
        self.songs: PersistentList[Song] = PersistentList()
        self.albums: PersistentList[Album] = PersistentList()
    
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
        self.songs.remove(song)

    def add_song(self, song: Song):
        self.songs.append(song)
    
    def add_album(self, album: "Album"):
        self.albums.append(album)
        
class Album(persistent.Persistent):
    def __init__(self, uuid, title, artists, songs):
        self.uuid: str = uuid
        self.title: str = title
        self.artists: PersistentList[Artist] = PersistentList(artists)
        self.songs: PersistentList[Song] = PersistentList(songs)

    def get_uuid(self):
        return self.uuid
    
    def get_title(self):
        return self.title
    
    def get_artists(self):
        return self.artists
        
    def get_songs(self):
        return self.songs

    def edit(self, title, artists, songs):
        self.title = title
        self.artists = artists
        self.songs = songs
        
    def delete_artist(self, artist: Artist):
        self.artists.remove(artist)
    
    def add_song(self, song: Song):
        self.songs.append(song)
        
class Library(persistent.Persistent):
    def __init__(self):
        pass

class Playlist(persistent.Persistent):
    def __init__(self):
        self.title
        self.songs
        
class Genre(persistent.Persistent):
    def __init__(self, uuid, name):
        self.uuid: str = uuid 
        self.name: str = name
        self.songs: PersistentList[Song] = PersistentList()

    def get_uuid(self):
        return self.uuid
    
    def get_name(self):
        return self.name

    def edit(self, name):
        self.name = name
        
    def add_song(self, song: Song):
        self.songs.append(song)