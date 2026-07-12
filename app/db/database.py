# 导入create_engine引擎，用于创建引擎以调用
from sqlalchemy import create_engine
from sqlalchemy import URL
# 导入会话工厂
from sqlalchemy.orm import sessionmaker,declarative_base

# 导入数据库配置
from app.core.config import settings
url_object = URL.create(
    drivername="mysql+pymysql",
    username=settings.MYSQL_USER,
    password=settings.MYSQL_PASSWORD,
    host=settings.MYSQL_HOST,
    port=settings.MYSQL_PORT,
    database=settings.MYSQL_DATABASE,
)

engine = create_engine(
    url_object,

    #   每次从连接池取连接时，先发送一个 ping 检测连接是否有效
    #   如果连接已断开，自动创建新连接，避免 "MySQL server has gone away" 错误
    pool_pre_ping=True,

    # pool_recycle=3600：
    #   连接在池中存活 1 小时后强制回收
    #   防止 MySQL 的 wait_timeout 导致连接超时
    pool_recycle=3600,

    # pool_size=10：
    #   连接池保持 10 个常驻连接
    pool_size=10,

    # max_overflow=20：
    #   当 10 个连接不够用时，最多额外创建 20 个临时连接
    max_overflow=20,

    # echo=False：
    #   设为 True 会在控制台打印所有执行的 SQL 语句（调试用）
    echo=False
)

# 创建会话工厂
SessionLocal = sessionmaker(
    # 禁止自动提交，需要手动调用 db.commit() 才会写入数据库
    #   这样可以确保事务完整性，出错时可以回滚
    autocommit=False,
    # autoflush=False：
    #   禁止自动刷新，需要手动调用 db.flush() 才会把操作发送到数据库
    #   避免在查询时意外触发 flush 导致性能问题
    autoflush=False,
    # 绑定引擎
    bind=engine
)

# 4. 创建模型基类（Base）
# ============================================
# 所有数据库模型都继承这个基类
# SQLAlchemy 通过它知道哪些类是数据库表
Base = declarative_base()


# ============================================
# 5. FastAPI 依赖注入函数
# ============================================
# 在路由中使用 Depends(get_db) 获取数据库会话
# 确保每次请求都有独立的会话，请求结束后自动关闭
def get_db():
    """
    生成数据库会话的生成器
    用法：在路由函数参数中写 db: Session = Depends(get_db)
    """
    # 创建一个新的数据库会话
    db = SessionLocal()
    try:
        # yield 返回会话给路由函数使用
        yield db
    finally:
        # 无论路由函数是否报错，最后都会执行这里关闭会话
        # 避免连接泄漏
        db.close()