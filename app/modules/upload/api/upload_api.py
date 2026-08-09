from fastapi import APIRouter, UploadFile, File
from app.modules.upload.schemas.upload_schema import UploadData
from app.schemas.response import ResponseModel
from app.modules.upload.service import upload_service

router = APIRouter()

@router.post(
    "/auth/upload",
    response_model=ResponseModel[UploadData])
async def upload_file(file: UploadFile = File(...)):
    return upload_service.upload_file(file)

