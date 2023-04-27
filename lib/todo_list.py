class TodoList:
    def __init__(self):
        self.tasks = [] 

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.tasks.append(todo)
        
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = [item.task for item in self.tasks if item.complete == False]
        # for item in self.tasks:
        #     if item.complete == False:
        #         incomplete_tasks.append(item.task)
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_tasks = [item.task for item in self.tasks if item.complete]
        return complete_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for item in self.tasks:
            item.mark_complete()