"""
模型导出模块
集中导出所有模型，方便其他模块导入
"""

from app.models.user import User

# __all__ 定义了 from router.models import * 时会导入哪些内容
__all__ = ["User"]