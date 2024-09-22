import tkinter

class UI:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Amazon Australia Deals Newsletter")
        self.window.geometry("1000x800")

        # create a canvas.
        self.canvas = tkinter.Canvas(self.window, bg= "gray20", width=1000, height=800, highlightthickness= 0)

        # add amazon icon.
        self.icon_path = tkinter.PhotoImage(file="Images/amazon_icon.png")
        self.canvas.create_image(500, 400, image= self.icon_path)

        self.canvas.place(x=0, y=0)



    def exit(self):
        self.window.mainloop()


app = UI()
app.exit()