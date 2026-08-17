import redis
from app.core.config import settings
from app.core.logger_config import logger

try:
    # 创建全局唯一连接池
    pool = redis.ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=getattr(settings, "REDIS_PASSWORD", None),
        decode_responses=True,
        max_connections=20,      # 最大连接数
        )
    # 创建全局复用 Redis 客户端实例
    redis_client = redis.Redis(connection_pool=pool)
    logger.info("Redis client created successfully")
except Exception as e:
    logger.error(f"Failed to create Redis client: {e}")

def get_redis():
    '''
    获取 Redis 客户端实例
    :return: Redis 客户端实例
    '''
    return redis_client

if __name__ == '__main__':
    get_redis().set('name', 'runbook')  # 设置 name 对应的值
    print(get_redis().get('name'))  # 获取 name 对应的值
