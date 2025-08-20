from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import joinedload
from app.models.user_subscriptions import UserSubscription
from app.models.users import User
from app.models.rss_feeds import RSSFeed
from app.database import SessionLocal
from app.schema.user_subscription import UserSubscriptionCreate, UserSubscriptionResponse, UserUnSubscribe
import uuid

router = APIRouter()

MOCK_USERID = "3f2a190b-0155-4b73-9f56-d05098567d19"

@router.post("/user_subscriptions/", response_model=UserSubscriptionCreate)
def create_user_subscription(subscription: UserSubscriptionCreate):
    """
    Create a new user subscription in the database or reactivate an existing one.
    """
    db = SessionLocal()
    try:
        existing_subscription = db.query(UserSubscription).filter(
            UserSubscription.user_id == MOCK_USERID,
            UserSubscription.feed_id == subscription.feed_id
        ).first()

        if existing_subscription:
            if not existing_subscription.is_active:
                existing_subscription.is_active = True
                db.commit()
                db.refresh(existing_subscription)
                return existing_subscription
            else:
                raise HTTPException(status_code=400, detail="Subscription already active")
        else:
            db_subscription = UserSubscription(
                user_id=MOCK_USERID,  # TODO change user id to get from token
                feed_id=subscription.feed_id,
                is_active=True
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
        subscriptions = db.query(UserSubscription).options(joinedload(UserSubscription.user),joinedload(UserSubscription.feed)).filter(UserSubscription.is_active == True).all()
        return subscriptions
    finally:
        db.close()

@router.post("/user_subscription/unsubscribe/", response_model=UserSubscriptionResponse)
def unsubscribe_user_subscription(payload: UserUnSubscribe):
    """
    Unsubscribe a user from a feed.
    """
    db = SessionLocal()
    try:
        subscription = db.query(UserSubscription).options(joinedload(UserSubscription.user), joinedload(UserSubscription.feed)).filter(UserSubscription.user_id == MOCK_USERID, UserSubscription.feed_id == payload.feed_id).first()
        if not subscription:
            raise HTTPException(status_code=400, detail="User is not subscribed")
        subscription.is_active = False
        db.commit()
        db.refresh(subscription)
        return subscription
    finally:
        db.close()
