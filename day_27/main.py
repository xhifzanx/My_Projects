import tkinter

def clicked_button():
    my_label["text"] = "Clicking........"
    text = input.get()
    my_label.config(text=text)

#Windows
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=40)

#Label
my_label = tkinter.Label(text="I am a Label",font=("Arial", 19, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=40)


#Entry
input = tkinter.Entry()
input.grid(column=3, row=2)
#input.pack()

#Button
button = tkinter.Button(text="Click here", command=clicked_button)
button.grid(column=1, row=1)
#button.pack()

button_2 = tkinter.Button(text="second button")
button_2.grid(column=2, row=0)



window.mainloop()