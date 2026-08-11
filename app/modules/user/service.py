# 导入SQLAlchemy模型
from sqlalchemy.orm import Session
from app.modules.user.schemas import UserBase,UserOut
from app.schemas.response import ResponseModel
from app.utils.md5tool import get_md5
from app.modules.user.repository import get_user_by_username,create_user,get_refresh
from app.core.logger_config import logger
from app.modules.user import User

def register_user(db: Session, user:UserBase):
    """
    注册账号Service
    :param db: 数据库会话
    :param user: 用户信息
    :return: 注册结果
    """
    db_user = User(
        username=user.username,
        password=get_md5(user.password),
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
    # db.add(db_user)
    create_user(db,db_user)
    get_refresh(db,db_user)
    # db.commit()
    # db.refresh(db_user)
    user_out = UserOut.model_validate(db_user)
    res = ResponseModel(
        data=user_out
    )
    logger.info(f'创建成功: {res}')
    return res


if __name__ == '__main__':
    register_user(UserBase(username="fhc51aa1", password="123", email="tes@qq.cd"))
