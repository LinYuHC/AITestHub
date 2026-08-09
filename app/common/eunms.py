from enum import IntEnum


class PostStatus(IntEnum):
    '''
    枚举类
    '''
    PUBLISHED = 1 # 已发布
    DRAFT = 2   # 草稿
    DELETED = 3 # 删除