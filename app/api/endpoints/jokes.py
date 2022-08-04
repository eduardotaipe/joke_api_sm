from typing import Any
from fastapi import Depends
from fastapi.routing import APIRouter

from app.service import joke_service
from app.schemas import JokeCreate, JokeUpdate, Joke, JokeApi

from app.api.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=Joke)
def get_random_joke(db: Session = Depends(get_db)) -> Any:
    joke = joke_service.get(db=db)
    return joke


@router.get("/{name_api}", response_model=JokeApi)
def get_api_joke(name_api: str) -> Any:
    joke = joke_service.get_by_api(name_api)
    return joke


@router.post("/", response_model=Joke)
def create_joke(
    *,
    db: Session = Depends(get_db),
    joke_in: JokeCreate,
) -> Any:
    joke = joke_service.create(db=db, obj=joke_in)
    return joke


@router.put("/{id}", response_model=Joke)
def update_joke(
    *,
    db: Session = Depends(get_db),
    id: int,
    joke_in: JokeUpdate,
) -> Any:
    joke = joke_service.update(db=db, id=id, obj=joke_in)
    return joke


@router.delete("/{id}", response_model=Joke)
def delete_joke(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    joke = joke_service.remove(db=db, id=id)
    return joke
