import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from database import DBManager, UserManager, MusicManager

db_manager = DBManager()
root = db_manager.get_root()

user_manager = UserManager(root)
music_manager = MusicManager(root)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    
    # on shutdown
    db_manager.shutdown_database()
    
# initial config
app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

# include routers
from routes import main as main_router
from auth import auth as auth_router
app.include_router(main_router)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)