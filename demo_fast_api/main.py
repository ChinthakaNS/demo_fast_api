from typing import Annotated

from fastapi import FastAPI, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from demo_fast_api.db.connection import get_db
from demo_fast_api.db.models import User
from demo_fast_api.pydantic.user import UserRequest

app = FastAPI()

db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/", status_code=status.HTTP_200_OK)
@app.post("/healthcheck", status_code=status.HTTP_200_OK)
@app.get("/", status_code=status.HTTP_200_OK)
@app.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck():
    return {"message": "Hello World"}


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
