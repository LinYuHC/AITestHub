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

