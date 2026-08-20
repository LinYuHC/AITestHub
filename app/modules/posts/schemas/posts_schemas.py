import datetime
from pydantic import BaseModel, ConfigDict


# 基础模型（存放公共字段）
class PostBase(BaseModel):
    title: str
    summary: str
    content: str
    status: int=2   # 默认2，1：已发布2：草稿
    category_id: int | None = None
    # author_id: int
    cover_image: str | None = None
    allow_comment: bool = True
    is_top: bool = False

    # model_config = ConfigDict(arbitrary_types_allowed=True)
    class Config:
        from_attributes = True

class PostsDetailsOut(BaseModel):
    '''
    博客详情返回模型
    '''
    id: int
    title: str
    summary: str
    content: str
    views_count: int
    status: int
    category_id: int
    cover_image: str | None = None
    allow_comment: bool = True
    is_top: bool = False
    author_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)

class PostsListOut(BaseModel):
    '''
    博客列表返回模型
    '''
    id: int
    title: str
    summary: str
    views_count: int
    category_id: int
    cover_image: str | None = None
    author_id: int

    class Config:
        from_attributes = True

class PostsListData(BaseModel):
    '''
    博客列表数据模型，包含分页信息
    '''
    total: int
    page: int | None = None
    page_size: int | None = None
    items: list[PostsListOut]

    class Config:
        orm_mode = True