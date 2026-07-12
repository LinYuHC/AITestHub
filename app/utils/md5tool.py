import hashlib

def get_md5(text:str)->str:
    # 创建md5对象
    m = hashlib.md5()
    # 对字符串进行编码并更新
    m.update(text.encode())
    # 返回16进制的加密结果（通常为32位）
    return m.hexdigest()