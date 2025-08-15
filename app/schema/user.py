from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class UserCreate(BaseModel):
    firebase_uid: str
    email: str
    display_name: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: uuid.UUID
    firebase_uid: str
    email: str
    display_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
