# Write your solution here:
class Task:
    id = 0
    def __init__(self, description, programmer, workload, ):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._finished = False
        if Task:
            Task.id += 1
            self.id = Task.id

    def __str__(self):
        finished = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finished}"

    def is_finished(self):
        return True if self._finished else False

    def mark_finished(self):
        self._finished = True

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return [task for task in self.orders]

    def programmers(self):
        return list(set([task.programmer for task in self.orders]))

    # garbage code, rewrite
    def mark_finished(self, id: int):
        task_id = [task.id for task in self.orders]
        if id not in task_id:
            raise ValueError
        for task in self.orders:
            if task.id == id:
                task.mark_finished()

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        programmer_names = list(set([task.programmer for task in self.orders]))
        if programmer not in programmer_names:
            raise ValueError

        finished_tasks = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished_tasks = [task for task in self.unfinished_orders() if task.programmer == programmer]
        hours_worked = sum(task.workload for task in finished_tasks)
        hours_remaining = sum(task.workload for task in unfinished_tasks)
        req_tuple = (len(finished_tasks), len(unfinished_tasks), hours_worked, hours_remaining)

        return req_tuple
