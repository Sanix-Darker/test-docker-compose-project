from sqlalchemy import Column, Integer, String, MetaData, Table, text
from db import engine, SessionLocal

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
)

def prepare_db():
    metadata.create_all(engine)

def seed_and_read():
    with engine.begin() as conn:
        conn.execute(todos.insert().values(title="docka is amazing (from postgresql)!"))
        result = conn.execute(text("SELECT id, title FROM todos"))
        for row in result:
            print(dict(row))

if __name__ == "__main__":
    prepare_db()
    seed_and_read()
