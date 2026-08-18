import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings
import uuid

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_EXPIRE_MINUTES
def generate_token(payload: dict):
    '''
    生成token
    :param payload:
    :return: token,jti
    '''
    # 拷贝传入的数据，避免修改原字典
    to_encode = payload.copy()
    # 记录签发时间 (iat)
    now = datetime.now(timezone.utc)
    # 设置过期时间 (exp)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    jti = str(uuid.uuid4())
    # 将签发时间和过期时间写入用户信息
    to_encode.update({
        "jti":jti,
        "iat": now,  # Issued At: 签发时间戳
        "exp": expire  # Expiration Time: 到期时间戳
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token,jti

def decode_token(token: str):
    '''
    解码token
    :param token:
    :return: payload
    '''
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
