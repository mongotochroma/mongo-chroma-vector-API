from pathlib import Path
import os

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

# Mongo
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "realtime_demo")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "articles")

# Chroma
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_store")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "realtime_demo")

# Optional Gemini (test only)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "text-embedding-004")
