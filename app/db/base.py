# app/db/base.py
from app.db.database import Base

# ⚠️ 必须把所有的 ORM Model 都在这里导入一遍
from app.modules.user.models import User
from app.modules.posts.models.posts import Post
from app.modules.posts.models.categories import Category