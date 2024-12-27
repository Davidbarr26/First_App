"""
Project: PythonProject
program: file compressor
Purpose: To create .zip files
Revision History:
    Created on December 26th 2024. By Juan (David) Barrios Rozo
"""

import FreeSimpleGUI as ui
import zip_creator

label1 = ui.Text("Select files to compress: ")
input1 = ui.Input()
choose_button_1 = ui.FilesBrowse("Select", key='files')

label2 = ui.Text("Select destination folder: ")
input2 = ui.Input()
choose_button_2 = ui.FolderBrowse("Select", key='folder')

compress_button = ui.Button("Compress")
output_label = ui.Text(key="output", text_color="green")

window = ui.Window("File Compressor",
                   layout=[[label1, input1, choose_button_1],
                           [label2, input2, choose_button_2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    folder = values['folder']
    zip_creator.make_archieve(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()

