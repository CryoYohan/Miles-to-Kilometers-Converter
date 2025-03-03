import tkinter

class Window():
    
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Miles to Kilometers Converter")
        self.window.minsize(width=500,height=300)
        self.my_label = tkinter.Label(text="Hello World Python", font=("Arial", 24, "bold"))
        self.my_label.pack()


if __name__ == "__main__":
    start = Window()
    start.window.mainloop()
