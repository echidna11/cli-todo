import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

class Database:

    db_url = "postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase"

    def __init__(self):
        self.engine = create_engine(self.db_url, echo=True)
        with self.engine.connect() as conn:
            conn.execute(text("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)"))
            conn.commit()

    def add(self, task: str) -> None:
        with self.engine.connect() as conn:
            conn.execute(text("INSERT INTO tasks (task) VALUES (:task)"), {"task": task})
            conn.commit() 

    def list(self) -> dict:
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT id, task FROM tasks"))
            return result.mappings()
        
    def remove(self, task_id: int) -> None:
        with self.engine.connect() as conn:
            conn.execute(text("DELETE FROM tasks WHERE id = :id"), {"id": task_id})
            conn.commit()