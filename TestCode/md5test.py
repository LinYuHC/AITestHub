import hashlib

def hash_password(password):
    # 创建md5对象
    md5 = hashlib.md5()

    md5.update(password.encode())

    return md5.hexdigest()

if __name__ == '__main__':
    print(hash_password("123456"))