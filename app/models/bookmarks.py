from sqlalchemy import Column, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Bookmark(Base):
    __tablename__ = "bookmarks"

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True, default=uuid.uuid4)
    blog_post_id = Column(UUID(as_uuid=True), ForeignKey('blog_posts.id'), primary_key=True, default=uuid.uuid4)
    bookmarked_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default='NOW()')

    user = relationship("User", back_populates="bookmarks")
    blog_post = relationship("BlogPost")
