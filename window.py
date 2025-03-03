import tkinter

class Window():
    
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Miles to Kilometers Converter")
        self.window.minsize(width=500,height=300)
        self.label()
        self.button()
        self.entry()
        self.textbox()

    
    def button_click(self):
        self.my_label.config(text=self.entry.get())

    def label(self):
        self.my_label = tkinter.Label(text="Hello World Python", font=("Arial", 24, "bold"))
        self.my_label.pack()

    def button(self):
        self.button = tkinter.Button(text="Click Me", command=self.button_click)
        self.button.pack()
    
    def entry(self):
        self.entry = tkinter.Entry()
        self.entry.pack()

    
    def textbox(self):
        self.textbox = tkinter.Text(width=30,height=10)
        self.textbox.focus()
        self.textbox.insert(tkinter.END, "Example of multi-line entry")
        self.textbox.pack()


if __name__ == "__main__":
    start = Window()
    start.window.mainloop()
