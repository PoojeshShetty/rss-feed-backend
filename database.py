import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Placeholder for database URL loaded from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__':
    # Example usage (for demonstration, not part of the module's core logic)
    # You would typically import this in your main app or routes
    print(f"DATABASE_URL: {DATABASE_URL}")
    # db = next(get_db())
    # print("Database session created.")
    # db.close()
    # print("Database session closed.")
    pass