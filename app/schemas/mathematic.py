from typing import Optional

from pydantic import BaseModel


class MathBase(BaseModel):
    result: Optional[int] = None


class MathLcm(MathBase):
    result: int


class MathPlusOne(MathBase):
    result: int
