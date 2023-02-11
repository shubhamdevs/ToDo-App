print("Welcome to ToDo App")

todo_list = []

# Taking User Input:
while True:
    user_input = input("Type add, show or exit: ")

    # matching user input with the assigned cases:
    match user_input:

        case "add":
            todo = input("Enter a todo: ")
            todo_list.append(todo)

        case "show":
            print(todo_list)

        case "exit":
            break

print("Thank you for using Todo App")
