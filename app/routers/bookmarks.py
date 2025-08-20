from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import joinedload
from app.models.bookmarks import Bookmark
from app.models.blog_posts import BlogPost
from app.database import SessionLocal
from app.schema.bookmark import BookmarkCreate, BookmarkResponse
import uuid

router = APIRouter()

MOCK_USERID = "3f2a190b-0155-4b73-9f56-d05098567d19"

@router.post("/bookmarks/", response_model=BookmarkCreate)
def create_bookmark(bookmark: BookmarkCreate):
    """
    Create a new bookmark in the database.
    """
    db = SessionLocal()
    try:
        existing_bookmark = db.query(Bookmark).filter(
            Bookmark.user_id == MOCK_USERID,
            Bookmark.blog_post_id == bookmark.blog_post_id
        ).first()

        if existing_bookmark:
            raise HTTPException(status_code=400, detail="Bookmark already exists")
        else:
            db_bookmark = Bookmark(
                user_id=MOCK_USERID,  # TODO change user id to get from token
                blog_post_id=bookmark.blog_post_id
            )
            db.add(db_bookmark)
            db.commit()
            db.refresh(db_bookmark)
            return db_bookmark
    finally:
        db.close()

@router.get("/bookmarks/", response_model=list[BookmarkResponse])
def get_bookmarks():
    """
    Get all bookmarked blog posts from the database.
    """
    db = SessionLocal()
    try:
        bookmarks = db.query(Bookmark).options(joinedload(Bookmark.blog_post)).filter(Bookmark.user_id == MOCK_USERID).all()
        return bookmarks
    finally:
        db.close()
