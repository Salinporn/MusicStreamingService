import ZODB, ZODB.FileStorage, ZODB.config
import zc.lockfile
from BTrees._OOBTree import BTree
import os
import transaction
from models import User
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

    def add_session(self, session_id: str, user_uuid: str, expiry_time: datetime.timedelta) -> bool:
        if user_uuid not in self.users:
            return False
        
        self.sessions[session_id] = {
            "session_id": session_id,
            "user_uuid": user_uuid,
            "expiry": datetime.datetime.now() + expiry_time
        }
        
        return True

class DBManager:
    INITIAL = ["users", "sessions"]
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