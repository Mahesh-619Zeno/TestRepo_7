import os
import json
import datetime

DATA_FILE = "tasks.json"
LOG_FILE = "task_manager.log"

class Task:
    def __init__(self, id, title, completed=False, tags=None, created=None, updated=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.tags = tags or []
        self.created = created or datetime.datetime.now().isoformat()
        self.updated = updated or self.created

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "tags": self.tags,
            "created": self.created,
            "updated": self.updated,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            completed=data["completed"],
            tags=data.get("tags", []),
            created=data.get("created"),
            updated=data.get("updated")
        )

    def __str__(self):
        status = "✅" if self.completed else "❌"
        tags_str = ", ".join(self.tags) if self.tags else "None"
        return f"[{self.id}] {status} {self.title} (tags: {tags_str})"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1
        self.load()

    def log(self, message):
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.datetime.now().isoformat()} {message}\n")

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data.get("tasks", [])]
                self.counter = data.get("counter", self.counter)
            self.log("Loaded tasks from disk.")
        else:
            self.log("No data file found; starting with an empty task list.")

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "tasks": [task.to_dict() for task in self.tasks],
                "counter": self.counter
            }, f, indent=2)
        self.log("Saved tasks to disk.")

    def add_task(self, title, tags=None):
        task = Task(self.counter, title, tags=tags or [])
        self.tasks.append(task)
        self.counter += 1
        self.save()
        self.log(f"Added task {task.id}: {title}")
        print("Task added:", task)

    def list_tasks(self, show_all=False):
        filtered = self.tasks if show_all else [t for t in self.tasks if not t.completed]
        if not filtered:
            print("🗒️ No tasks to display.")
        for task in filtered:
            print(task)

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            task.completed = True
            task.updated = datetime.datetime.now().isoformat()
            self.save()
            self.log(f"Marked task {task_id} as completed")
            print("Completed:", task)
        else:
            print("Task not found.")

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            self.log(f"Deleted task {task_id}")
            print("Deleted:", task)
        else:
            print("Task not found.")

    def search_tasks(self, term):
        results = [t for t in self.tasks if term.lower() in t.title.lower()]
        if not results:
            print("No tasks found matching:", term)
        else:
            for task in results:
                print(task)

    def tag_task(self, task_id, tags):
        task = self._find_task(task_id)
        if task:
            new_tags = set(task.tags + tags)
            task.tags = list(new_tags)
            task.updated = datetime.datetime.now().isoformat()
            self.save()
            self.log(f"Tagged task {task_id} with: {tags}")
            print("Updated:", task)
        else:
            print("Task not found.")

    def _find_task(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)


def menu():
    manager = TaskManager()

    while True:
        print("\n== Task Manager ==")
        print("1) Add Task")
        print("2) List Uncompleted Tasks")
        print("3) List All Tasks")
        print("4) Complete Task")
        print("5) Delete Task")
        print("6) Search Tasks")
        print("7) Tag Task")
        print("8) Exit")

        choice = input("> ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            tags = input("Tags (comma-separated, optional): ").strip()
            tag_list = [tag.strip() for tag in tags.split(",")] if tags else []
            manager.add_task(title, tag_list)

        elif choice == "2":
            manager.list_tasks(show_all=False)

        elif choice == "3":
            manager.list_tasks(show_all=True)

        elif choice == "4":
            task_id = input("Task ID to complete: ").strip()
            if task_id.isdigit():
                manager.complete_task(int(task_id))
            else:
                print("Invalid task ID.")

        elif choice == "5":
            task_id = input("Task ID to delete: ").strip()
            if task_id.isdigit():
                manager.delete_task(int(task_id))
            else:
                print("Invalid task ID.")

        elif choice == "6":
            term = input("Search term: ").strip()
            manager.search_tasks(term)

        elif choice == "7":
            task_id = input("Task ID to tag: ").strip()
            tags = input("Tags (comma-separated): ").strip()
            tag_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
            if task_id.isdigit():
                manager.tag_task(int(task_id), tag_list)
            else:
                print("Invalid task ID.")

        elif choice == "8":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    menu()
