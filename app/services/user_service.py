# 导入SQLAlchemy模型
from fastapi import HTTPException

from app.models import *
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, SessionLocal
from app.schemas.user_schemas import *
from app.schemas.response import *
from app.utils.md5tool import get_md5
from app.repository.user_repository import *


def register_user(user:UserBase):
    '''
    注册账号Service
    :return:
    '''
    db_user = User(
        username=user.username,
        password=get_md5(user.password),
        email=user.email,
        phone=user.phone,
        sex=user.sex,
        nickname=user.nickname
    )
    # 创建会话工厂对象
    # db = SessionLocal()
    # 查询当前用户名是否被注册
    # select_user = db.query(User).filter(User.username==user.username).first()
    select_user = get_user_by_username(user.username)
    if select_user:
        print(f'Username {select_user.username} has been registered')
        return ResponseModel(code=400, message=f"Username {select_user.username} has been registered")
    # 添加用户
    # db.add(db_user)
    create_user(db_user)
    get_refresh(db_user)
    # db.commit()
    # db.refresh(db_user)
    print('创建成功')
    user_out = UserOut.model_validate(db_user)
    return ResponseModel(data=user_out)


if __name__ == '__main__':
    register_user(UserBase(username="fhc51", password="123", email="tes@qq.cd"))
