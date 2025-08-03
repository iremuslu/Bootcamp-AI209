from fastapi import APIRouter, Request, Form, Depends, Query, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from utils.auth_utils import get_current_user
from database import get_db
from models import Diary
from app.emotion_map import EMOTION_MAP

router = APIRouter(tags=["Entries"])
templates = Jinja2Templates(directory="templates")

# ===========================
# 📜 HTML Endpoints (Swagger’da görünmez)
# ===========================

@router.get("/all-entries", response_class=HTMLResponse, include_in_schema=False)
async def all_entries(
    request: Request,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    date: str = Query(None)
):
    query = db.query(Diary).filter_by(user_id=current_user["user_id"])
    if date:
        try:
            selected_date = datetime.strptime(date, "%Y-%m-%d").date()
            query = query.filter(func.date(Diary.timestamp) == selected_date)
        except ValueError:
            pass

    entries = query.order_by(Diary.timestamp.asc()).all()

    return templates.TemplateResponse("all_entries.html", {
        "request": request,
        "entries": entries,
        "username": current_user["username"],
        "emotion_map": EMOTION_MAP
    })


@router.get("/delete-entry/{entry_id}", include_in_schema=False)
async def delete_entry(entry_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Günlük bulunamadı.")
    db.delete(entry)
    db.commit()
    return RedirectResponse(url="/all-entries", status_code=303)


@router.get("/edit-entry/{entry_id}", response_class=HTMLResponse, include_in_schema=False)
async def edit_entry_form(request: Request, entry_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Günlük bulunamadı.")
    return templates.TemplateResponse("edit_entry.html", {
        "request": request,
        "entry": entry,
        "username": current_user["username"]
    })


@router.post("/edit-entry/{entry_id}", include_in_schema=False)
async def edit_entry_save(entry_id: int, content: str = Form(...), emotion: str = Form(...),
                          current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Günlük bulunamadı.")
    entry.content = content
    entry.emotion = emotion
    db.commit()
    return RedirectResponse(url="/all-entries", status_code=303)

# ===========================
# 📜 JSON CRUD Endpoints (Swagger’da görünür)
# ===========================

@router.get("/api/entries", summary="Get All Entries (JSON)")
async def get_all_entries_api(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = db.query(Diary).filter_by(user_id=current_user["user_id"]).all()
    return [
        {"id": e.id, "content": e.content, "emotion": e.emotion, "timestamp": e.timestamp}
        for e in entries
    ]


@router.get("/api/entries/{entry_id}", summary="Get Entry by ID (JSON)")
async def get_entry_api(entry_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"id": entry.id, "content": entry.content, "emotion": entry.emotion, "timestamp": entry.timestamp}


@router.post("/api/entries", summary="Create Entry (JSON)")
async def create_entry_api(content: str, emotion: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    new_entry = Diary(user_id=current_user["user_id"], content=content, emotion=emotion, timestamp=datetime.now())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return {"message": "Entry created", "id": new_entry.id}


@router.put("/api/entries/{entry_id}", summary="Update Entry (JSON)")
async def update_entry_api(entry_id: int, content: str, emotion: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry.content = content
    entry.emotion = emotion
    db.commit()
    return {"message": "Entry updated"}


@router.delete("/api/entries/{entry_id}", summary="Delete Entry (JSON)")
async def delete_entry_api(entry_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = db.query(Diary).filter_by(id=entry_id, user_id=current_user["user_id"]).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted"}
