from fastapi import UploadFile, HTTPException
from minio import Minio
import uuid
from app.core.config import settings
from app.modules.upload.schemas.upload_schema import UploadData
from app.schemas.response import ResponseModel

# 1. 初始化 MinIO 客户端 (注意用 19000 API 端口)
minio_client = Minio(
    endpoint=settings.MINIO_ENDPOINT,  # API 端口是 19000
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)
BUCKET_NAME = settings.UPLOAD_BUCKET_NAME

def upload_file(file: UploadFile):
    try:
        # 生成唯一文件名
        file_ext = file.filename.split(".")[-1] if "." in file.filename else ""
        object_name = f"{uuid.uuid4()}{'.' + file_ext if file_ext else ''}"

        # 2. 直接将内存/临时文件流传给 MinIO SDK (不要用 open())
        minio_client.put_object(
            bucket_name=BUCKET_NAME,
            object_name=object_name,
            data=file.file,  # 直接传 UploadFile 的 file 对象
            length=-1,  # -1 配合 part_size 表示流式上传
            part_size=10 * 1024 * 1024,  # 10MB 分片
            content_type=file.content_type
        )

        # 3. 拼接返回给前端的公网只读 URL (同样使用 19000 端口)
        file_url = f"http://{settings.MINIO_ENDPOINT}/{BUCKET_NAME}/{object_name}"

        return ResponseModel(
            code=200,
            message="success",
            data=UploadData(
                url=file_url,
                filename=file.filename
            )
        )
    except Exception as e:
        return ResponseModel(
            code=400,
            message=f"上传失败: {str(e)}",
            data=None
        )
        # raise HTTPException(status_code=500, detail=f"上传失败: {str(e)}")