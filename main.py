from fastapi import FastAPI
# 导入路由
from app.modules.user.api import router as user_api_router
from app.modules.upload.api.upload_api import router as upload_api_router
app = FastAPI()

# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
# # ... 你原本的代码: app = FastAPI(title="AITestHub API") ...
# # 1. 定位到你的 uploads 文件夹
# BASE_DIR = Path(__file__).resolve().parent
# UPLOAD_DIR = BASE_DIR / "uploads"
# # 2. 【核心步骤】将 /static 请求映射到本地的 uploads 文件夹
# app.mount("/static", StaticFiles(directory=str(UPLOAD_DIR)), name="static")

app.include_router(user_api_router, prefix="/api/v1")
app.include_router(upload_api_router, prefix="/api/v1")
@app.get("/")
async def root():
    return {"message": "testSuccess"}