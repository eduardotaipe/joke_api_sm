import httpx

from sqlalchemy import func
from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.models import Joke
from app.schemas import JokeCreate
from app.schemas import JokeUpdate
from app.schemas import Joke as JokeResponse
from app.schemas.joke import JokeApi as JokeApiResponse


class JokeService:
    def __init__(self):
        self.model: Joke = Joke
        self.joke_apis = {
            "chuck": ("https://api.chucknorris.io/jokes/random", "value"),
            "dad": ("https://icanhazdadjoke.com/", "joke"),
        }

    def get(self, db: Session) -> Joke:
        joke = db.query(self.model).order_by(func.random()).first()
        if joke is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JokeResponse(text=joke.text)

    def get_by_api(self, name: str):
        joke_values = self.joke_apis.get(name.lower())

        if joke_values is None:
            raise HTTPException(
                status_code=404,
                detail=f"Joke API type {name} not found.",
            )

        joke_api, joke_field = joke_values
        response = httpx.get(joke_api, headers={"Accept": "application/json"})
        json_response = response.json()
        return JokeApiResponse(
            api=joke_api,
            text=json_response[joke_field],
        )

    def get_by_id(self, db: Session, id: int):
        joke: Joke = db.query(self.model).get(id)
        if joke is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return joke

    def create(self, db: Session, obj: JokeCreate):
        db_obj = Joke(**obj.dict())
        db.add(db_obj)
        db.commit()
        return JokeResponse(text=db_obj.text)

    def update(self, db: Session, id: int, obj: JokeUpdate):
        joke_db = self.get_by_id(db=db, id=id)

        updated_data = obj.dict()
        for field, value in updated_data.items():
            setattr(joke_db, field, value)
        db.add(joke_db)
        db.commit()
        return JokeResponse(text=joke_db.text)

    def remove(self, db: Session, id: int):
        joke_db = self.get_by_id(db=db, id=id)
        db.delete(joke_db)
        db.commit()
        return JokeResponse(text=joke_db.text)


joke_service: JokeService = JokeService()
