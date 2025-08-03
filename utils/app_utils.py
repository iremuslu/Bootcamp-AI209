import json
import os
from datetime import datetime

DATA_PATH = "data/diary.json"

def save_entry(text, emotion, comment, suggestions):
    # Kayıt yapılacak veri
    entry = {
        "timestamp": datetime.now().isoformat(),
        "text": text,
        "emotion": emotion,
        "comment": comment,
        "suggestions": suggestions
    }

    # Eski verileri al
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    # Yeni veri ile güncelle
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)