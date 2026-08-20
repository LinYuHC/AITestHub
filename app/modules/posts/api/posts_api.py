# 导入路由
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.modules.user.models import User
from app.db.database import get_db
from app.modules.posts.schemas.posts_schemas import PostBase, PostsListOut
from app.modules.posts.service import posts_service
from app.core.logger_config import logger
from app.schemas.response import ResponseModel
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=["博客"]
    # dependencies=[Depends(get_current_user)]
)

@router.post("/create",)
def create_post(post: PostBase,db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f'current_user==={current_user}')
    return posts_service.create_posts_service(db,post,author_id=current_user)

@router.get("/list")
def get_posts_list(
        db:Session = Depends(get_db),
        page: int =Query(1, ge=1, description='当前页码，必须 >= 1'),
        page_size: int = Query(10, ge=1, le=100, description='每页条数，必须 >= 1, <= 100'),
        title: str | None = Query(None, description='文章标题，模糊查询')):
    return posts_service.get_posts_list_service(
        db,
        title=title,
        page=page,
        page_size=page_size
    )

@router.get("/details")
def get_posts_details(
        posts_id: int,
        db:Session = Depends(get_db)):
    return posts_service.get_posts_details(db,posts_id)