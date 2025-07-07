from fastapi import APIRouter
from ..models.users import User
from ..database import SessionLocal
from ..schema.user import UserCreate

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate):
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
