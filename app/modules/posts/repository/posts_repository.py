from sqlalchemy.orm import Session
from app.modules.posts.models.posts import Post
from app.db.database import get_db
from app.modules.posts.schemas.posts_schemas import PostsListOut
# 导入模型
from app.modules.posts.models import posts

def create_posts(db: Session, post: posts.Post):
    # 创建博客
    db.add(post)
    db.commit()
    db.refresh(post)

def get_posts_list(db: Session, title: str | None = None):
    '''
    获取博客列表（默认所有），可根据据标题模糊搜索
    :param db:
    :return:
    '''
    # 默认查所有
    query = db.query(posts.Post)
    if title:
        # 模糊搜索标题
        query = db.query(posts.Post).where(posts.Post.title.contains(title))
    return query.all()

