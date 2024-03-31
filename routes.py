from fastapi import APIRouter, Depends, Request, Body, Form, File, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from auth import current_user
from server import user_manager, music_manager
from models import Song
from werkzeug.security import generate_password_hash
import shutil
from pathlib import Path

main = APIRouter()
templates = Jinja2Templates(directory="templates")

# -- utilities --

# def get_context(request: Request, user=Depends(current_user)):
#     context = {"request": request}
    
#     if user is not None:
#         context["logged_in"] = True
#         context["user"] = user
#     return context

async def upload_file(file: UploadFile, file_types: list[str], file_path: str):
    # get the file size (in bytes)
    file.file.seek(0, 2)
    file_size = file.file.tell()

    # move the cursor back to the beginning
    await file.seek(0)

    if file_size > 10 * 1024 * 1024:
        # more than 10 MB
        raise HTTPException(status_code=400, detail="File too large")

    # check the content type
    content_type = file.content_type
    if content_type not in file_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return True

# -- views -- 
@main.get("/", response_class=HTMLResponse)
@main.get("/dashboard/", response_class=HTMLResponse)
@main.get("/dashboard/home", response_class=HTMLResponse)
def dashboard_home(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_home.html", {"request": request})

# manage users
@main.get("/dashboard/users", response_class=HTMLResponse)
def dashboard_users(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_users.html", {
        "request": request,
        "users": user_manager.get_users()
    })

@main.get("/dashboard/users/add", response_class=HTMLResponse)
def dashboard_users_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_users_form.html", {"request": request})

@main.post("/dashboard/users/add", response_class=HTMLResponse)
def dashboard_users_add_submit(
        request: Request,
        user = Depends(current_user),
        email: str = Form(...),
        username: str = Form(...),
        password: str = Form(...),
        is_admin: bool = Form(...)):

    print(email, username, password)
    
    success = user_manager.create_new_user(email, username, password, is_admin)
    
    if success:
        return RedirectResponse("/dashboard/users", status_code=302)
    else:
        return templates.TemplateResponse("dashboard_users_form.html", {
            "request": request,
            "message": "Email already in use."
        })

@main.get("/dashboard/users/{user_id}", response_class=HTMLResponse)
def dashboard_users_edit(user_id: str, request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_users_form.html", {
        "request": request,
        "edit_user": user_manager.get_user_from_uuid(user_id)
    })

@main.post("/dashboard/users/{user_id}", response_class=HTMLResponse)
def dashboard_users_edit_submit(
        request: Request,
        user_id: str,
        action: str = Form(...),
        user = Depends(current_user),
        email: str = Form(...),
        username: str = Form(...),
        password: str = Form(None),
        is_admin: bool = Form(...)):
    
    if not user_manager.get_user_from_uuid(user_id):
        return

    if action == "delete":
        user_manager.delete_user_from_uuid(user_id)
    elif action == "edit":
        print(user_id, email, username, password, is_admin)
        if not password:
            password_hash = user_manager.get_user_from_uuid(user_id).password_hash
        else:
            password_hash = generate_password_hash(password)
            
        user_manager.edit_user(user_id, email, username, password_hash, is_admin)
    
    return RedirectResponse("/dashboard/users", status_code=302)

# manage music
MUSIC_FOLDER_PATH = "uploads/"
SONG_FOLDER_PATH = "media/"
ALBUM_COVER_FOLDER_PATH = "album_covers/"
GENRE_FOLDER_PATH = "genre/"

@main.get("/dashboard/music", response_class=HTMLResponse)
def dashboard_music(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_music.html", {
        "request": request,
        "songs": music_manager.get_songs(),
        "artists": music_manager.get_artists(),
        "albums": music_manager.get_albums(),
        "genres": music_manager.get_genres()
    })

# -- songs --
@main.get("/dashboard/music/songs/add", response_class=HTMLResponse)
def dashboard_songs_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_song_form.html", {
        "request": request,
        "genres": music_manager.get_genres(),
        "artists": music_manager.get_artists()
    })

@main.post("/dashboard/music/songs/add", response_class=HTMLResponse)
async def dashboard_songs_add_submit(
        request: Request,
        user = Depends(current_user),
        song_title: str = Form(...),
        genres: list[str] = Form(...),
        artists: list[str] = Form(...),
        song_file: UploadFile = File(...)):
    
    song: Song = music_manager.create_new_song(song_title, genres, artists)
    
    if song:
        success = await upload_file(song_file, ["audio/mpeg"], MUSIC_FOLDER_PATH + SONG_FOLDER_PATH + song.uuid + Path(song_file.filename).suffix)
    
    if song and success:
        return RedirectResponse("/dashboard/music", status_code=302)
    else:
        return templates.TemplateResponse("dashboard_song_form.html", {
            "request": request,
            "message": "Failed to create song."
        })

