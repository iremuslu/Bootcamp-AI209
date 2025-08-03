from datetime import datetime, timedelta, timezone
from models import User, Diary, Badge, UserBadge
from sqlalchemy.orm import Session

TURKEY_TZ = timezone(timedelta(hours=3))

def check_and_award_badges(user_id: int, db: Session):
    total_entries = db.query(Diary).filter(Diary.user_id == user_id).count()

    # 📌 1. İlk Günlük Rozeti
    if total_entries >= 1:
        give_badge(user_id, "İlk Günlük", db)

    # 📌 2. 7 Günlük Seri Rozeti
    today = datetime.now(TURKEY_TZ).date()
    entries_last_7_days = db.query(Diary).filter(
        Diary.user_id == user_id,
        Diary.timestamp >= today - timedelta(days=6)
    ).all()
    unique_days = set(e.timestamp.date() for e in entries_last_7_days)
    if len(unique_days) >= 7:
        give_badge(user_id, "7 Günlük Seri", db)

    # 📌 3. Toplam 30 Günlük Rozeti
    if total_entries >= 30:
        give_badge(user_id, "30 Günlük", db)


def give_badge(user_id: int, badge_name: str, db: Session):
    badge = db.query(Badge).filter(Badge.name == badge_name).first()
    if not badge:
        return  # Badge tanımlı değilse atla

    # Daha önce alınmış mı kontrol et
    existing = db.query(UserBadge).filter(
        UserBadge.user_id == user_id,
        UserBadge.badge_id == badge.id
    ).first()
    if existing:
        return

    new_user_badge = UserBadge(user_id=user_id, badge_id=badge.id, earned_at=datetime.utcnow())
    db.add(new_user_badge)
    db.commit()
