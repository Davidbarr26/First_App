"""
Project: PythonProject
program: To-Do App
Purpose: To create a To-Do application
Revision History:
    Created on December 20th 2024. By Juan (David) Barrios Rozo
    edited on December 22nd 2024. By Juan (David) Barrios Rozo
    edited on December 23rd 2024. By Juan (David) Barrios Rozo
    edited on December 24th 2024. By Juan (David) Barrios Rozo
    edited on December 25th 2024. By Juan (David) Barrios Rozo
    edited on December 26th 2024. By Juan (David) Barrios Rozo
"""
import functions
import time

date = time.strftime("%A, %d, %b, %Y \nTime: %H:%M:%S (%Z)")
print(date)

# This loop will run as many times as the user wants before writing 'exit' to exit the program.
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        #Iterate through the list
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[4:])
            print(num)
            num = num - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[num] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. Try Again!")
            continue

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])

            todos = functions.get_todos()
            index = num - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"You've completed '{todo_to_remove}' and it has been removed from the list"
            print(message)

        except IndexError:
            print("No data was found with that number. Try Again!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Please enter a valid command! Try again.")

print("Thank you!")

