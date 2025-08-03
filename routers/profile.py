from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import extract, and_, or_
from datetime import datetime
import calendar

from utils.auth_utils import get_current_user
from database import get_db
from models import User, Diary, Badge, UserBadge
from app.emotion_map import EMOTION_MAP
from utils.timezone_utils import to_turkey_time, TURKEY_TZ

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

TURKISH_MONTHS = [
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
]

# ===========================
# 📜 HTML Endpoint (Swagger’da görünmez)
# ===========================
@router.get("", response_class=HTMLResponse, include_in_schema=False)
async def profile_page(
    request: Request,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    month: int = Query(None),
    year: int = Query(None)
):
    today = datetime.now()
    current_month = month if month else today.month
    current_year = year if year else today.year

    month_name = TURKISH_MONTHS[current_month - 1]
    days_in_month = calendar.monthrange(current_year, current_month)[1]

    user = db.query(User).filter_by(id=current_user["user_id"]).first()

    entries = db.query(Diary).filter(
        Diary.user_id == current_user["user_id"],
        extract('month', Diary.timestamp) == current_month,
        extract('year', Diary.timestamp) == current_year
    ).order_by(Diary.timestamp.asc()).all()

    total_entries = db.query(Diary).filter(Diary.user_id == current_user["user_id"]).count()
    emotions = [e.emotion for e in entries if e.emotion]
    most_frequent_emotion = max(set(emotions), key=emotions.count) if emotions else "Belirsiz"

    # ✅ Türkiye saatine çevrilmiş en son kayıt
    last_entry_time = (
        to_turkey_time(entries[-1].timestamp).strftime("%d.%m.%Y %H:%M")
        if entries else "Yok"
    )

    scores = [EMOTION_MAP.get(e, {"score": 8})["score"] for e in emotions]
    avg_score = round(sum(scores) / len(scores)) if scores else 8
    avg_emotion = next((k for k, v in EMOTION_MAP.items() if v["score"] == avg_score), "Nötr")

    # ✅ Rozetlerde Türkiye saatine dönüşüm
    user_badges = (
        db.query(UserBadge)
        .join(Badge)
        .filter(UserBadge.user_id == current_user["user_id"])
        .all()
    )
    badges = [
        {
            "name": ub.badge.name,
            "description": ub.badge.description,
            "icon": ub.badge.icon,
            "earned_at": to_turkey_time(ub.earned_at).strftime("%d.%m.%Y")
        }
        for ub in user_badges
    ]

    # 🔹 Günlükleri takvim günlerine bağlama (Türkiye saatiyle)
    days_data = []
    for day in range(1, days_in_month + 1):
        day_entries = [
            {
                "emoji": EMOTION_MAP.get(entry.emotion, {}).get("emoji", "❓"),
                "emotion": entry.emotion,
                "note": entry.content,
                "date": to_turkey_time(entry.timestamp).strftime("%Y-%m-%d"),
                "color": EMOTION_MAP.get(entry.emotion, {}).get("color", "#555")
            }
            for entry in entries
            if to_turkey_time(entry.timestamp).day == day
        ]
        days_data.append({
            "number": day,
            "entries": day_entries
        })

    last_emotion = entries[-1].emotion if entries else "Belirsiz"
    last_emotion_color = EMOTION_MAP.get(last_emotion, {}).get("color", "#555")

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "username": current_user["username"],
        "created_at": to_turkey_time(user.created_at).strftime("%d.%m.%Y") if user else "Bilinmiyor",
        "total_entries": total_entries,
        "most_frequent_emotion": f"{EMOTION_MAP[last_emotion]['emoji']} {last_emotion}" if last_emotion in EMOTION_MAP else last_emotion,
        "last_emotion_color": last_emotion_color,
        "last_entry_time": last_entry_time,
        "average_emotion": f"{EMOTION_MAP[avg_emotion]['emoji']} {avg_emotion}",
        "current_month": current_month,
        "current_year": current_year,
        "month_name": month_name,
        "days": days_data,
        "badges": badges,
        "EMOTION_MAP": EMOTION_MAP
    })

