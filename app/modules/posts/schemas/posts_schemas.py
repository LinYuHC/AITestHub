from pydantic import BaseModel

# 基础模型（存放公共字段）
class PostBase(BaseModel):
    title: str
    summary: str
    content: str
    status: int=1   # 默认1：已发布
    category_id: int | None = None
    author_id: int | None = None
    cover_image: str | None = None
    allow_comment: bool = True
    is_top: bool = False