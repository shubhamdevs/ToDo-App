print("Welcome to ToDo App")

user_prompt = "Enter a todo: "
todos = []

# Taking User Input:
while True:
    text = input(user_prompt)
    todos.append(text)
    print(todos)
