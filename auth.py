from fastapi import APIRouter, Depends, Request, Form, Body
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, UTC
from email.utils import parseaddr
from server import user_manager, app
from models import User

import os
import secrets
from dotenv import load_dotenv

# load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# set router
auth = APIRouter()
templates = Jinja2Templates(directory="templates")

# initialize login manager
login_manager = LoginManager(SECRET_KEY, token_url="/login", use_cookie=True)
login_manager.cookie_name = "session"

# exception handling for pages that need login
class RequiresLogin(Exception):
    pass

# https://stackoverflow.com/questions/71657407/how-to-redirect-to-login-in-fastapi
@app.exception_handler(RequiresLogin)
async def requires_login(request: Request, _: Exception):
    return RedirectResponse(f"/login", status_code=302)

def current_user(request: Request, user=Depends(login_manager.optional)):
    if not user:
        raise RequiresLogin("You must be logged in to access this")

    return user

@login_manager.user_loader()
def load_user(email) -> User:
    return user_manager.get_user_from_email(email)

@auth.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/login")
async def handle_dashboard_login(request: Request, email: str = Form(...), password: str = Form(...), remember: bool = Form(False)):
    email = email.lower()
    
    user = load_user(email)

    # check if user exists and password is correct
    if not user or not check_password_hash(user.get_password_hash(), password):
        return templates.TemplateResponse("login.html", {"request": request, "message": "Incorrect email/password."})

    # handle remember me button
    expiry_time = timedelta(days=7) if remember else timedelta(minutes=15)
    
    access_token = login_manager.create_access_token(
        data={"sub": email}, expires=expiry_time
    )
    
    # successful login
    response = RedirectResponse(url="/", status_code=302)
    login_manager.set_cookie(response, access_token)
    
    return response

@auth.get("/logout")
def logout(user = Depends(login_manager.optional)):
    response = RedirectResponse("/login", status_code=302)
    
    # remove the cookie to log the user out
    if user is not None:
        response.delete_cookie(key="session")
    return response

# -- client --
def create_session(user_uuid: str, expiry_time: timedelta):
    session_id = secrets.token_urlsafe(32)
    user_manager.add_session(session_id, user_uuid, expiry_time)
    return session_id

@auth.post("/client-login")
def handle_client_login(request: Request, email: str = Body(...), password: str = Body(...), remember: bool = Body(False)):
    email = email.lower()
    
    user = load_user(email)

    # check if user exists and password is correct
    if not user or not check_password_hash(user.get_password_hash(), password):
        return JSONResponse(status_code=401, content={
            "message": "Incorrect credentials"
        })

    # handle remember me button
    expiry_time = timedelta(days=7) if remember else timedelta(minutes=15)
    
    # session cookie
    session_id = create_session(user.get_uuid(), expiry_time)
    
    response = JSONResponse(status_code=200, content={
        "message": "Logged in successfully"
    })
    
    response.set_cookie(
        key="session",
        value=session_id,
        expires=datetime.now(UTC) + expiry_time
    )
    
    # successful login
    return response

@auth.post("/client-register")
async def handle_client_register(request: Request, email: str = Body(...), name: str = Body(...), password: str = Body(...), repassword: str = Body(...) ):
    
    # validate email format
    if "@" not in parseaddr(email)[1]:
        return JSONResponse(status_code=400, content={"message": "Invalid email format"})
    
    user = load_user(email)
    
    # check if user already exists
    if user:
        return JSONResponse(status_code=400, content={"message": "User already exists"})
    
    # verify password entered correctly
    if password != repassword:
        return JSONResponse(status_code=400, content={"message": "Passwords not the same"})
    
    # create new user and update the database
    user_manager.create_new_user(email, name, generate_password_hash(password), is_admin=False)
    user_manager.commit()

    # successful registration
    return JSONResponse(status_code=200, content={"message": "Registered successfully"})
