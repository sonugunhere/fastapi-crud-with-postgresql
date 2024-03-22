from datetime import timedelta
from app.auth.schemas import UserCreate, UserUpdate
from app.auth.services import UserService
from database import get_db
from starlette.config import Config
from sqlalchemy.orm import Session

from fastapi import APIRouter, Response, Depends, Request


config = Config(".env")
ACCESS_TOKEN_EXPIRES_IN = config("ACCESS_TOKEN_EXPIRES_IN")


router = APIRouter(
    prefix="/auth",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


# add user
@router.post('/user-create/')
async def user_registration(
    payload: UserCreate, 
    request: Request,
    db: Session = Depends(get_db),
    response: Response = None
    ):
    
    user_sign_up_service = UserService(request, response, db)
    return await user_sign_up_service.create_user(payload)

@router.get('/user-detail/{id}')
async def get_detail_user(
    id:int,
    request: Request,
    db: Session = Depends(get_db),
    response: Response = None
    ):
    user_sign_up_service = UserService(request, response, db)
    return await user_sign_up_service.user_details(id)
    


# user by id
@router.get('/user-list')
async def get_user_list(
    request: Request,
    db: Session = Depends(get_db),
    response: Response = None
    ):
    user_sign_up_service = UserService(request, response, db)
    return await user_sign_up_service.all_user()
    


@router.put('/user-update/{id}')
async def user_update(
    id: int, 
    payload: UserUpdate,
    request: Request,
    db: Session = Depends(get_db),
    response: Response = None
    ):
    user_sign_up_service = UserService(request, response, db)
    return await user_sign_up_service.update_user(id, payload)


# delete user
@router.delete('/user-delete/{id}')
async def user_delete(
    id:int,
    request: Request,
    db: Session = Depends(get_db),
    response: Response = None):
    user_sign_up_service = UserService(request, response, db)
    return await user_sign_up_service.delete_user(id)