print("Welcome to ToDo App")

todo_list = []

# Taking User Input:
while True:
    user_input = input("Type add, edit, show or exit: ")
    user_input = user_input.strip()

    # matching user input with the assigned cases:
    match user_input:

        case "add":
            todo = input("Enter a todo: ")
            todo_list.append(todo)

        case "edit":
            num = int(input("Number of the todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todo_list[num - 1] = new_todo

        case "show":
            for index, item in enumerate(todo_list):
                print(f"{index + 1}.{item}")

        case "exit":
            break

print("Thank you for using Todo App")
