from sqlalchemy.orm import Session
from app.models.user import User
from app.db.database import SessionLocal
from app.schemas.user_schemas import UserBase


# 创建会话工厂
# db = SessionLocal()
def get_user_by_username(db:Session,username:str):
    '''

    :param db:
    :param username:
    :return:
    '''
    return db.query(User).filter(User.username == username).first()
def create_user(db:Session, user:User):
    db.add(user)
    db.commit()

def get_refresh(db:Session,db_user):
    return db.refresh(db_user)