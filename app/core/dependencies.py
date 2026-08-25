from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.utils.pyjwt_tool import decode_token
from app.db.redis_db import get_redis
from app.modules.user.repository import get_user_by_id
from app.db.database import get_db


# HTTPBearer负责从请求头中提取 Bearer Token
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    '''
    获取当前用户
    :param credentials:
    :param db:
    :return:
    '''
    # 1. 从 Authorization Header 获取 Token
    token = credentials.credentials

    # 2. 验证 JWT
    payload = decode_token(token)
    print(f'打印payload: {payload}')

    # 3. JWT 验证失败
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 无效或已过期"
        )



    # 获取jti
    jti = payload.get("jti")

    # 4. 查询 Redis
    session = get_redis().get(f"user:token:{jti}")

    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 无效或已过期"
        )

    #  从 JWT 中获取用户ID
    user_id = payload.get("user_id")

    # MySQL
    user = get_user_by_id(db,user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 中缺少用户信息"
        )

    # 暂时直接返回 user_id
    return user_id