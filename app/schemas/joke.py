from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JokeBase(BaseModel):
    text: Optional[str] = None


class JokeCreate(JokeBase):
    text: str


class JokeUpdate(JokeBase):
    text: str


class JokeApi(JokeBase):
    api: str
    text: str


class JokeInDBBase(JokeBase):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Joke(JokeInDBBase):
    pass
