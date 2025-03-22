from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"  # Change for PostgreSQL/MySQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
