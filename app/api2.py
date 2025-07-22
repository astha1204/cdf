
from fastapi import APIRouter
from app.models import DataModel
from app.db import collection
from bson import ObjectId

router = APIRouter()

@router.post("/upload")
def upload_data(data: DataModel):
    doc = data.dict()
    doc["_id"] = ObjectId()  # Optional
    result = collection.insert_one(doc)
    return { "status": "success", "inserted_id": str(result.inserted_id) }

@router.get("/all")
def get_all():
    return [
        {**{k: (str(v) if k == '_id' else v) for k, v in doc.items()}}
        for doc in collection.find()
    ]
