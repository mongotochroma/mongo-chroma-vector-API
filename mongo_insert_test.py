from pymongo import MongoClient
from datetime import datetime
from backend.config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
coll = db[MONGO_COLLECTION]

coll.insert_one({
    "title": "Diabetic Retinopathy Detection",
    "body": "We use a custom CNN trained on ODIR-5K for DR classification.",
    "tags": ["DR", "CNN", "medical"],
    "created_at": datetime.utcnow()
})

print(
    f"Inserted test document into MongoDB {MONGO_DB}.{MONGO_COLLECTION} using {MONGO_URI}")

