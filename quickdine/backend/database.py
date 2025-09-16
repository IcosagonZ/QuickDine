
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ SQLite database (saved in project folder as project.db)
DATABASE_URL = "sqlite:///./project.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # required for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
