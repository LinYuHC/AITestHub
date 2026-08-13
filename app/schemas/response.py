from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, Any

T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[T] = None

    class Config:
        from_attributes = True  # 支持 ORM 对象自动转换

class ResponseError(BaseModel):
    code: int = 500
    message: str = "error"
    data: Optional[Any] = None

    class Config:
        from_attributes = True  # 支持 ORM 对象自动转换