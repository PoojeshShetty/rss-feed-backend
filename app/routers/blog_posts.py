from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from app.database import SessionLocal
from app.models.blog_posts import BlogPost
from app.models.bookmarks import Bookmark
from app.models.user_subscriptions import UserSubscription
from app.schema.blog_post import BlogPostCreate, BlogPostWithFeed

router = APIRouter()

MOCK_USERID = "3f2a190b-0155-4b73-9f56-d05098567d19"

@router.post("/blog_posts/", response_model=BlogPostCreate)
def create_blog_post(blog_post: BlogPostCreate):
    """
    Create a new blog post in the database.
    """
    db = SessionLocal()
    db_blog_post = BlogPost(
        feed_id=blog_post.feed_id,
        guid=blog_post.guid,
        title=blog_post.title,
        link=blog_post.link,
        published_at=blog_post.published_at,
        author=blog_post.author,
        content_html=blog_post.content_html,
        summary=blog_post.summary,
        image_url=blog_post.image_url
    )
    db.add(db_blog_post)
    db.commit()
    db.refresh(db_blog_post)
    db.close()
    return db_blog_post

@router.get("/blog_posts/", response_model=list[BlogPostWithFeed])
def get_blog_posts():
    """
    Get all blog posts with related feed information.
    """
    db = SessionLocal()
    blog_posts = db.query(BlogPost).options(joinedload(BlogPost.feed)).all()
    db.close()
    return blog_posts

@router.get("/blog_posts/bookmarked", response_model=list[BlogPostWithFeed])
def get_bookmarked_blog_posts():
    """
    Get all blog posts that are bookmarked by the user.
    """
    db = SessionLocal()
    try:
        bookmarked_blog_posts = (
            db.query(BlogPost)
            .join(Bookmark, BlogPost.id == Bookmark.blog_post_id)
            .filter(Bookmark.user_id == MOCK_USERID)
            .options(joinedload(BlogPost.feed))
            .all()
        )
        return bookmarked_blog_posts
    finally:
        db.close()

@router.get("/blog_posts/subscribed", response_model=list[BlogPostWithFeed])
def get_subscribed_blog_posts():
    """
    Get all blog posts for the feeds the user is subscribed to.
    """
    db = SessionLocal()
    try:
        subscribed_blog_posts = (
            db.query(BlogPost)
            .join(UserSubscription, BlogPost.feed_id == UserSubscription.feed_id)
            .filter(UserSubscription.user_id == MOCK_USERID)
            .filter(UserSubscription.is_active == True)  # Added filter for active subscriptions
            .options(joinedload(BlogPost.feed))
            .all()
        )
        return subscribed_blog_posts
    finally:
        db.close()
