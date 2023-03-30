import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sg.theme('DarkGrey4')
table_contents = []
layout = [
    [sg.Table(
        headings=['Observation', 'Results'],
        values=table_contents,
        expand_x=True,
        hide_vertical_scroll=True,
        key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')],
    [sg.Canvas(key='-CANVAS-')]
]

window = sg.Window('Graph App', layout, finalize=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_contents.append([len(table_contents) + 1, float(new_value)])
            window['-TABLE-'].update(table_contents)
            window['-INPUT-'].update('')

window.close()
