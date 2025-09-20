from sqlalchemy import Column, Integer, String

from demo_fast_api.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), unique=True)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(String(250))
    user_id = Column(Integer)