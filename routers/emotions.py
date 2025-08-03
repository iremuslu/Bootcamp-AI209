from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from utils.auth_utils import get_current_user
from database import get_db
from models import Diary
from app.emotion_map import EMOTION_MAP

router = APIRouter(
    tags=["Emotion Graph"]
)
templates = Jinja2Templates(directory="templates")

# ===========================
# 📜 HTML Endpoint (Swagger’da görünmez)
# ===========================
@router.get("/emotion-graph", response_class=HTMLResponse, include_in_schema=False)
async def emotion_graph(
    request: Request,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = db.query(Diary).filter_by(user_id=current_user["user_id"]).order_by(Diary.timestamp.asc()).all()
    data = [{
        "label": e.timestamp.strftime("%d.%m.%Y"),
        "emotion": e.emotion,
        "score": EMOTION_MAP.get(e.emotion, {"score": 8})["score"],
        "emoji": EMOTION_MAP.get(e.emotion, {"emoji": "😐"})["emoji"]
    } for e in entries]

    return templates.TemplateResponse("emotion_graph.html", {
        "request": request,
        "username": current_user["username"],
        "data": data
    })

# ===========================
# 📜 JSON Endpoint (Swagger’da görünür)
# ===========================
@router.get("/emotion-graph-data", summary="Get Emotion Graph Data (JSON)")
async def emotion_graph_data(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = db.query(Diary).filter_by(user_id=current_user["user_id"]).order_by(Diary.timestamp.asc()).all()
    data = [{
        "label": e.timestamp.strftime("%d.%m.%Y"),
        "emotion": e.emotion,
        "score": EMOTION_MAP.get(e.emotion, {"score": 8})["score"],
        "emoji": EMOTION_MAP.get(e.emotion, {"emoji": "😐"})["emoji"]
    } for e in entries]
    return {"data": data}
