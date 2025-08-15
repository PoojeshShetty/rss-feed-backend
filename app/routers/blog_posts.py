from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from app.database import SessionLocal
from app.models.blog_posts import BlogPost
from app.schema.blog_post import BlogPostCreate, BlogPostWithFeed

router = APIRouter()

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
