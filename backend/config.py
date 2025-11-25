from pathlib import Path
import os

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]

# Load base .env, then overlay environment-specific file when present.
BASE_ENV_PATH = ROOT_DIR / ".env"
load_dotenv(BASE_ENV_PATH)
APP_ENV = os.getenv("APP_ENV", "development")
ENV_SPECIFIC = ROOT_DIR / f".env.{APP_ENV}"
if ENV_SPECIFIC.exists():
    load_dotenv(ENV_SPECIFIC, override=True)

# Fail fast if required vars are missing to avoid accidental defaults in production.
REQUIRED_VARS = [
    "MONGO_URI",
    "MONGO_DB",
    "MONGO_COLLECTION",
    "CHROMA_DIR",
    "CHROMA_COLLECTION",
]
missing = [key for key in REQUIRED_VARS if not os.getenv(key)]
if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")

# Mongo
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Chroma
CHROMA_DIR = os.getenv("CHROMA_DIR")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION")

# Optional Gemini (test only)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "text-embedding-004")