@main.get("/dashboard/music/songs/{song_id}", response_class=HTMLResponse)
def dashboard_songs_edit(song_id: str, request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_song_form.html", {
        "request": request,
        "edit_song": music_manager.get_song_from_uuid(song_id),
        "genres": music_manager.get_genres(),
        "artists": music_manager.get_artists()
    })

@main.post("/dashboard/music/songs/{song_id}", response_class=HTMLResponse)
async def dashboard_songs_edit_submit(
        request: Request,
        song_id: str,
        action: str = Form(...),
        user = Depends(current_user),
        song_title: str = Form(...),
        genres: list[str] = Form(None),
        artists: list[str] = Form(None),
        song_file: UploadFile = File(None)):
    
    song = music_manager.get_song_from_uuid(song_id)
    
    if not song:
        return
    
    if song_file.filename:
        success = await upload_file(song_file, ["audio/mpeg"], MUSIC_FOLDER_PATH + SONG_FOLDER_PATH + song.uuid + Path(song_file.filename).suffix)
    else:
        success = True
    
    if success:
        if action == "delete":
            music_manager.delete_song_from_uuid(song_id)
        elif action == "edit":
            if genres == None:
                genres = song.get_genres()
            if artists == None:
                artists = song.get_artists()
            
            music_manager.edit_song(song_id, song_title, genres, artists)
    
        return RedirectResponse("/dashboard/music", status_code=302)

# -- artists --
@main.get("/dashboard/music/artists/add", response_class=HTMLResponse)
def dashboard_artists_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_artists_form.html", {"request": request})

@main.get("/dashboard/music/artists/add", response_class=HTMLResponse)
def dashboard_artists_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_artists_form.html", {"request": request})

@main.post("/dashboard/music/artists/add", response_class=HTMLResponse)
def dashboard_artists_add_submit(
        request: Request,
        user = Depends(current_user),
        name: str = Form(...)
    ):
    
    artist = music_manager.create_new_artist(name)
    
    if artist:
        return RedirectResponse("/dashboard/music", status_code=302)
    else:
        return templates.TemplateResponse("dashboard_songs_form.html", {
            "request": request,
            "message": "Failed to create song."
        })

@main.get("/dashboard/music/artists/{artist_id}", response_class=HTMLResponse)
def dashboard_artists_edit(artist_id: str, request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_artists_form.html", {
        "request": request,
        "edit_artist": music_manager.get_artist_from_uuid(artist_id)
    })

@main.post("/dashboard/music/artists/{artist_id}", response_class=HTMLResponse)
def dashboard_artists_edit_submit(
        request: Request,
        artist_id: str,
        action: str = Form(...),
        user = Depends(current_user),
        name: str = Form(...)):
    
    if not music_manager.get_artist_from_uuid(artist_id):
        return
    
    if action == "delete":
        music_manager.delete_artist_from_uuid(artist_id)
    elif action == "edit":            
        music_manager.edit_artist(artist_id, name)
    
    return RedirectResponse("/dashboard/music", status_code=302)

# -- albums --
@main.get("/dashboard/music/albums/add", response_class=HTMLResponse)
def dashboard_albums_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_albums_form.html", {
        "request": request,
        "artists": music_manager.get_artists(),
        "songs": music_manager.get_songs()
    })

@main.post("/dashboard/music/albums/add", response_class=HTMLResponse)
async def dashboard_albums_add_submit(
        request: Request,
        user = Depends(current_user),
        album_title: str = Form(...),
        artists: list[str] = Form(...),
        songs: list[str] = Form(...),
        album_cover: UploadFile = Form(...)):
    
    album = music_manager.create_new_album(album_title, artists, songs)
    
    if album:
        success = await upload_file(album_cover, ["image/gif", "image/jpeg", "image/png"], MUSIC_FOLDER_PATH + ALBUM_COVER_FOLDER_PATH + album.uuid + Path(album_cover.filename).suffix)
    
    if album and success:
        return RedirectResponse("/dashboard/music", status_code=302)
    else:
        return templates.TemplateResponse("dashboard_albums_form.html", {
            "request": request,
            "message": "Album already exists."
        })

