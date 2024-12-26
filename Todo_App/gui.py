import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do to the list: ")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
show_button = sg.Button("Show")
complete_button = sg.Button("Complete")

window = sg.Window('To-Do App', layout=[[label], [input_box, add_button], [edit_button, show_button, complete_button]])
window.read()
window.close()