from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class UserSubscriptionCreate(BaseModel):
    feed_id: uuid.UUID

    class Config:
        orm_mode = True

class UserUnSubscribe(BaseModel):
    feed_id: uuid.UUID

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: uuid.UUID
    firebase_uid: str
    email: str
    display_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class FeedResponse(BaseModel):
    id: uuid.UUID
    feed_url: str
    title: str
    description: Optional[str] = None
    link: str
    image_url: Optional[str] = None
    last_fetched_at: Optional[datetime] = None
    last_fetched_status: Optional[str] = None
    error_details: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserSubscriptionResponse(BaseModel):
    user_id: uuid.UUID
    feed_id: uuid.UUID
    subscribed_at: datetime
    is_active: bool
    user: UserResponse
    feed: FeedResponse

    class Config:
        orm_mode = True
