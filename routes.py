from fastapi import APIRouter, Depends, Request, Body, Form, File, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from auth import current_user
from server import user_manager
from werkzeug.security import generate_password_hash

main = APIRouter()
templates = Jinja2Templates(directory="templates")

# -- utilities --

# def get_context(request: Request, user=Depends(current_user)):
#     context = {"request": request}
    
#     if user is not None:
#         context["logged_in"] = True
#         context["user"] = user
#     return context

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
        # todo: exception or something for nonexistant user
        return
    
    print(action)
    
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
@main.get("/dashboard/music", response_class=HTMLResponse)
def dashboard_music(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_music.html", {"request": request})

@main.get("/dashboard/music/add", response_class=HTMLResponse)
def dashboard_music_add(request: Request, user=Depends(current_user)):
    return templates.TemplateResponse("dashboard_song_form.html", {"request": request})

# -- handle streaming --
CHUNK_SIZE = 1024
MEDIA_PATH = "static/media/"

# DEMO
@main.get("/stream-audio")
async def stream_audio():
    def iterate_audio():
        try:
            with open(MEDIA_PATH + "demo.mp3", "rb") as audio_file:
                while True:
                    chunk = audio_file.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    yield chunk
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Audio file not found")

    return StreamingResponse(iterate_audio(), media_type="audio/mpeg")
