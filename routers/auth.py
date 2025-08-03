from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User
from utils.auth_utils import hash_password, verify_password, create_access_token

router = APIRouter(tags=["authentication"])
templates = Jinja2Templates(directory="templates")

# 📌 DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🟢 Kayıt Sayfası (GET)
@router.get("/register", response_class=HTMLResponse)
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "message": ""})


@router.post("/register")
async def register_post(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    hashed_pw = hash_password(password)
    user = User(username=username, password=hashed_pw)

    try:
        db.add(user)
        db.commit()
        if "application/json" in request.headers.get("accept", ""):
            return JSONResponse({"message": "Kayıt başarılı"})
        return RedirectResponse(url="/login", status_code=303)
    except IntegrityError:
        db.rollback()
        if "application/json" in request.headers.get("accept", ""):
            return JSONResponse({"error": "Kullanıcı adı mevcut"})
        return templates.TemplateResponse("register.html", {
            "request": request,
            "message": "Kullanıcı adı zaten mevcut."
        })


# 🟢 Login Sayfası (GET)
@router.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "message": ""})

# 🟢 Login İşlemi (POST)
@router.post("/login")
async def login_post(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    # Kullanıcı yok veya şifre yanlış
    if not user or not verify_password(password, user.password):
        if "application/json" in request.headers.get("accept", ""):
            return JSONResponse({"error": "Geçersiz giriş bilgileri"}, status_code=401)
        return templates.TemplateResponse("login.html", {
            "request": request,
            "message": "Geçersiz giriş bilgileri."
        })

    # JWT Token oluştur
    token = create_access_token({"sub": str(user.id), "username": user.username})

    # Accept Header JSON ise JSON döndür
    if "application/json" in request.headers.get("accept", ""):
        return JSONResponse({"message": "Giriş başarılı", "access_token": token})

    # Tarayıcı ise Cookie ayarla ve yönlendir
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="access_token", value=token, httponly=True, max_age=3600)
    return response

@router.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(url="/", status_code=303)  # index.html'e yönlendir
    response.delete_cookie("access_token")  # Token'ı sil
    return response
