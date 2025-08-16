from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.models.user_subscriptions import UserSubscription
from app.models.users import User
from app.models.rss_feeds import RSSFeed
from app.database import SessionLocal
from app.schema.user_subscription import UserSubscriptionCreate, UserSubscriptionResponse

router = APIRouter()

@router.post("/user_subscriptions/", response_model=UserSubscriptionCreate)
def create_user_subscription(subscription: UserSubscriptionCreate):
    """
    Create a new user subscription in the database.
    """
    db = SessionLocal()
    try:
        db_subscription = UserSubscription(
            user_id=subscription.user_id,
            feed_id=subscription.feed_id,
            subscribed_at=subscription.subscribed_at,
            is_active=subscription.is_active
        )
        db.add(db_subscription)
        db.commit()
        db.refresh(db_subscription)
        return db_subscription
    finally:
        db.close()

@router.get("/user_subscriptions/", response_model=list[UserSubscriptionResponse])
def get_user_subscriptions():
    """
    Get all user subscriptions from the database.
    """
    db = SessionLocal()
    try:
        subscriptions = db.query(UserSubscription).join(User, UserSubscription.user_id == User.id).join(RSSFeed, UserSubscription.feed_id == RSSFeed.id).all()
        return subscriptions
    finally:
        db.close()
