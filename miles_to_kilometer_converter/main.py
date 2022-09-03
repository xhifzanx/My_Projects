import tkinter

def calculate():
    mile = entry.get()
    mile = int(mile)
    km = 1.609 * mile
    answer.config(text=f"{km}")
    return km
#Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(width=20, height=20)
#Label
label = tkinter.Label(text="  ")
label.grid(column=0, row=0)
#Entry
entry = tkinter.Entry(width=7)
entry.grid(column=1, row=0)
#Label 2
label_2 = tkinter.Label(text="Miles")
label_2.grid(column=3, row=0)
#Label 3
label_3 = tkinter.Label(text="is equal to")
label_3.grid(column=0, row=1)
#Answer
answer = tkinter.Label(text=0)
answer.grid(column=1, row=1)
#Label 4
label_4 = tkinter.Label(text="Km")
label_4.grid(column=2, row=1)
#Button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()