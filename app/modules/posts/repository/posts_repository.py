from sqlalchemy.orm import Session
# 导入模型
from app.modules.posts.models import posts

def create_posts(db: Session, post: posts.Post):
    # 创建博客
    db.add(post)
    db.commit()
    db.refresh(post)