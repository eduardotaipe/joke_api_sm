from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text

from app.db.base import Base


class Joke(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    text = Column(Text)
