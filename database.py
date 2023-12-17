from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
# engine_profiles = create_engine(SQLALCHEMY_DATABASE_URL_profiles, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal_profiles = sessionmaker(autocommit=False, autoflush=False, bind=engine_profiles)


Base = declarative_base()