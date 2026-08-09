from app.modules.posts.models.posts import Post
from app.modules.posts.schemas.posts_schemas import PostBase
# 导入会话
from app.db.database import SessionLocal
from app.modules.user.models import User
from app.modules.posts.models.categories import Category
def create_posts_service(post: PostBase):
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

    # 创建会话工厂
    db = SessionLocal()
    # 创建博客
    db.add(db_posts)
    db.commit()
    db.close()
    return db_posts

if __name__ == '__main__':
    # 1. 构造一个测试用的 Pydantic Schema 参数对象
    test_post_data = PostBase(
        title="这是我的测试文章标题",
        summary="这是文章摘要说明",
        content="# 测试文章正文\n\n这是 Markdown 内容...",
        status=1,
        category_id=1,
        author_id=1,
        cover_image="https://example.com/cover.jpg",
        allow_comment=True,
        is_top=False
    )
    create_posts_service(test_post_data)
