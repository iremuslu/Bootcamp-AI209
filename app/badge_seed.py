from database import SessionLocal
from models import Badge

def seed_badges():
    db = SessionLocal()

    badges = [
        {
            "name": "İlk Günlük",
            "description": "İlk günlüğünü eklediğinde kazanılır.",
            "icon": "🥇"
        },
        {
            "name": "7 Günlük Seri",
            "description": "Arka arkaya 7 gün günlük yazdığında kazanılır.",
            "icon": "🔥"
        },
        {
            "name": "30 Günlük",
            "description": "Toplam 30 günlük eklediğinde kazanılır.",
            "icon": "🏆"
        }
    ]

    for b in badges:
        existing = db.query(Badge).filter_by(name=b["name"]).first()
        if not existing:
            badge = Badge(name=b["name"], description=b["description"], icon=b["icon"])
            db.add(badge)

    db.commit()
    db.close()
    print("Rozetler başarıyla eklendi.")

if __name__ == "__main__":
    seed_badges()
