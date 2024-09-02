class TaskManager(list):
    def __init__(self):
        self.to_do = []
        self.done = []
    def add_task(self,*args):
        added_tasks = []
        for task in args:
            if task.lower() not in [content.lower() for content in self.to_do]:
                self.to_do.append(task)
                added_tasks.append(task)
        if added_tasks:
            return f"{', '.join(added_tasks)} added successfully. "
        else:
            return f"{task} already in the to-do list:\n {self.to_do}"
    def remove_task(self,*args):
        removed_tasks = []
        not_found_tasks = []

        for task in args:
            if task in self.to_do:
                self.to_do.remove(task)
                removed_tasks.append(task)
            else:
                not_found_tasks.append(task)

        if removed_tasks and not_found_tasks:
            return f"{', '.join(removed_tasks)} removed successfully. However, {', '.join(not_found_tasks)} not found in the to-do list."
        elif removed_tasks:
            return f"{', '.join(removed_tasks)} removed successfully."
        elif not_found_tasks:
            return f"{', '.join(not_found_tasks)} not found in the to-do list."
    def task_done(self,*args):
        done_tasks = []
        for task in args:
            if task in self.to_do and task not in self.done:
                self.done.append(task)
                self.to_do.remove(task)
                done_tasks.append(task)
            elif task in self.done:
                return "Already done."
            elif task not in self.to_do:
                return f"{task} not in the to-do list."

        if done_tasks:
            return f"{', '.join(done_tasks)} marked as done."
        else:
            return "No tasks were marked as done."

    def current_state(self,option='both'):
        if option == 'both':
            return f"Your tasks to do are:\n{self.to_do}\nYour done tasks are:\n {self.done}"
        elif option == 'to-do':
            return f"Your current to do list is:\n{self.to_do}"
        elif option == 'done':
            return f"Your done tasks are:\n{self.done}"
    def clear_todo_list(self):
        self.to_do.clear()
        return "To-Do list cleared."
    def clear_done_list(self):
        self.done.clear()
        return "Done list cleared."
    def reset(self):
        self.to_do.clear()
        self.done.clear()
        return "Both lists reseted and cleaned."



