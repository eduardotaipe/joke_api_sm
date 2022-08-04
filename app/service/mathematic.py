from math import gcd
from typing import List

from fastapi import HTTPException

from app.schemas.mathematic import MathLcm, MathPlusOne


class MathService:
    def get_lcm(self, numbers: List[int]) -> MathLcm:
        if numbers is None:
            raise HTTPException(
                status_code=404, detail="Parameter must be a comma separated integers"
            )
        lcm = 1
        for number in numbers:
            lcm = lcm * number // gcd(lcm, number)
        return MathLcm(result=lcm)

    def get_number_plus_one(self, number: int) -> MathPlusOne:
        if number is None:
            raise HTTPException(
                status_code=404, detail="Parameter must be a integers value"
            )
        number_plus_one = number + 1
        return MathPlusOne(result=number_plus_one)


math_service: MathService = MathService()
