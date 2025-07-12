from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class FeedCategory(Base):
    __tablename__ = "feed_categories"

    feed_id = Column(UUID(as_uuid=True), ForeignKey('rss_feeds.id'), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), primary_key=True, default=uuid.uuid4)

    # Define relationships if needed
    # feed = relationship("RssFeed", back_populates="feed_categories")
    # category = relationship("Category", back_populates="feed_categories")
