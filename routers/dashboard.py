from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db
from sqlalchemy.orm import Session
from models import Diary
from utils.auth_utils import get_current_user

router = APIRouter(tags=["Dashboard"])
templates = Jinja2Templates(directory="templates")

# ===========================
# 📜 HTML Endpoint (Swagger’da görünmez)
# ===========================
@router.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(
    request: Request,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = db.query(Diary).filter_by(user_id=current_user["user_id"]).order_by(Diary.timestamp.asc()).all()
    recent_entries = [{
        "date": e.timestamp.strftime("%d.%m.%Y"),
        "content": e.content,
        "emotion": e.emotion
    } for e in entries[-5:]]

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": current_user["username"],
        "recent_entries": recent_entries
    })

# ===========================
# 📜 JSON Endpoint (Swagger’da görünür)
# ===========================
@router.get("/dashboard-data", summary="Get Dashboard Data (JSON)")
async def dashboard_data(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = db.query(Diary).filter_by(user_id=current_user["user_id"]).order_by(Diary.timestamp.asc()).all()
    recent_entries = [{
        "date": e.timestamp.strftime("%d.%m.%Y"),
        "content": e.content,
        "emotion": e.emotion
    } for e in entries[-5:]]

    return {"username": current_user["username"], "recent_entries": recent_entries}
