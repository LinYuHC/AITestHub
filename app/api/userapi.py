from fastapi import FastAPI, Depends, HTTPException, APIRouter,status
from app.models.user import User
from app.services import user_service
from app.services.user_service import *
from app.schemas.user_schemas import *


router = APIRouter()
@router.post("/auth/register",
             response_model=ResponseModel[UserOut]
             )
async def register_user(user:UserBase):
    return user_service.register_user(user)

# if __name__ == '__main__':
#     register_user(UserBase(username="fhc", password="", phone="+91"))