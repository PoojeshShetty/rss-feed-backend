from fastapi import APIRouter
from sqlalchemy.orm import joinedload
from app.database import SessionLocal
from app.models.rss_feeds import RSSFeed
from app.models.feed_categories import FeedCategory
from app.models.user_subscriptions import UserSubscription
from app.schema.rss_feed import RSSFeedCreate, RSSFeedGet

router = APIRouter()

MOCK_USERID = "3f2a190b-0155-4b73-9f56-d05098567d19"

@router.post("/rss_feeds/", response_model=RSSFeedGet)
def create_rss_feed(rss_feed: RSSFeedCreate):
    """
    Create a new RSS feed in the database.
    """
    db = SessionLocal()
    try:
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

        for category_id in rss_feed.category_ids:
            db_feed_category = FeedCategory(feed_id=db_rss_feed.id, category_id=category_id)
            db.add(db_feed_category)
        db.commit()

        return db_rss_feed
    finally:
        db.close()

@router.get("/rss_feeds/", response_model=list[RSSFeedGet])
def get_rss_feeds():
    """
    Get all RSS feeds from the database.
    """
    db = SessionLocal()
    try:
        rss_feeds = (
            db.query(RSSFeed)
            .options(joinedload(RSSFeed.categories))  # eager load categories
            .all()
        )
        return rss_feeds
    finally:
        db.close()

@router.get("/rss_feeds/subscribed", response_model=list[RSSFeedGet])
def get_subscribed_rss_feeds():
    """
    Get all RSS feeds that the user is subscribed to.
    """
    db = SessionLocal()
    try:
        subscribed_feeds = (
            db.query(RSSFeed)
            .join(UserSubscription, UserSubscription.feed_id == RSSFeed.id)
            .filter(UserSubscription.user_id == MOCK_USERID, UserSubscription.is_active == True)
            .options(joinedload(RSSFeed.categories))  # eager load categories
            .all()
        )
        return subscribed_feeds
    finally:
        db.close()
