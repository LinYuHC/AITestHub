from pathlib import Path
# 导入配置文件
from app.core.config import settings
import logging
from datetime import datetime

# 获取当前config.py所在目录
# config_dir = Path(__file__)
# 获取项目根目录，在当前目录的上一级目录
PROJECT_ROOT=  Path(__file__).parent.parent.parent
# 创建日志目录
LOG_DIR = PROJECT_ROOT / settings.LOG_PATH
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------# logging.basicConfig----------------------
logging.basicConfig(
    level=logging.ERROR,    #级别
    filename=f"{LOG_DIR}/{datetime.today().strftime('%Y-%m-%d')}.log",  #日志存放路径
    filemode="a",           #写日志模式
    format="%(asctime)s [%(lineno)d] %(message)s %(filename)s",   #格式

)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")


#---------------loger----------------

logger = logging.getLogger('sqlalchemy')

file_h = logging.FileHandler(f"{LOG_DIR}/logger.log")
print_h = logging.StreamHandler()

fm = logging.Formatter("%(asctime)s %(message)s")

file_h.setFormatter(fm)
print_h.setFormatter(fm)


logger.addHandler(file_h)
logger.addHandler(print_h)
logger.setLevel("DEBUG")

#------------------------------------------------------

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

"""
# 获取当前config.py所在目录
# config_dir = Path(__file__)
# 获取项目根目录，在当前目录的上一级目录
PROJECT_ROOT=  Path(__file__).parent.parent.parent
# 创建日志目录
LOG_DIR = PROJECT_ROOT / settings.LOG_PATH
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 配置根日志器，自动捕获所有库的日志
logging.basicConfig(
    level=logging.DEBUG,  # 捕获 DEBUG 及以上级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/app.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# 获取名为'my_logger'的Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG
logger.setLevel(logging.ERROR)  # 设置日志级别为ERROR
logger.setLevel(logging.INFO)  # 设置日志级别为INFO

# 日志创建路径
file_handler_path = f'{PROJECT_ROOT}/{settings.LOG_PATH}/user.log'
# 创建一个Handler来将日志写入文件
file_handler = logging.FileHandler(file_handler_path, encoding='utf-8')
print(f'file_handler_path: {file_handler_path}')

file_handler.setLevel(logging.DEBUG)  # 该Handler只记录DEBUG及以上级别的日志
file_handler.setLevel(logging.ERROR)  # 该Handler只记录ERROR及以上级别的日志
file_handler.setLevel(logging.INFO)  # 该Handler只记录ERROR及以上级别的日志

# 创建一个Handler来将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 控制台仅记录INFO及以上级别的日志

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将Handler添加到Logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 使用不同的日志级别记录消息
# logger.debug('这是一条DEBUG级别的消息')  # 不会被任何处理器记录，因为它低于它们的设置级别
# logger.info('这是一条INFO级别的消息')  # 会被console_handler处理并显示在控制台
# logger.warning('这是一条WARNING级别的消息')  # 会被console_handler处理并显示在控制台
# logger.error('这是一条ERROR级别的消息')  # 会被file_handler和console_handler处理，并记录到文件和控制台
# logger.critical('这是一条CRITICAL级别的消息')  # 同上
"""
# if __name__ == '__main__':
#
#
#     print()