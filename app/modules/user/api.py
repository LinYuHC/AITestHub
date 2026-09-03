from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.schemas.response import ResponseModel
from app.modules.user.schemas import UserBase, UserOut, UserLogin, EditUser, CurrentUser
from app.modules.user import service
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["用户"]
)
@router.post(
    "/register",
    response_model=ResponseModel[UserOut]
             )
def register_user(user:UserBase, db: Session = Depends(get_db)):
    return service.register_user(db, user)

@router.post(
    "/login",
    response_model=ResponseModel[UserLogin]
             )
def login_user(user:UserBase, db: Session = Depends(get_db)):
    return service.login_user(db, user.username, user.password)

@router.post("/edit")
def edit_user(user: EditUser,db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return service.edit_user(db, current_user.user_id,user)

@router.get(
    "/userinfo",
    response_model=ResponseModel[UserOut]
)
def get_user_info(db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    '''
    获取用户信息
    :param current_user:
    :param db:
    :param user_id:
    :return:
    '''
    return service.get_user_info(db, current_user.user_id)

@router.post(
    "/logout"
)
def logout_user(current_user: CurrentUser = Depends(get_current_user)):
    print(f'jti等于: {current_user.jti}')
    return service.logout_user(current_user.jti)

if __name__ == '__main__':
    import asyncio
    asyncio.run(login_user(UserBase(username="fhc", password="1234567890")))