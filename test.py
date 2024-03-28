class Task:
    def __init__(self, description, deadline, status="Не выполнено"):
        self.description = description
        self.deadline = deadline
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print("Задача добавлена.")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Выполнено"
                print(f"Задача '{description}' отмечена как выполненная.")
                break
        else:
            print("Задача не найдена.")

    def list_current_tasks(self):
        print("Текущие задачи (Не выполнено):")
        for task in self.tasks:
            if task.status == "Не выполнено":
                print(f"Описание: {task.description}, Срок: {task.deadline}")

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Задача 1", "2022-12-01")
task_manager.add_task("Задача 2", "2022-12-15")
task_manager.mark_task_completed("Задача 1")
task_manager.list_current_tasks()