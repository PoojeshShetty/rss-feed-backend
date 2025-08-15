from pydantic import BaseModel
from datetime import datetime
import uuid
from app.schema.rss_feed import RSSFeedCreate

class BlogPostCreate(BaseModel):
    feed_id: uuid.UUID
    guid: str
    title: str
    link: str
    published_at: datetime
    author: str = None
    content_html: str
    summary: str = None
    image_url: str = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True

class BlogPostWithFeed(BlogPostCreate):
    feed: RSSFeedCreate

    class Config:
        orm_mode = True
