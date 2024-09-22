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

        # Add Signup labels.
        self.labels_signup()
        self.input_signup()

        # Button - Add Customer.
        self.button_signin = tkinter.Button(self.window, text= "Subscribe", font=('arial', 30, 'bold'), anchor= "center")
        self.button_signin.place(x=480, y=570)


    def labels_signup(self):
        # add text.
        self.canvas.create_text(500, 100, text="Amazon Newsletter", font=('arial', 30, 'bold'), fill="snow",
                                anchor="center")
        self.canvas.create_text(200, 200, text="username : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 270, text="Email : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 340, text="number : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 410, text="category : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")
        self.canvas.create_text(200, 480, text="No. Deals : ", font=('arial', 30, 'bold'), fill="snow",
                                anchor="w")

        self.canvas.place(x=0, y=0)

    def input_signup(self):
        self.username_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                            foreground="gray20")
        self.username_input.place(x=400, y=180)

        self.email_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                         foreground="gray20")
        self.email_input.place(x=400, y=250)

        self.number_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                          foreground="gray20")
        self.number_input.place(x=400, y=320)

        self.number_deals_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                                foreground="gray20")
        self.number_deals_input.place(x=400, y=460)

    def exit(self):
        self.window.mainloop()


app = UI()
app.exit()