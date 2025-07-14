from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.rss_feeds import RSSFeed
from app.schema.rss_feed import RSSFeedCreate

router = APIRouter()

@router.post("/rss_feeds/", response_model=RSSFeedCreate)
def create_rss_feed(rss_feed: RSSFeedCreate):
    """
    Create a new RSS feed in the database.
    """
    db = SessionLocal()
    db_rss_feed = RSSFeed(
        feed_url=rss_feed.feed_url,
        title=rss_feed.title,
        description=rss_feed.description,
        link=rss_feed.link,
        image_url=rss_feed.image_url,
        last_fetched_at=rss_feed.last_fetched_at,
        last_fetched_status=rss_feed.last_fetched_status,
        error_details=rss_feed.error_details
    )
    db.add(db_rss_feed)
    db.commit()
    db.refresh(db_rss_feed)
    db.close()
    return db_rss_feed
