print("Welcome to ToDo App")

# Taking User Input:
while True:
    user_input = input("Type add, edit, complete, show or exit: ")
    user_input = user_input.strip()

    # matching user input with the assigned cases:
    if "add" in user_input:
        with open("todos.txt", "r") as file:
            todo_list = file.readlines()

        todo = user_input[4:]
        todo_list.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todo_list)

    elif "edit" in user_input:
        with open("todos.txt", "r") as file:
            todo_list = file.readlines()

        num = int(input("Number of the todo to edit: "))
        new_todo = input("Enter the new todo: ")

        todo_list[num - 1] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todo_list)

    elif "complete" in user_input:
        with open("todos.txt", "r") as file:
            todo_list = file.readlines()

        num = int(input("Enter the number of completed todo: "))
        index = num - 1
        todoToDelete = todo_list[index].strip("\n")
        todo_list.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todo_list)

        print(f"Task {todoToDelete} is removed from the list")

    elif "show" in user_input:
        with open("todos.txt", "r") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}.{item}")

        file.close()

    elif "exit" in user_input:
        break

print("Thank you for using Todo App")
