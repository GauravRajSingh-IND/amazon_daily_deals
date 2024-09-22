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

        # add text.
        self.canvas.create_text(500, 100, text= "Amazon Newsletter", font= ('arial', 30, 'bold'), fill= "snow",
                                anchor= "center")
        self.canvas.create_text(200, 200, text= "username : ", font= ('arial', 30, 'bold'), fill= "snow",
                                anchor= "w")
        self.canvas.create_text(200, 270, text="Email : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 340, text="number : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 410, text="category : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 480, text="No. Deals : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")

        self.canvas.place(x=0, y=0)



    def exit(self):
        self.window.mainloop()


app = UI()
app.exit()