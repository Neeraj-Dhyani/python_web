from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql+psycopg://postgres:post%40sql@localhost:5432/todo_list"

engine = create_engine(database_url)

sessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)