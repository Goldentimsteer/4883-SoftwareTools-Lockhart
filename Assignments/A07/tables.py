import PySimpleGUI as sg  
import numpy as np 

def build_display(table,Daily):
    sg.set_options(font=("Arial Bold", 14))
    #if daily then the headers will change
    if Daily:
            top = ['Time', 'Temp', 'Dew Point', 'Humidity', 'Wind', 'Wind Speed', 'Wind Gust', 'Pressure', 'Precipitation', 'Condition']
            rows = table
    else:
        top = ['Time', 'Temp', 'Dew Point', 'Humidity', 'Wind', 'Pressure', 'Precipitation']
        rows = np.array(table).T.tolist()
    tbl1 = sg.Table(values=rows, headings=top,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)
    layout = [[tbl1]]

    #sets window size
    window = sg.Window("Weather stats", layout, size=(tbl1.get_size()[0], tbl1.get_size()[1]), resizable=False)
    window.read()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
