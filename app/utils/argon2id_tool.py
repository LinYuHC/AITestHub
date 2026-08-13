from argon2 import PasswordHasher

def hash_password(password: str) -> str:
    """
    Hash a password using Argon2id
    :param password: The password to hash
    :return: The hashed password
    """
    ph = PasswordHasher()
    return ph.hash(password)

if __name__ == '__main__':
    password = "123456"
    hashed_password = hash_password(password)
    print(hashed_password)

    pwd = PasswordHasher().verify(hashed_password, "1234516")
    print("Password is correct",pwd)