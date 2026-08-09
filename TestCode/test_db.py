from app.db.database import engine, SessionLocal
from app.db.database import Base  # 如果有导入 Base
from sqlalchemy import text
from models.user import Users


def test_connection():
    """测试数据库连接"""
    try:
        # 方式1：测试引擎连接
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"✅ 连接成功: {result.fetchone()}")

        # 方式2：测试创建表（如果有模型）
        # Base.metadata.create_all(bind=engine)
        # print("✅ 表创建成功")

        return True

    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return False


def test_session():
    """测试会话和简单查询"""
    db = SessionLocal()
    try:
        # 执行任意 SQL
        result = db.execute(text("SHOW DATABASES"))
        print("✅ 数据库列表:")
        for row in result:
            print(f"  - {row[0]}")

        # 测试当前数据库
        result = db.execute(text("SELECT DATABASE()"))
        current_db = result.fetchone()[0]
        print(f"✅ 当前数据库: {current_db}")

    except Exception as e:
        print(f"❌ 查询失败: {e}")
    finally:
        db.close()

def select_user():
    db = SessionLocal()
    user = db.query(Users).first()
    print(f"✅ 查询结果: {user}")

if __name__ == "__main__":
    print("=" * 40)
    print("测试数据库连接...")
    print("=" * 40)


    if test_connection():
        print("\n" + "=" * 40)
        print("测试会话查询...")
        print("=" * 40)
        test_session()
        select_user()