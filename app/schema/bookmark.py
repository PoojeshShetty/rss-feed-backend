from pydantic import BaseModel
import uuid
from datetime import datetime

class BookmarkCreate(BaseModel):
    blog_post_id: uuid.UUID

    class Config:
        orm_mode = True

class BookmarkResponse(BaseModel):
    user_id: uuid.UUID
    blog_post_id: uuid.UUID
    bookmarked_at: datetime

    class Config:
        orm_mode = True
