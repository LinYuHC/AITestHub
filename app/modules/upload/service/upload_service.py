import shutil
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
from app.core.config import settings

def upload_file(file: UploadFile):
    # 1. 定义项目根目录及上传目录
    BASE_DIR = Path(__file__).resolve().parents[3]
    UPLOAD_DIR = BASE_DIR / settings.UPLOAD_PATH

    # 确保 uploads 文件夹存在，不存在则自动创建
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # 校验文件类型（企业级安全规范：限制只能上传图片）
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="只能上传图片文件！")

    try:
        # 为了防止文件名重复覆盖，利用时间戳或 UUID 生成唯一文件名
        import uuid

        file_extension = Path(file.filename).suffix  # 获取后缀名，如 .jpg, .png
        unique_filename = f"{uuid.uuid4()}{file_extension}"

        # 最终保存文件的绝对路径
        file_path = UPLOAD_DIR / unique_filename

        # 将上传的文件流写入到本地磁盘
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 4. 拼接返回给前端/数据库的访问 URL
        # 例如：http://你的服务器IP:8000/static/xxxx-xxxx.png
        file_url = f"/static/{unique_filename}"

        return {
            "code": 200,
            "message": "图片上传成功",
            "data": {
                "url": file_url,
                "filename": unique_filename,
            },
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"上传失败: {str(e)}")


if __name__ == '__main__':
    from fastapi import FastAPI

    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
    # testapp = FastAPI()
    #
    #
    # @testapp.post(path="/upload")
    # async def test_route(files: UploadFile = File(...)):  # 修改点1：换个名字，防止覆盖上面的核心业务函数
    #     return upload_file(files)  # 修改点2：这里现在能正确调用到你最上面的 upload_file 函数了
    #
    #
    # from fastapi.testclient import TestClient
    #
    # client = TestClient(testapp)
    #
    # test_image_path = r"C:\Users\Administrator\Pictures\test.png"
    #
    # # 4. 模拟发送 POST 请求上传文件
    # with open(test_image_path, "rb") as f:
    #     response = client.post(
    #         "/upload", files={"files": ("test.png", f, "image/jpeg")}
    #     )
    #     print("测试结果响应：", response.json())