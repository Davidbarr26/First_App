import functions
import FreeSimpleGUI as UI

label = UI.Text("Type in a to-do")
input_box = UI.InputText(tooltip="Enter a to-do to the list: ")
add_button = UI.Button("Add")
edit_button = UI.Button("Edit")
show_button = UI.Button("Show")
complete_button = UI.Button("Complete")

window = UI.Window('To-Do App', layout=[[label], [input_box], [add_button, edit_button, show_button, complete_button]])
window.read()
window.close()