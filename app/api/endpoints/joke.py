from typing import Any

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.responses import Response

from starlette.status import HTTP_201_CREATED
from starlette.status import HTTP_204_NO_CONTENT

from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas import Joke
from app.schemas import JokeApi
from app.schemas import JokeCreate
from app.schemas import JokeUpdate
from app.service import joke_service


router = APIRouter(prefix="/joke")


@router.get("/", response_model=Joke)
def random_joke(db: Session = Depends(get_db)) -> Any:
    joke = joke_service.get(db=db)
    return joke


@router.get("/{name_api}", response_model=JokeApi)
def api_joke(name_api: str) -> Any:
    joke = joke_service.get_by_api(name_api)
    return joke


@router.post("/", response_model=Joke, status_code=HTTP_201_CREATED)
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


@router.delete("/{id}", response_class=Response)
def delete_joke(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    joke_service.remove(db=db, id=id)
    return Response(status_code=HTTP_204_NO_CONTENT)
