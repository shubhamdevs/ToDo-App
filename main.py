print("Welcome to ToDo App")

todo_list = []

# Taking User Input:
while True:
    user_input = input("Type add or show")

    match user_input:
        case "add":
            todo = input("Enter a todo: ")
            todo_list.append(todo)
        case "show":
            print(todo_list)
