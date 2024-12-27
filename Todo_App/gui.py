import functions
import FreeSimpleGUI as UI

label = UI.Text("Type in a to-do")
input_box = UI.InputText(tooltip="Enter a to-do to the list: ", key='todo')
add_button = UI.Button("Add")
show_button = UI.Button("Show")
edit_button = UI.Button("Edit")
complete_button = UI.Button("Complete")
list_box = UI.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
exit_button = UI.Button("Exit")
footer = UI.Text(functions.display_copyright())

window = UI.Window('To-Do App',
                   layout=[[label],
                           [input_box],
                           [add_button,
                            show_button,
                            edit_button,
                            complete_button,
                            exit_button],
                           [list_box],
                           [footer]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case UI.WIN_CLOSED:
            break

window.close()