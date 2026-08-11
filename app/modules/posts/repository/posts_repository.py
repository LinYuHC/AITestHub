from sqlalchemy.orm import Session
# 导入模型
from app.modules.posts.models import posts

def create_posts_repository(db: Session, post: posts.Post) -> posts.Post:
    # 创建博客
    db.add(post)
    db.commit()
    db.refresh(post)
    return post