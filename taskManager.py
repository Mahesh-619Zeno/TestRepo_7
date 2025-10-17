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
            data["id"],
            data["title"],
            data.get("completed", False),
            data.get("tags", []),
            data.get("created"),
            data.get("updated"),
        )

    def __str__(self):
        status = "✅" if self.completed else "❌"
        tags = ", ".join(self.tags)
        return f"[{self.id}] {status} {self.title} (tags: {tags})"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data.get("tasks", [])]
                self.counter = data.get("counter", self.counter)
            self.log("Loaded tasks from disk.")
        else:
            self.log("No data file found. Starting fresh.")

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump(
                {"tasks": [task.to_dict() for task in self.tasks], "counter": self.counter},
                f,
                indent=2
            )
        self.log("Saved tasks to disk.")

    def log(self, message):
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.datetime.now().isoformat()} {message}\n")

    def add_task(self, title, tags=None):
        task = Task(self.counter, title, False, tags or [])
        self.tasks.append(task)
        self.counter += 1
        self.save()
        self.log(f"Added task {task.id}: {title}")
        print("✅ Task added:", task)

    def list_tasks(self, show_all=False):
        filtered_tasks = sorted(self.tasks, key=lambda t: t.id)
        found = False
        for task in filtered_tasks:
            if show_all or not task.completed:
                print(task)
                found = True
        if not found:
            print("🗒️ No tasks to show.")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                if task.completed:
                    print("Task already completed.")
                    return
                task.completed = True
                task.updated = datetime.datetime.now().isoformat()
                self.save()
                self.log(f"Completed task {task_id}")
                print("✅ Completed:", task)
                return
        print("❌ Task not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                deleted = self.tasks.pop(i)
                self.save()
                self.log(f"Deleted task {task_id}")
                print("🗑️ Deleted:", deleted)
                return
        print("❌ Task not found.")

    def search(self, term):
        results = [t for t in self.tasks if term.lower() in t.title.lower()]
        if not results:
            print("🔍 No tasks found matching:", term)
        else:
            for task in results:
                print(task)

    def tag_task(self, task_id, tags):
        for task in self.tasks:
            if task.id == task_id:
                task.tags = list(set(task.tags + tags))
                task.updated = datetime.datetime.now().isoformat()
                self.save()
                self.log(f"Tagged task {task_id} with {tags}")
                print("🏷️ Updated:", task)
                return
        print("❌ Task not found.")


def prompt_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("⚠️ Invalid number.")
        return None

def prompt_tags():
    tags_input = input("Tags (comma-separated): ").strip()
    return [tag.strip() for tag in tags_input.split(",") if tag.strip()]

def menu():
    mgr = TaskManager()
    while True:
        print("\n== Task Manager ==")
        print("1) Add Task")
        print("2) List Tasks (uncompleted)")
        print("3) List All Tasks")
        print("4) Complete Task")
        print("5) Delete Task")
        print("6) Search Tasks")
        print("7) Tag Task")
        print("8) Exit")
        choice = input("> ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            tags = prompt_tags() if input("Add tags? (y/n): ").strip().lower() == "y" else []
            mgr.add_task(title, tags)

        elif choice == "2":
            mgr.list_tasks(show_all=False)

        elif choice == "3":
            mgr.list_tasks(show_all=True)

        elif choice == "4":
            task_id = prompt_int("Enter Task ID to complete: ")
            if task_id is not None:
                mgr.complete_task(task_id)

        elif choice == "5":
            task_id = prompt_int("Enter Task ID to delete: ")
            if task_id is not None:
                mgr.delete_task(task_id)

        elif choice == "6":
            term = input("Search term: ").strip()
            mgr.search(term)

        elif choice == "7":
            task_id = prompt_int("Enter Task ID to tag: ")
            if task_id is not None:
                tags = prompt_tags()
                mgr.tag_task(task_id, tags)

        elif choice == "8":
            print("👋 Bye!")
            break

        else:
            print("❌ Invalid choice. Please select a number between 1 and 8.")


if __name__ == "__main__":
    menu()
