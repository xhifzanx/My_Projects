import PySimpleGUIQt as s
my_layout = [
    [s.Text("hello world!")],
    [s.Button("OK"), s.Button("Cancel")]
]
window = s.Window(title="hello world", size=(640, 480), layout=my_layout)
window.read()