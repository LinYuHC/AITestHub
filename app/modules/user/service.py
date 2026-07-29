# 导入SQLAlchemy模型
from app.modules.user.schemas import UserBase,UserOut
from app.schemas.response import ResponseModel
from app.utils.md5tool import get_md5
from app.modules.user.repository import get_user_by_username,create_user,get_refresh
from app.core.logger_config import logger
from app.modules.user import User
# 导入数据库配置
from app.db.database import SessionLocal

def register_user(user:UserBase):
    """
    注册账号Service
    :param user:
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
    # 创建会话工厂对象
    db = SessionLocal()
    # 查询当前用户名是否被注册
    # select_user = db.query(User).filter(User.username==user.username).first()
    select_user = get_user_by_username(db,user.username)
    if select_user:
        print(f'Username {select_user.username} has been registered')
        res = ResponseModel(code=400, message=f"Username {select_user.username} has been registered")
        logger.error(f'注册失败: {res}')
        return res
    # 添加用户
    # db.add(db_user)
    create_user(db,db_user)
    get_refresh(db,db_user)
    # db.commit()
    # db.refresh(db_user)
    print('创建成功')
    user_out = UserOut.model_validate(db_user)
    res = ResponseModel(data=user_out)
    logger.info(f'创建成功: {res}')
    return res


if __name__ == '__main__':
    register_user(UserBase(username="fhc51aa1", password="123", email="tes@qq.cd"))