@main.get("/dashboard/music/albums/{album_id}", response_class=HTMLResponse)
def dashboard_albums_edit(album_id: str, request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_albums_form.html", {
        "request": request,
        "edit_album": music_manager.get_album_from_uuid(album_id),
        "artists": music_manager.get_artists(),
        "songs": music_manager.get_songs()
    })

@main.post("/dashboard/music/albums/{album_id}", response_class=HTMLResponse)
async def dashboard_albums_edit_submit(
        request: Request,
        album_id: str,
        action: str = Form(...),
        user = Depends(current_user),
        album_title: str = Form(...),
        artists: list[str] = Form(None),
        songs: list[str] = Form(None),
        album_cover: UploadFile = Form(None)):

    album = music_manager.get_album_from_uuid(album_id)

    if not album:
        return
    
    if album_cover.filename:
        success = await upload_file(album_cover, ["image/gif", "image/jpeg", "image/png"], MUSIC_FOLDER_PATH + ALBUM_COVER_FOLDER_PATH + album.uuid + Path(album_cover.filename).suffix)
    else:
        success = True
    
    if success:
        if action == "delete":
            music_manager.delete_album_from_uuid(album_id)
        elif action == "edit":
            if artists == None:
                artists = album.get_artists()
            if songs == None:
                songs = album.get_songs()
            music_manager.edit_album(album_id, album_title, artists, songs)
        return RedirectResponse("/dashboard/music", status_code=302)

# -- genre --
@main.get("/dashboard/music/genres/add", response_class=HTMLResponse)
def dashboard_genres_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_genres_form.html", {"request": request})

@main.post("/dashboard/music/genres/add", response_class=HTMLResponse)
async def dashboard_genres_add_submit(
        request: Request,
        user = Depends(current_user),
        genre_name: str = Form(...),
        genre_image: UploadFile = Form(...)):
    
    genre = music_manager.create_new_genre(genre_name)
    
    if genre:
        success = await upload_file(genre_image, ["image/gif", "image/jpeg", "image/png"], MUSIC_FOLDER_PATH + GENRE_FOLDER_PATH + genre.uuid + Path(genre_image.filename).suffix)
    
    if success:
        return RedirectResponse("/dashboard/music", status_code=302)
    else:
        return templates.TemplateResponse("dashboard_genres_form.html", {
            "request": request,
            "message": "Genre already exists."
        })
    
@main.get("/dashboard/music/genres/{genre_id}", response_class=HTMLResponse)
def dashboard_genres_edit(genre_id: str, request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_genres_form.html", {
        "request": request,
        "edit_genre": music_manager.get_genre_from_uuid(genre_id)
    })

@main.post("/dashboard/music/genres/{genre_id}", response_class=HTMLResponse)
async def dashboard_genres_edit_submit(
        request: Request,
        genre_id: str,
        action: str = Form(...),
        user = Depends(current_user),
        genre_name: str = Form(...),
        genre_image: UploadFile = Form(None)):
    
    genre = music_manager.get_genre_from_uuid(genre_id)
    
    if not genre:
        return
    
    if genre_image.filename:
        success = await upload_file(genre_image, ["image/gif", "image/jpeg", "image/png"], MUSIC_FOLDER_PATH + GENRE_FOLDER_PATH + genre.uuid + Path(genre_image.filename).suffix)
    else:
        success = True
    
    if success:
        if action == "delete":
            music_manager.delete_genre_from_uuid(genre_id)
        elif action == "edit":
            if not genre_name:
                return templates.TemplateResponse("dashboard_genres_form.html", {
                    "request": request,
                    "message": "Genre name is missing"
                })
            music_manager.edit_genre(genre_id, genre_name)
        return RedirectResponse("/dashboard/music", status_code=302)

# --- client ---
def authorized_session_id(self):
    pass

# -- get user info --
@main.get("/user-info")
def get_user_info(user=Depends(authorized_session_id)):
    pass

# -- handle streaming --
CHUNK_SIZE = 1024

# DEMO
@main.get("/stream-audio/")
async def stream_audio():
    def iterate_audio():
        try:
            with open(MUSIC_FOLDER_PATH + SONG_FOLDER_PATH + "demo.mp3", "rb") as audio_file:
                while True:
                    chunk = audio_file.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    yield chunk
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Audio file not found")

    return StreamingResponse(iterate_audio(), media_type="audio/mpeg")
