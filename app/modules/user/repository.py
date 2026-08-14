from sqlalchemy.orm import Session
from app.modules.user.models import User


# 创建会话工厂
# db = SessionLocal()
def get_user_by_username(db:Session,username:str):
    '''
    根据用户名获取用户
    :param db:
    :param username:
    :return:
    '''
    return db.query(User).filter(User.username == username).first()
def create_user(db:Session, user:User):
    '''
    创建用户
    :param db:
    :param user:
    :return:
    '''
    db.add(user)
    db.commit()

def get_refresh(db:Session,db_user):
    '''
    刷新用户信息
    :param db: 数据库会话
    :param db_user: 用户对象
    :return: None
    '''
    db.refresh(db_user)
    return db_user