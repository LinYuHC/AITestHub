import jwt
secret_key = "your-secret-key-change-in-production"
def generate_token(payload: dict) -> str:
    return jwt.encode(payload, secret_key, algorithm="HS256")

if __name__ == '__main__':
    token = generate_token({"user_id": 1})
    print(token)