from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ihebgoodboy1999*@lab-postgres.cp5nuzvurixr.us-east-1.rds.amazonaws.com:5432/postgres""

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

