class TodoModel:

    def __init__(self):
        # Lista que funcionará como nuestra "base de datos"
        self._tasks = []

    def add_task(self, task_name):
        task_name = task_name.strip()

        if task_name:
            self._tasks.append(task_name)
            return True

        return False

    def get_all_tasks(self):
        return self._tasks

    def delete_task(self, index):
        try:
            return self._tasks.pop(index)
        except IndexError:
            return None