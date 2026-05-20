from sqlmodel import create_engine

engine = create_engine(f"postgresql://myuser:mypassword@localhost:5433/mydatabase")