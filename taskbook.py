import sys

class Task:
    def __init__(self,task_id, task_detail) -> None:
        self.id = task_id
        self.text = task_detail
    
    def modify_task(self,task_id,task_detail):
        if self.id == task_id:
            self.text = task_detail
    



class Taskbook:
    all_task = []

    def __init__(self) -> None:
        self.tasks = []

    def add_task(self,task_id,task_detail):
        self.tasks.append(Task(task_id,task_detail))

    def modify_task(self,task_id,task_detail):
        for i in self.tasks:
            if i.id == task_id:
                i.text = task_detail 
    
                


if __name__=="__main__":
    t = Taskbook()

    t.add_task(1,'Task 1')
    t.add_task(2,'Task 2')
    t.add_task(3,'Task 3')
    t.add_task(4,'Task 4')

    t.modify_task(4,"Task 4 Changed")
    for i in t.tasks:
        print(f"Task {i.id} : {i.text}")