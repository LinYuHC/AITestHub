from fastapi import APIRouter
from app.schemas.response import ResponseModel
from app.modules.user.schemas import UserBase, UserOut
from app.modules.user import service


router = APIRouter()
@router.post("/auth/register",
             response_model=ResponseModel[UserOut]
             )
async def register_user(user:UserBase):
    return service.register_user(user)

if __name__ == '__main__':
    import asyncio
    asyncio.run(register_user(UserBase(username="fhc", password="", phone="+91")))