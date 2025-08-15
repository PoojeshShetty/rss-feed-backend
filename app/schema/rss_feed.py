from pydantic import BaseModel
from datetime import datetime
import uuid

class RSSFeedCreate(BaseModel):
    feed_url: str
    title: str
    description: str = None
    link: str
    image_url: str = None
    last_fetched_at: datetime = None
    last_fetched_status: str = None
    error_details: str = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
