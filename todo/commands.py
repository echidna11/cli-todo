from .models import Database 

class todolist:
    db = None

    def __init__(self):
        self.db = Database()

    def add_task(self, task : str) -> None:
        self.db.add(task)

    def list_tasks(self) -> dict:
        # Fix here: Create and return a dictionary
        tasks_dict = {row['id']: row['task'] for row in self.db.list()}
        return tasks_dict
    
    def remove_task(self, task_id: int) -> None:
        self.db.remove(task_id)

    def clear(self) -> None:
        self.db.clear()