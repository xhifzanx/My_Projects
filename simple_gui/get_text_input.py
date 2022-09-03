import PySimpleGUIQt as sg
form = sg.FlexForm('My First GUI')
layout = [
    [sg.Text("Enter your name", size=(15, 1)), sg.InputText()],
    [sg.Text("Enter your country", size=(15, 1)), sg.InputText()],
    [sg.Text("Enter your city", size=(15, 1)), sg.InputText()],
    [sg.Text("Enter your phone", size=(15, 1)), sg.InputText()],
    [sg.OK(), sg.Cancel()]
]

button, value = form.Layout(layout).Read()
print(value)
print(value[0])
print(button)