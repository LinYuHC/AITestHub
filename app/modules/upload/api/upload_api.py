from fastapi import APIRouter, UploadFile, File, Depends
from app.modules.upload.schemas.upload_schema import UploadData
from app.schemas.response import ResponseModel
from app.modules.upload.service import upload_service
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix='/upload',
    tags=['上传'],
    dependencies=[Depends(get_current_user)]
)

@router.post(
    "/",
    response_model=ResponseModel[UploadData])
def upload_file(file: UploadFile = File(...)):
    return upload_service.upload_file(file)

