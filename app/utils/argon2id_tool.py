from argon2 import PasswordHasher


ph = PasswordHasher()
def hash_password(password: str) -> str:
    """
    Hash a password using Argon2id
    :param password: The password to hash
    :return: The hashed password
    """
    return ph.hash(password)

def verify_password(hashed_password: str, password: str) -> bool:
    """
    Verify a password against a hashed password
    :param password: The password to verify
    :param hashed_password: The hashed password to verify against
    :return: True if the password is correct, False otherwise
    """
    try:
        return ph.verify(hashed_password, password)
    except Exception as e:
        print(f'Error verifying password: {e}')
        return False

def needs_rehash(hashed_password: str) -> bool:
    return ph.check_needs_rehash(hashed_password)

if __name__ == '__main__':
    password = "123456"
    hashed_password = hash_password(password)
    print(hashed_password)

    pwd = verify_password(hashed_password, "123456")
    print("Password is correct",pwd)

    rehash = needs_rehash(hashed_password)
    print("Needs rehash",rehash)