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

SECRET_KEY = "df9564678fa80612898b78d7abd7f35477f93dbd23c39932f664285acb4a9834"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30