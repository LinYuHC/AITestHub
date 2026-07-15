from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Pydantic模型
# 基础模型（共享字段）
class UserBase(BaseModel):
    username: str
    password: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    sex: Optional[int] = None
    nickname: Optional[str] = None


class UserOut(BaseModel):
    username: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    sex: Optional[int] = None
    nickname: Optional[str] = None

    class Config:
        from_attributes = True