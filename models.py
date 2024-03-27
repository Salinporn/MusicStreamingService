import persistent
import abc

class User(persistent.Persistent):
    def __init__(self, uuid, email, name, password_hash, is_admin=False):
        self.uuid = uuid
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.is_admin = is_admin
        
        self.playlists
        self.favorites
    
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
    def __init__(self):
        self.song_id
        self.title
        self.artists
        self.album
        self.listens

class Album(persistent.Persistent):
    def __init__(self):
        self.album_id
        self.title
        self.artists
        self.songs

class Artist(persistent.Persistent):
    def __init__(self):
        self.artist_id
        self.songs
        self.albums

class Library(persistent.Persistent):
    def __init__(self):
        pass

class Playlist(persistent.Persistent):
    def __init__(self):
        self.title
        self.songs
        
