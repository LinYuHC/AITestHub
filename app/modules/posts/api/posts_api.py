# 导入路由
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user

from app.db.database import get_db
from app.modules.posts.schemas.posts_schemas import PostBase
from app.modules.posts.service import posts_service

router = APIRouter(
    prefix="/posts",
    tags=["博客"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/create",)
def create_post(post: PostBase,db:Session = Depends(get_db)):
    return posts_service.create_posts_service(db,post)