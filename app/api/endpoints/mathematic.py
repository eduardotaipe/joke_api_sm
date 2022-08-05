from typing import Any, List

from fastapi import Depends, Query
from fastapi.routing import APIRouter

from app.api.deps import get_query_as_numbers_list
from app.schemas import MathLcm, MathPlusOne
from app.service import math_service


router = APIRouter(prefix="/math")


@router.get("/lcm", response_model=MathLcm)
def lowest_common_multiple(
    numbers: List[int] = Depends(get_query_as_numbers_list),
) -> Any:
    lcm = math_service.get_lcm(numbers)
    return lcm


@router.get("/plus_one", response_model=MathPlusOne)
def number_plus_one(number: int = Query(None)):
    plus_one = math_service.get_number_plus_one(number)
    return plus_one
