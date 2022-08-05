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


class Joke(JokeBase):
    text: str
