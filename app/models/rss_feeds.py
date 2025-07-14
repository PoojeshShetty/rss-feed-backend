from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class RSSFeed(Base):
    __tablename__ = "rss_feeds"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    feed_url = Column(Text, unique=True, nullable=False)
    title = Column(String(511), nullable=False)
    description = Column(Text)
    link = Column(Text)
    image_url = Column(Text)
    last_fetched_at = Column(TIMESTAMP)
    last_fetched_status = Column(String(50))
    error_details = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default='NOW()')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='NOW()')
