from fastapi import FastAPI, Depends, HTTPException, APIRouter,status
from app.models.user import Users
from app.services import user_service
from app.services.user_service import *
from app.schemas.user_schemas import *


router = APIRouter()
@router.post("/auth/register",
             response_model=UserBase,
             status_code=status.HTTP_201_CREATED
             )
async def register_user(user:UserBase):
    return user_service.register_user(user)

# if __name__ == '__main__':
#     register_user(UserBase(username="fhc", password="", phone="+91"))