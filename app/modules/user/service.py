# 导入SQLAlchemy模型
from sqlalchemy.orm import Session
from app.modules.user.schemas import UserBase,UserOut
from app.schemas.response import ResponseModel,ResponseError
# Argon2id加密
from app.utils.argon2id_tool import hash_password, verify_password
from app.modules.user.repository import get_user_by_username,create_user,get_refresh
from app.core.logger_config import logger
from app.modules.user import User
from app.utils.pyjwt_tool import generate_token

def register_user(db: Session, user:UserBase):
    """
    注册账号Service
    :param db: 数据库会话
    :param user: 用户信息
    :return: 注册结果
    """
    db_user = User(
        username=user.username,
        password=hash_password(user.password),
        email=user.email,
        phone=user.phone,
        sex=user.sex,
        nickname=user.nickname
    )
    # 查询当前用户名是否被注册
    select_user = get_user_by_username(db,user.username)
    if select_user:
        res = ResponseModel(
            code=400,
            message=f"Username {select_user.username} has been registered"
        )
        logger.error(f'注册失败: {res}')
        return res
    # 添加用户
    create_user(db,db_user)
    get_refresh(db,db_user)
    user_out = UserOut.model_validate(db_user)
    res = ResponseModel(
        data=user_out
    )
    logger.info(f'创建成功: {res}')
    return res

def login_user(db: Session, username: str, password: str):
    """
    登录账号Service
    :param db: 数据库会话
    :param username: 用户名
    :param password: 密码
    :return: 登录结果
    """
    db_user = get_user_by_username(db, username)
    if db_user is not None:
        if verify_password(db_user.password, password):
            print(f'id=={db_user.id}')
            # 生成令牌
            token = generate_token({"user_id": db_user.id})
            return ResponseModel(data={
                "access_token": token,
                "token_type": "bearer",
                "user_info": db_user})
        else:
            return ResponseError(message="Password is incorrect")
    else:
        return ResponseError(message="User not found")

def logout_user(db: Session, user_id: int):
    """
    登出账号Service
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 登出结果
    """
    pass

if __name__ == '__main__':
    register_user(UserBase(username="fhc51aa1", password="123", email="tes@qq.cd"))
