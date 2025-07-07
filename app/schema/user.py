from pydantic import BaseModel
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    firebase_uid: str
    email: str
    display_name: str = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
