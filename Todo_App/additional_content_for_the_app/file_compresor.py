import FreeSimpleGUI as ui

label1 = ui.Text("Select files to compress: ")
input1 = ui.Input()
choose_button_1 = ui.FilesBrowse("Select")

label2 = ui.Text("Select destination folder: ")
input2 = ui.Input()
choose_button_2 = ui.FolderBrowse("Select")

compress_button = ui.Button("Compress")

window = ui.Window("File Compressor",
                   layout=[[label1, input1, choose_button_1],
                           [label2, input2, choose_button_2],
                           [compress_button]])
window.read()
window.close()

