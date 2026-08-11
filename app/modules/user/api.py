from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.schemas.response import ResponseModel
from app.modules.user.schemas import UserBase, UserOut
from app.modules.user import service
from sqlalchemy.orm import Session


router = APIRouter()
@router.post("/auth/register",
             response_model=ResponseModel[UserOut]
             )
def register_user(user:UserBase, db: Session = Depends(get_db)):
    return service.register_user(db, user)

if __name__ == '__main__':
    import asyncio
    asyncio.run(register_user(UserBase(username="fhc", password="", phone="+91")))