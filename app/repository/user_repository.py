from sqlalchemy.orm import Session
from app.models.user import User
from app.db.database import SessionLocal
from app.schemas.user_schemas import UserBase


# 创建会话工厂
db = SessionLocal()
def get_user_by_username(username:str):
    '''
    根据用户名获取用户
    :param username:
    :return:
    '''
    return db.query(User).filter(User.username == username).first()
def create_user(user:User):
    db_user = db.add(user)
    db.commit()
    return db_user

def get_refresh(db_user):
    return db.refresh(db_user)