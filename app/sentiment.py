import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ChromaDB client ve embedding modeli
chroma_client = chromadb.Client()
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=GOOGLE_API_KEY)

prompt_template = PromptTemplate.from_template("""
Aşağıda bir günlük yazısı var. Bu kişinin gün içindeki ruh halini değerlendir.  
Lütfen tek kelimelik bir **duygu etiketi** üret (örnek: 'mutlu', 'endişeli', 'yalnız').  
Ardından küçük ve empatik bir **yorum** yaz.  
Son olarak, kullanıcının uygulayabileceği somut **3 öneri** üret.

Günlük:
\"\"\"{journal_text}\"\"\"

Yanıt formatı şu şekilde olmalı:
Duygu: ...
Yorum: ...
Öneriler:
- ...
- ...
- ...
""")

emotion_chain = prompt_template | llm


import re

def analyze_sentiment(text: str):
    result = emotion_chain.invoke({"journal_text": text})
    response_text = result.content if hasattr(result, "content") else str(result)

    print("LLM'den gelen ham yanıt:\n", response_text)

    sentiment = ""
    comment = ""
    suggestions_lines = []

    # Markdown kalınlıklarını temizle
    cleaned_text = re.sub(r"\*\*(.*?)\*\*", r"\1", response_text)

    lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
    collecting_suggestions = False

    for line in lines:
        if line.lower().startswith("duygu:"):
            sentiment = line.split(":", 1)[1].strip()
            collecting_suggestions = False
        elif line.lower().startswith("yorum:"):
            comment = line.split(":", 1)[1].strip()
            collecting_suggestions = False
        elif line.lower().startswith("öneriler:"):
            collecting_suggestions = True
        elif collecting_suggestions:
            if re.match(r"^[\-–•]", line):  # öneri satırı mı?
                suggestions_lines.append(line.lstrip("-–• ").strip())
            else:
                # başlık değil ama madde de değil, boş bırak
                continue

    if not sentiment:
        sentiment = "Bilinmiyor"
    if not comment:
        comment = "Analiz yapılamadı."
    suggestions = "\n".join(suggestions_lines).strip() if suggestions_lines else ""

    return sentiment, 0.0, comment, suggestions



if __name__ == "__main__":
    test_text = "Bugün biraz yalnız hissettim ama sonunda rahatladım."
    sentiment, score, comment, suggestions = analyze_sentiment(test_text)
    print(f"Duygu: {sentiment}\nYorum: {comment}\nÖneriler: {suggestions}")