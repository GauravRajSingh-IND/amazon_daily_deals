import tkinter

class UI:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Amazon Australia Deals Newsletter")
        self.window.geometry("1000x800")
        self.window.config(bg= "gray20")

        # add Icon

    def exit(self):
        self.window.mainloop()


app = UI()
app.exit()