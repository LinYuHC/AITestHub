from sqlalchemy.orm import Session
from app.modules.posts.models.posts import Post
from app.modules.posts.schemas.posts_schemas import PostBase, PostsListOut, PostsListData, PostsDetailsOut
from app.modules.posts.repository import posts_repository
from app.schemas.response import ResponseModel

def create_posts_service(db: Session,post: PostBase, author_id):
    '''
    创建博客
    :param db:
    :param post:
    :param author_id:
    :return:
    '''
    # 需要传参的数据模型
    db_posts = Post(
        title=post.title,
        summary=post.summary,
        content=post.content,
        status=post.status,
        category_id=post.category_id,
        author_id=author_id,
        cover_image=post.cover_image,
        allow_comment=post.allow_comment,
        is_top=post.is_top
    )

    try:
        # 执行创建
        posts_repository.create_posts(db, db_posts)
        # 校验模型参数
        posts_uot = PostBase.model_validate(db_posts)
        # 获取并返回模型响应
        res = ResponseModel(data=posts_uot)
        return res
    except Exception as e:
        res = ResponseModel(code=500, message=f"创建失败: {e}")
        return res

def get_posts_list_service(db: Session, page: int, page_size: int, title: str | None = None):
    '''
    获取博客列表（默认所有），可根据据标题模糊搜索
    :param db:
    :param page:
    :param page_size:
    :param title:
    :return:
    '''
    posts_all, total = posts_repository.get_posts_list(db, title=title, page=page, page_size=page_size)
    if posts_all:
        # 将查询结果转换为 Pydantic 模型列表
        posts_list_out = [PostsListOut.model_validate(post) for post in posts_all]
        # 包装查询结果
        posts_list_data = PostsListData(
            total=total,
            page=page,
            page_size=page_size,
            items=posts_list_out
        )
        # 返回响应模型
        res = ResponseModel(data=posts_list_data)
        return res
    else:
        res = ResponseModel(data=PostsListData(total=0, page=page, page_size=page_size, items=[]))
        return res

def get_posts_details(db: Session, posts_id: int):
    posts_details = posts_repository.get_posts_details(db, posts_id)
    if posts_details:
        print('存在')
        postindustrial = PostsDetailsOut.model_validate(posts_details)
        res = ResponseModel(data=postindustrial)
        return res
    else:
        res = ResponseModel(code=404, message="博客不存在")
        return res