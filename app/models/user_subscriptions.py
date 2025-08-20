from sqlalchemy import Column, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True, default=uuid.uuid4)
    feed_id = Column(UUID(as_uuid=True), ForeignKey('rss_feeds.id'), primary_key=True, default=uuid.uuid4)
    subscribed_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default='NOW()')
    is_active = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="subscriptions")
    feed = relationship("RSSFeed", back_populates="subscriptions")
