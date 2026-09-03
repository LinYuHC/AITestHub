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
def get_user_by_id(db:Session,user_id:int):
    '''
    根据用户ID获取用户
    :param user_id:
    :param db:
    :param id:
    :return:
    '''
    return db.query(User).filter(User.id == user_id).first()
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

def update_user(db:Session,user_id: int,user:dict):
    '''
    更新用户
    :param db: 数据库会话
    :param user_id: 用户ID
    :param user: 用户信息
    :return: None
    '''
    # 更新用户信息
    db.query(User).filter(User.id == user_id).update(user)
    # 提交
    db.commit()
    # 重新查询用户信息
    db_user_info = get_user_by_id(db,user_id)
    # 返回修改后的用户信息
    return db_user_info