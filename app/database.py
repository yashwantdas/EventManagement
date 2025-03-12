import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Get MySQL DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Please check your .env file.")

print(f"✅ Using DATABASE_URL: {DATABASE_URL}")

# Create MySQL database engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL logs

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Initialize Database
def init_db():
    Base.metadata.create_all(bind=engine)
