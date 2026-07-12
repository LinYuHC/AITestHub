# 导入SQLAlchemy模型
from fastapi import HTTPException

from app.models import *
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, SessionLocal
from app.schemas.user_schemas import *


def register_user(user:UserBase):
    '''
    注册账号Service
    :return:
    '''
    db_user = Users(
        username=user.username,
        password=user.password,
        email=user.email,
        phone=user.phone,
        sex=user.sex,
        nickname=user.nickname
    )
    # 创建会话工厂对象
    db = SessionLocal()
    # 查询当前用户名是否被注册
    select_user = db.query(Users).filter(Users.username==user.username).first()
    if select_user:
        print(f'用户名：{select_user.username} 已被注册')
        raise HTTPException(status_code=400, detail=f"用户名 {user.username} 已被注册")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print('创建成功')
    return db_user



if __name__ == '__main__':
    register_user(UserBase(username="fhc3", password="123", email="tes@qq.cd"))
