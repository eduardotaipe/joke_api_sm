import re

from typing import Generator, List, Optional

from fastapi import HTTPException, Query

from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_query_as_numbers_list(numbers: str = Query(None)) -> Optional[List[int]]:
    if numbers is None:
        return None

    regex = re.compile("^\d+(,\d+)?$")
    regex_result = re.search(regex, numbers)

    if regex_result is None:
        raise HTTPException(
            status_code=404, detail="Parameter must be a comma separated integers"
        )

    numbers_list = [int(value) for value in numbers.split(",")]
    return numbers_list
