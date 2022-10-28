import os
from pickletools import int4
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi_pagination import Page, paginate, add_pagination

from app.schema.schemas import UserCreate, UserBase, UserUpdate
from app.model.models import User

from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# add user
@app.post('/user/', response_model=UserBase)
async def user(user: UserCreate):
    db_user = User(username=user.username, password=user.password, fullname=user.fullname, email = user.email, address = user.address)
    db.session.add(db_user)
    db.session.commit()
    return db_user

# get all user
@app.get('/user/')
async def user():
    user = db.session.query(User).all()
    return user


# delete user
@app.delete('/user/{id}')
async def user(id:int):
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()
    return {"user": "deleted"}

# user by id
@app.get('/user/{id}')
async def user(id:int):
    user = db.session.query(User).get(id)
    return user


@app.put('/user/{id}', response_model=UserUpdate)
async def user(id: int, user: UserBase):
    users = db.session.query(User).get(id)
    users.username=user.username
    users.password=user.password
    users.fullname=user.fullname
    users.email = user.email
    users.address = user.address
    db.session.add(users)
    db.session.commit()
    db.session.refresh(users)
    return users

