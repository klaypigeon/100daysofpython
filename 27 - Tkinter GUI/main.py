import tkinter


def button_clicked():
    my_label["text"] = my_input.get()


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="More New")

button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()

my_input = tkinter.Entry(width=10)
my_input.pack()





window. mainloop()
