from pydantic import BaseModel
from datetime import datetime
import uuid

class CategoryCreate(BaseModel):
    name: str
    slug: str
    description: str = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
