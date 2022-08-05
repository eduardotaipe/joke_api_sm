from sqlalchemy import func

from app.db.session import SessionLocal as db
from app.models import Joke


def get_random_joke():
    joke = db().query(Joke).order_by(func.random()).first()
    return joke.id
