from sqlmodel import create_engine

def get_secret(secret: str):
    path = f"/run/secrets/{secret}"
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise RuntimeError(f"Secret db_name not found at {path}")

user = get_secret("db_user")
password = get_secret("db_password")
name = get_secret("db_name")

engine = create_engine(f"postgresql://{user}:{password}@db:5432/{name}")

SECRET_KEY = get_secret("secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30