class Task():
   def __init__(self, description, deadline, status):
    self.description = description
    self.deadline = deadline
    self.status = status


   def add_tasks(self):

       self.description = input("Добавте задачу: ")
       print(self.description)
   def mark_tasks(self):

       self.deadline = input("Крайний срок выполнения: ")
       print(self.deadline)

   def list_tasks(self):

       self.status = input("Статус выполнения: ")
       print(self.status)







task1 = Task("Задача 1", "2020-10-10", "Не выполнено")
task2 = Task("Написать реферат", "2024-03-24", "Выполнено")
#print(task2.description)
#print(task2.deadline)
#print(task2.status)
task1.add_tasks()
task1.mark_tasks()
task1.list_tasks()

