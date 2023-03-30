import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    axes[0].plot(x, y, 'g-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


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

# matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

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
            update_figure(table_contents)

window.close()