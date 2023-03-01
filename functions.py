
# reading the todo list and listing them in a variable
def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


# writing the todo list with assigned values
def write_todos(todo_arg, filepath="todos.txt"):
    with open(filepath, "w") as file_local:
        file_local.writelines(todo_arg)
