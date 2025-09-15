from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

from src.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.SQL_ECHO)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


DatabaseSessionDepends = Annotated[Session, Depends(get_session)]
