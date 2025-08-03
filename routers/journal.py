from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime

from utils.auth_utils import get_current_user
from database import get_db
from models import Diary
from app.sentiment import analyze_sentiment
from app.badge_logic import check_and_award_badges
from utils.timezone_utils import TURKEY_TZ

router = APIRouter(
    tags=["Journal"]
)
templates = Jinja2Templates(directory="templates")

# ===========================
# 📜 HTML Endpoint (Swagger’da görünmez)
# ===========================
@router.get("/journal", response_class=HTMLResponse, include_in_schema=False)
async def journal(request: Request, current_user: dict = Depends(get_current_user)):
    return templates.TemplateResponse("journal.html", {
        "request": request,
        "username": current_user["username"]
    })

# ===========================
# 📜 JSON Endpoint (Swagger’da görünür)
# ===========================
@router.post("/diary", summary="Create Diary Entry (JSON)")
async def diary_post(
    content: str = Form(...),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        sentiment, score, comment, suggestions = analyze_sentiment(content)
    except Exception:
        sentiment, comment, suggestions = "Bilinmiyor", "Analiz yapılamadı", ""

    new_diary = Diary(
        user_id=current_user["user_id"],
        content=content,
        timestamp=datetime.now(TURKEY_TZ),
        emotion=sentiment,
        comment=comment,
        suggestions=suggestions
    )

    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)

    # Rozet kontrolü
    check_and_award_badges(current_user["user_id"], db)

    return JSONResponse({
        "message": "Günlük kaydedildi!",
        "sentiment": sentiment,
        "comment": comment,
        "suggestions": suggestions
    })
