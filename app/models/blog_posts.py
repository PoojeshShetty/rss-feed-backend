from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    feed_id = Column(UUID(as_uuid=True), nullable=False)
    guid = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    link = Column(Text, nullable=False)
    published_at = Column(TIMESTAMP, nullable=False)
    author = Column(String(255))
    content_html = Column(Text, nullable=False)
    summary = Column(Text)
    image_url = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default='NOW()')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='NOW()')
