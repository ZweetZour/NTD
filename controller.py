class TodoController:

    def __init__(self, model):
        self.model = model

    def get_tasks(self):
        return self.model.get_all_tasks()

    def add_task(self, task_name):
        return self.model.add_task(task_name)

    def delete_task(self, index):
        return self.model.delete_task(index)