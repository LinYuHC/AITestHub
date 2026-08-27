from fastapi import FastAPI
# 导入路由
from app.modules.user.api import router as user_api_router
from app.modules.upload.api.upload_api import router as upload_api_router
from app.modules.posts.api.posts_api import router as posts_api_router
# 导入表注册
import app.db.base
# 导入CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
# 当项目上线发布到真实服务器时，应将 allow_origins 里的 localhost:5173 替换为你前端上线的真实域名（如 [https://hub.example.com](https://hub.example.com)），避免接口被任意第三方恶意网页调用。
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://81.71.136.66:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_api_router, prefix="/api/v1")
app.include_router(upload_api_router, prefix="/api/v1")
app.include_router(posts_api_router, prefix="/api/v1")
@app.get("/")
async def root():
    return {"message": "testSuccess"}