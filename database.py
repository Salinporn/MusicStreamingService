import ZODB, ZODB.FileStorage, ZODB.config
import zc.lockfile
from BTrees._OOBTree import BTree
import os
import transaction
from models import *
import uuid
from werkzeug.security import generate_password_hash
import datetime

# middleman for communicating with the database
class Manager:
    def __init__(self, root):
        self.root = root
    
    def commit(self):
        transaction.commit()

class UserManager(Manager):
    DEFAULT_ADMIN_EMAIL = "admin@admin.com"
    DEFAULT_ADMIN_NAME = "admin"
    DEFAULT_ADMIN_PASSWORD = "admin"
    
    def __init__(self, root):
        super().__init__(root)
        self.users = self.root["users"]
        self.sessions = self.root["sessions"]
        
        # default admin user
        self.create_new_user(self.DEFAULT_ADMIN_EMAIL, self.DEFAULT_ADMIN_NAME, self.DEFAULT_ADMIN_PASSWORD)

    def calculate_uuid(self, email) -> str:
        return str(uuid.uuid3(uuid.NAMESPACE_URL, email.lower()))

    def create_new_user(self, email: str, name: str, password: str, is_admin: bool = False):
        user_uuid = self.calculate_uuid(email)
        if not self.users.get(user_uuid):
            user = User(user_uuid, email=email.lower(), name=name, password_hash=generate_password_hash(password), is_admin=is_admin)
            
            self.users[user_uuid] = user
            return user
        else:
            return None

    def get_user_from_email(self, email: str) -> User:
        user_uuid = self.calculate_uuid(email)
        
        return self.users.get(user_uuid)
    
    def get_user_from_uuid(self, uuid) -> User:
        return self.users.get(uuid)
    
    def get_users(self):
        return [self.users.get(user) for user in self.users]
    
    def delete_user_from_email(self, email):
        uuid = self.calculate_uuid(email)
        return self.delete_user_from_uuid(uuid)

    def delete_user_from_uuid(self, uuid) -> bool:
        if uuid in self.users:
            del self.users[uuid]
            return True
        else:
            return False

    def edit_user(self, old_uuid, email, name, password, is_admin) -> bool:
        if old_uuid not in self.users:
            return False
        
        new_uuid = self.calculate_uuid(email)

        # handle changing email
        
        self.users[old_uuid].edit(new_uuid, email, name, password, is_admin)
        if new_uuid != old_uuid:
            self.users[new_uuid] = self.users[old_uuid]
            
            # remove reference to old uuid
            del self.users[old_uuid]
            
        return True

    def edit_playlist(self, user_id, playlist_id, playlist_name):
        if user_id in self.users:
            playlist: Playlist = self.get_playlist(user_id, playlist_id)
            playlist.set_name(playlist_name)
            playlist.set_file_name(playlist_id)

    def add_session(self, session_id: str, user_uuid: str, expiry_time: datetime.timedelta) -> bool:
        if user_uuid not in self.users:
            return False
        
        self.sessions[session_id] = {
            "session_id": session_id,
            "user_uuid": user_uuid,
            "expiry": datetime.datetime.now() + expiry_time
        }
        
        return True
    
    def delete_session(self, session_id: str):
        del self.sessions[session_id]

    def get_session(self, session_id: str):
        if session_id in self.sessions:
            return self.sessions[session_id]

    # -- playlists --
    def create_empty_playlist(self, user_uuid):
        user = self.users[user_uuid]

        playlist_uuid = str(uuid.uuid4())
        playlist = Playlist(playlist_uuid, "Untitled Playlist", user)

        user.add_playlist(playlist)
        
        return playlist

    def get_playlist(self, user_uuid, playlist_uuid):
        user: User = self.users[user_uuid]
        
        playlists: list[Playlist] = user.get_playlists()
        for playlist in playlists:
            if playlist.get_uuid() == playlist_uuid:
                return playlist

