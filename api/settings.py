from sqlmodel import create_engine

engine = create_engine(f"postgresql://myuser:mypassword@localhost:5433/mydatabase")

SECRET_KEY = "df9564678fa80612898b78d7abd7f35477f93dbd23c39932f664285acb4a9834"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30