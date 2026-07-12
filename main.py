from fastapi import FastAPI
# 导入路由
from app.api.userapi import router as user_api_router

app = FastAPI()
app.include_router(user_api_router, prefix="/api/v1")
@app.get("/")
async def root():
    return {"message": "testSuccess"}