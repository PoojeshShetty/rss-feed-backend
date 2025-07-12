from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.categories import Category
from app.schema.category import CategoryCreate

router = APIRouter()

@router.post("/categories/", response_model=CategoryCreate)
def create_category(category: CategoryCreate):
    """
    Create a new category in the database.
    """
    db = SessionLocal()
    db_category = Category(
        name=category.name,
        slug=category.slug,
        description=category.description
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    db.close()
    return db_category
