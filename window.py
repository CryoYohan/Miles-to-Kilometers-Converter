import tkinter

class Window():
    
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Miles to Kilometers Converter")
        self.window.minsize(width=500,height=300)
        self.kilometers = 0
        self.miles_entry()
        self.miles_label()
        self.is_equal_to_km_label()
        self.km_label()
        self.km_label2()
        self.convert_button()

    
    def button_click(self):
        self.kilometers = round(float(self.entry.get()) * 1.60934, 2)
        self.my_label3.config(text=f"{self.kilometers}")

    def miles_label(self):
        self.my_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
        self.my_label.grid(row=0,column=3)
        self.my_label.config(padx=20, pady=20)
    
    def is_equal_to_km_label(self):
        self.my_label2 = tkinter.Label(text=f"is equal to ", font=("Arial", 24, "bold"))
        self.my_label2.grid(row=2,column=1)
        self.my_label2.config(padx=20, pady=20)
    
    def km_label(self):
        self.my_label3 = tkinter.Label(text=f"{self.kilometers}", font=("Arial", 24, "bold"))
        self.my_label3.grid(row=2,column=2)
    
    def km_label2(self):
        self.my_label4 = tkinter.Label(text=f"KM", font=("Arial", 24, "bold"))
        self.my_label4.grid(row=2,column=3)

    def convert_button(self):
        self.button = tkinter.Button(text="Convert Miles", command=self.button_click)
        self.button.grid(row=3,column=2)
        self.button.config(width=15, height=3, font=("Arial", 15, "bold"))
    
    def miles_entry(self):
        self.entry = tkinter.Entry()
        self.entry.grid(row=0,column=2)
        self.entry.config(width=7,font=("Arial", 24, "bold"))

    

if __name__ == "__main__":
    start = Window()
    start.window.mainloop()
