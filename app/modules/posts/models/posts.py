from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from app.db.database import Base
from app.common.eunms import PostStatus


class Post(Base):
    __tablename__ = "posts"
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    # 文章标题
    title = Column(String(255), nullable=False)
    # 文章摘要 / 描述
    summary = Column(String(500), nullable=False)
    # 文章正文（存储Markdown源码）
    content = Column(Text, nullable=False)
    # 文章状态：1 - 已发布，2 - 草稿 3删除
    status = Column(Integer, default=PostStatus.DRAFT, nullable=False)
    # 阅读量
    views_count = Column(Integer, default=0, nullable=False)
    # 文章分类ID
    category_id = Column(
        Integer,
        ForeignKey(
            "categories.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )
    # 创建时间
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    # 更新时间
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    # 文章封面图片资源Key
    cover_image = Column(String(500), nullable=True)
    # 是否允许评论：0 - 否，1 - 是
    allow_comment = Column(Boolean, default=True, nullable=False)
    # 是否置顶：0 - 否，1 - 是
    is_top = Column(Boolean, default=False, nullable=False)
    # 逻辑删除：0 - 正常，1 - 已删除
    is_deleted = Column(Boolean, default=False, nullable=False)
    # 文章作者ID
    author_id = Column(Integer,
    ForeignKey(
        "user.id",
        ondelete="RESTRICT"
    ),
    nullable=False,
    index=True)