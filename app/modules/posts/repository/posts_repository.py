from sqlalchemy.orm import Session
from app.modules.posts.models.posts import Post
# 导入模型
from app.modules.posts.models import posts

def create_posts(db: Session, post: posts.Post):
    # 创建博客
    db.add(post)
    db.commit()
    db.refresh(post)

def get_posts_list(db: Session, title: str | None = None, page: int = 1, page_size: int = 10):
    '''
    获取博客列表（默认所有），可根据据标题模糊搜索
    :param title:默认None，表示不进行标题搜索
    :param page_size:默认10，表示每页条数
    :param page:默认1，表示第几页
    :param db:
    :return:
    '''
    # 默认查所有
    query = db.query(posts.Post)
    if title:
        # 模糊搜索标题
        query = db.query(posts.Post).where(posts.Post.title.contains(title))
    # 根据is_top、id降序排序，并进行分页查询
    items = (
        query.order_by(Post.is_top.desc(), Post.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    # 统计total
    total = query.count()
    return items, total

def get_posts_details(db: Session, posts_id: int):
    '''
    获取博客详情
    :param db:
    :param posts_id:
    :return:
    '''
    query = db.query(posts.Post).filter(posts.Post.id == posts_id).first()
    print(f'query==: {query}')
    # print(f'query==: {query.id}')
    return query
