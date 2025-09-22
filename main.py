import todo
from todo import commands as tl
import argparse

todo = tl.todolist()

class client:

    Parser = None

    def __init__(self):
        self.Parser = argparse.ArgumentParser(
            prog="todo",
            description="A simple command line todo list application",
            epilog="Enjoy the app!"
        )
        self.Parser.add_argument("todo")

    def parse_args(self):
        self.Parser.add_argument("command", help="Subcommand to run")
        self.Parser.add_argument("args", nargs="*", help="Arguments for the subcommand")
        return self.Parser.parse_args()


if __name__ == "__main__":
    client = client()
    while True:
        args = client.parse_args()

        if args.command == "add":
            if len(args.args) == 0:
                print("Error: No task provided to add.")
            else:
                task = " ".join(args.args)
                todo.add_task(task)
                print(f"Added task: {task}")

        elif args.command == "list":
            tasks = todo.list_tasks()
            if not tasks:
                print("No tasks in the todo list.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif args.command == "remove":
            if len(args.args) != 1 or not args.args[0].isdigit():
                print("Error: Please provide the task number to remove.")
            else:
                task_number = int(args.args[0])
                try:
                    removed_task = todo.remove_task(task_number - 1)
                    print(f"Removed task: {removed_task}")
                except IndexError:
                    print("Error: Task number out of range.")

        else:
            print(f"Unknown command: {args.command}")
            client.Parser.print_help()