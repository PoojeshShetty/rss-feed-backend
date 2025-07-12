from fastapi import APIRouter
from app.models.users import User
from app.database import SessionLocal
from app.schema.user import UserCreate

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate):
    """
    Create a new user in the database.
    """
    db = SessionLocal()
    db_user = User(
        firebase_uid=user.firebase_uid,
        email=user.email,
        display_name=user.display_name,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
