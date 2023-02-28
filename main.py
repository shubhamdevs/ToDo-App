print("Welcome to ToDo App")


# Crating a get_todos() function to get previous tasks.
def get_todos():
    with open("todos.txt", "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


# Taking User Input:
while True:
    user_input = input("Type add, edit, complete, show or exit: ")
    user_input = user_input.strip()

    # matching user input with the assigned cases:
    if user_input.startswith("add"):
        todo_list = get_todos()
        todo = user_input[4:]
        todo_list.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todo_list)

    elif user_input.startswith("edit"):
        try:
            todo_list = get_todos()

            num = int(user_input[5:])
            new_todo = input("Enter the new todo: ")

            todo_list[num - 1] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todo_list)

        # Checking for a Value Error as takes integers and if the user only mention strings.
        except ValueError:
            print("Your Command is not valid")
            continue

    elif user_input.startswith("complete"):
        try:
            todo_list = get_todos()

            num = int(user_input[9:])
            index = num - 1
            todoToDelete = todo_list[index].strip("\n")
            todo_list.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todo_list)

            print(f"Task {todoToDelete} is removed from the list")

        # Checking if the user input a task number that is not present in the task list. It will give Index Error.
        except IndexError:
            print("There is no item with that number: ")
            continue

    elif user_input.startswith("show"):
        todo_list = get_todos()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}.{item}")

        file.close()

    elif user_input.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Thank you for using Todo App")