class MusicManager(Manager):
    def __init__(self, root):
        super().__init__(root)
        self.songs = self.root["songs"]
        self.artists = self.root["artists"]
        self.albums = self.root["albums"]
        self.genres = self.root["genres"]
    
    # -- songs --
    def create_new_song(self, song_title: str, genres: list[str], artists: list[str]):
        song_uuid = str(uuid.uuid4())
        if self.songs.get(song_uuid):
            return None
        
        genre_list = [self.genres[g] for g in genres]
        artist_list = [self.artists[a] for a in artists]
        
        song = Song(song_uuid, song_title, genre_list, artist_list)

        for g in genres:
            self.genres[g].add_song(song)
            
        for a in artists:
            self.artists[a].add_song(song)

        self.songs[song_uuid] = song
        return song

    def get_song_from_uuid(self, uuid) -> Song:
        return self.songs.get(uuid)
    
    def get_songs(self) -> list[Song]:
        return [val for val in self.songs.values()]
    
    def delete_song_from_uuid(self, uuid):
        if uuid in self.songs:
            # just in case
            # self.delete_song_file(uuid)
            
            for a in self.artists:
                self.artists[a].delete_song(self)
            
            del self.songs[uuid]
            return True
        else:
            return False
    
    def edit_song(self, uuid, title, genres, artists):
        if uuid not in self.songs:
            return False
        
        self.songs[uuid].edit(title, genres, artists)
        
        return True
    
    # -- artists --
    def create_new_artist(self, name):
        artist_uuid = str(uuid.uuid4())
        if self.artists.get(artist_uuid):
            return None
        
        artist = Artist(artist_uuid, name)

        self.artists[artist_uuid] = artist
        return artist

    def get_artist_from_uuid(self, uuid) -> Artist:
        return self.artists.get(uuid)

    def get_artists(self) -> list[Artist]:
        return [val for val in self.artists.values()]

    def delete_artist_from_uuid(self, uuid):
        if uuid in self.artists:
            for a in self.artists[uuid].get_albums():
                a.delete_artist(self.artists[uuid])
            
            for s in self.artists[uuid].get_songs():
                s.delete_artist(self.artists[uuid])
                
            del self.artists[uuid]
            return True
        else:
            return False
    
    def edit_artist(self, uuid, name):
        if uuid not in self.artists:
            return False
        
        self.artists[uuid].edit(name)
        
        return True

    # -- albums --
    def create_new_album(self, album_title: str, artists: list[str], songs: list[str]):
        album_uuid = str(uuid.uuid4())

        if self.albums.get(album_uuid):
            return None
        
        artist_list = [self.artists[a] for a in artists]
        song_list = [self.songs[s] for s in songs] 
        album = Album(album_uuid, album_title, artist_list, song_list)
        for a in artists:
            self.artists[a].add_album(album)
            
        for s in songs:
            self.songs[s].set_album(album)

        self.albums[album_uuid] = album
        return album
    
    def get_album_from_uuid(self, uuid) -> Album:
        return self.albums.get(uuid)

    def get_albums(self) -> list[Album]:
        return [val for val in self.albums.values()]

    def delete_album_from_uuid(self, uuid):
        if uuid not in self.albums:
            return False
        
        del self.albums[uuid]
        return True
    
    def edit_album(self, uuid, title, artists, song):
        if uuid not in self.albums:
            return False
        
        self.albums[uuid].edit(title, artists, song)
        return True
    
    # -- genre --
    def create_new_genre(self, genre_name, genre_color):
        genre_uuid = str(uuid.uuid4())
        
        if self.genres.get(genre_uuid):
            return None
        
        genre = Genre(genre_uuid, genre_name, genre_color)

        self.genres[genre_uuid] = genre
        
        return genre
    
    def get_genre_from_uuid(self, uuid) -> Genre:
        return self.genres.get(uuid)

    def get_genres(self) -> list[Genre]:
        return [val for val in self.genres.values()]
    
    def delete_genre_from_uuid(self, uuid) -> bool:
        if uuid in self.genres:
            del self.genres[uuid]
            return True
        else:
            return False
            
    def edit_genre(self, old_uuid, genre_name, genre_color) -> bool:
        if old_uuid not in self.genres:
            return False
        
        self.genres[old_uuid].edit(genre_name, genre_color)
        
        return True

class DBManager:
    INITIAL = ["users", "songs", "artists", "albums", "genres", "sessions"]
    CONFIG_PATH = "./config.xml"
    
    def __init__(self):
        # initialize database
        # try:
        self.storage = ZODB.FileStorage.FileStorage("instances/database.fs")
        self.db = ZODB.DB(self.storage)
        # except zc.lockfile.LockError:
        #     os.remove("instances/database.fs.lock")
        #     self.storage = ZODB.FileStorage.FileStorage("instances/database.fs")
        #     self.db = ZODB.DB(self.storage)
        
        # self.db = ZODB.config.databaseFromURL(self.CONFIG_PATH)
        
        self.connection = self.db.open()
        self.root = self.connection.root()
        
        for table in self.INITIAL:
            if table not in self.root:
                self.root[table] = BTree()
        
    def get_root(self):
        return self.root
        
    def shutdown_database(self):
        print("Shutting down database...")
        transaction.commit()
        
        self.connection.close()
        self.db.close()
        self.storage.close()