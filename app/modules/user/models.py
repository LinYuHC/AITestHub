"""
数据库模型模块
使用 SQLAlchemy ORM 定义数据库表结构
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

# 导入模型基类
from app.db.database import Base

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    #   id：主键，自增
    #   Integer：整数类型
    #   primary_key=True：设为主键
    #   index=True：创建索引，加快查询速度
    #   autoincrement=True：自动递增
    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    #   username：用户名
    #   String(50)：最大长度 20 的字符串
    #   unique=True：唯一约束，不能重复
    #   nullable=False：不允许为空
    username = Column(String(255), nullable=False, unique=True)
    # 密码
    password = Column(String(255), nullable=False)
    # 手机号
    phone = Column(String(255), nullable=True)
    # 邮箱
    email = Column(String(255), nullable=True)
    # 性别0未知1男2女
    sex = Column(Integer, nullable=True)
    # 昵称
    nickname = Column(String(255), nullable=True)

    # 自定义方法
    def __repr__(self):
        """打印对象时的显示格式"""
        return f"<User(id={self.id}, username={self.username}, phone={self.phone}, email={self.email})>"



