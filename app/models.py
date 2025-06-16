from sqlalchemy import (
    Column, String, Text, Boolean, ForeignKey, DateTime, func, UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    firebase_uid = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    display_name = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    subscriptions = relationship("UserSubscription", back_populates="user")
    bookmarks = relationship("UserBookmark", back_populates="user")


class RSSFeed(Base):
    __tablename__ = "rss_feeds"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    feed_url = Column(Text, unique=True, nullable=False)
    title = Column(String(511), nullable=False)
    description = Column(Text)
    link = Column(Text)
    image_url = Column(Text)
    last_fetched_at = Column(DateTime(timezone=True))
    last_fetched_status = Column(String(50))
    error_details = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    posts = relationship("BlogPost", back_populates="feed")
    categories = relationship("FeedCategory", back_populates="feed")


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    feed_id = Column(UUID(as_uuid=True), ForeignKey("rss_feeds.id"), primary_key=True)
    subscribed_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="subscriptions")
    feed = relationship("RSSFeed", back_populates="subscriptions")


class UserBookmark(Base):
    __tablename__ = "user_bookmarks"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    feed_id = Column(UUID(as_uuid=True), ForeignKey("rss_feeds.id"), primary_key=True)
    bookmarked_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="bookmarks")
    feed = relationship("RSSFeed", back_populates="bookmarks")


class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    feed_id = Column(UUID(as_uuid=True), ForeignKey("rss_feeds.id"), nullable=False)
    guid = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    link = Column(Text, nullable=False)
    published_at = Column(DateTime(timezone=True), nullable=False)
    author = Column(String(255))
    content_html = Column(Text, nullable=False)
    summary = Column(Text)
    image_url = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    feed = relationship("RSSFeed", back_populates="posts")


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    name = Column(String(255), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)

    feeds = relationship("FeedCategory", back_populates="category")


class FeedCategory(Base):
    __tablename__ = "feed_categories"

    feed_id = Column(UUID(as_uuid=True), ForeignKey("rss_feeds.id"), primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), primary_key=True)

    feed = relationship("RSSFeed", back_populates="categories")
    category = relationship("Category", back_populates="feeds")
