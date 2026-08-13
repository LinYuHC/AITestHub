from sqlalchemy.orm import Session
from app.modules.posts.models.posts import Post
from app.modules.posts.schemas.posts_schemas import PostBase
from app.modules.posts.repository import posts_repository
from app.schemas.response import ResponseModel

def create_posts_service(db: Session,post: PostBase):
    # 需要传参的数据模型
    db_posts = Post(
        title=post.title,
        summary=post.summary,
        content=post.content,
        status=post.status,
        category_id=post.category_id,
        author_id=post.author_id,
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

if __name__ == '__main__':
    # 1. 构造一个测试用的 Pydantic Schema 参数对象
    # test_post_data = PostBase(
    #     title="这是我的测试文章标题",
    #     summary="这是文章摘要说明",
    #     content="# 测试文章正文\n\n这是 Markdown 内容...",
    #     status=1,
    #     category_id=1,
    #     author_id=1,
    #     cover_image="https://example.com/cover.jpg",
    #     allow_comment=True,
    #     is_top=False
    # )
    # create_posts_service(test_post_data)
    pass
