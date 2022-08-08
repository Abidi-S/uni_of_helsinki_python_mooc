# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0
    def __init__(self, description, programmer, workload, ):
        self.description = description
        self.programmer = programmer
        self.workload = int(workload)
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

class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    def help(self):
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(" ")
        # print(f"{description} {programmer} {workload}")
        self.order_book.add_order(description, programmer, workload)
        print("added!")
        # for task in self.order_book.all_orders():
        #     print(task)

    def finished_tasks(self):
        if len(self.order_book.finished_orders()) == 0:
            print("no finished tasks")
        for task in self.order_book.finished_orders():
            print(task)

    def unfinished_tasks(self):
        if len(self.order_book.unfinished_orders()) == 0:
            print("no unfinished tasks")
        for task in self.order_book.unfinished_orders():
            print(task)

    def mark_finished(self):
        task_id = int(input("id: "))
        self.order_book.mark_finished(task_id)
        print("marked as finished")

    def programmers(self):
        for programmer in self.order_book.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        finished, unfinished, hours_done, hours_scheduled = self.order_book.status_of_programmer(programmer)
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {hours_done} scheduled {hours_scheduled}")

    def execute(self):
        print("commands: ")
        self.help()
        while True:
            print("")
            command = int(input("command: "))
            try:
                if command == 0:
                    break
                elif command == 1:
                    self.add_order()
                elif command == 2:
                    self.finished_tasks()
                elif command == 3:
                    self.unfinished_tasks()
                elif command == 4:
                    self.mark_finished()
                elif command == 5:
                    self.programmers()
                elif command == 6:
                    self.status_of_programmer()
                else:
                    self.help()
            except:
                print("erroneous input")

application = OrderBookApplication()
application.execute()