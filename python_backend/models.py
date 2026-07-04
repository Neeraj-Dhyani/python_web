from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean, DateTime;
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    complete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)