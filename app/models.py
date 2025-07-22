from pydantic import BaseModel, Field
from typing import Dict, Any
from datetime import datetime

class ContentModel(BaseModel):
    normalized: Dict[str, Any]
    raw: str
    enriched: Dict[str, Any]

class DataModel(BaseModel):
    source_type: str
    sub_source: str
    file_type: str
    ingested_at: datetime
    metadata: Dict[str, Any]
    content: ContentModel
