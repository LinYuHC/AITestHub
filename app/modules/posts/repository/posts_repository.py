from sqlalchemy.orm import Session
# 导入模型
from app.modules.posts.models import posts,categories
from app.modules.posts.schemas.posts_schemas import PostBase


def create_posts_service(db: Session, post: posts.Post) -> posts.Post:
    # 创建博客
    db.add(post)
    db.commit()
    db.refresh(post)
    return post