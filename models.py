from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    diaries = relationship("Diary", back_populates="user")
    user_badges = relationship("UserBadge", back_populates="user")


class Diary(Base):
    __tablename__ = "diary"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    emotion = Column(String, nullable=True)  # örnek: 'mutlu', 'endişeli'

    comment = Column(String)         # yorum
    suggestions = Column(String)     # öneriler

    user = relationship("User", back_populates="diaries")

# 🔹 Tüm rozetlerin listesi (statik bilgiler)
class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)   # Örn: "İlk Günlük"
    description = Column(String)         # Örn: "İlk günlük kaydını ekledin!"
    icon = Column(String)                 # Örn: "🥉" veya bir ikon dosya adı
    condition_type = Column(String)       # Örn: "first_entry", "streak_7", "total_30"

    user_badges = relationship("UserBadge", back_populates="badge")


# 🔹 Kullanıcının kazandığı rozetler
class UserBadge(Base):
    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    badge_id = Column(Integer, ForeignKey("badges.id"))
    earned_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_badges")
    badge = relationship("Badge", back_populates="user_badges")

