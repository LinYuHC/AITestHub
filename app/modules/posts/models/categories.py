from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from app.db.database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 分类名称
    name = Column(String(255), nullable=False)
    # 分类描述
    description = Column(String(200), nullable=True)
    # 创建时间
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    # 更新时间
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    # 分类排序，数值越大越靠前
    sort = Column(Integer, nullable=False)
    # 逻辑删除：0 - 正常，1 - 已删除
    is_deleted = Column(Boolean, nullable=False, default=False)