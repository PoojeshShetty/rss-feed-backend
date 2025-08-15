from pydantic import BaseModel
from datetime import datetime
import uuid

class CategoryGet(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    description: str = None

    class Config:
        orm_mode = True

class CategoryCreate(CategoryGet):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True

