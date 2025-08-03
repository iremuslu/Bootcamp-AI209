from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import auth, dashboard, pages,entries,emotions,journal,profile
from models import Base
from database import engine

app = FastAPI(title="MindMirrorAI", version="1.0.0")

# Statik dosyalar
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Router'ları dahil et
app.include_router(pages.router)  # Ana sayfa için
app.include_router(auth.router)  # Login/register
app.include_router(dashboard.router)  # Dashboard ve profil
app.include_router(emotions.router)      # duygu durumları
app.include_router(journal.router)      # günlük
app.include_router(entries.router)      # Günlük girişleri (edit vb.)
app.include_router(profile.router)      # Günlük girişleri (edit vb.)

# 🔹 Tabloları oluştur
Base.metadata.create_all(bind=engine)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "EmoteryAI is running!"}