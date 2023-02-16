print("Welcome to ToDo App")

# Taking User Input:
while True:
    user_input = input("Type add, edit, complete, show or exit: ")
    user_input = user_input.strip()

    # matching user input with the assigned cases:
    match user_input:

        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todo_list)
            file.close()

        case "edit":

            file = open("todos.txt", "r")
            todo_list = file.readlines()
            num = int(input("Number of the todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todo_list[num - 1] = new_todo
            file.close()

        case "complete":
            file = open("todos.txt", "w")
            todo_list = file.readlines()
            num = int(input("Enter the number of completed todo: "))
            todo_list.pop(num - 1)
            file.close()

        case "show":
            file = open("todos.txt", "r")
            todo_list = file.readlines()
            file.close()

            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                print(f"{index + 1}.{item}")

            file.close()

        case "exit":
            break

print("Thank you for using Todo App")
