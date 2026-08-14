from pydantic import BaseModel, EmailStr
from typing import Optional

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
    id: int
    username: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    sex: Optional[int] = None
    nickname: Optional[str] = None

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_info: UserOut | None = None  # 可选返回用户信息

    class Config:
        from_attributes = True