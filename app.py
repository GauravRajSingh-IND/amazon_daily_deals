import tkinter
from unicodedata import category


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
        self.button_signin = tkinter.Button(self.window, text= "Subscribe", font=('arial', 30, 'bold'), anchor= "center",
                                            command=self.get_user_data)
        self.button_signin.place(x=480, y=570)

    def get_user_data(self):

        # assign all the values to variables.
        username = self.username_input.get()
        email = self.email_input.get()
        phone_number = self.number_input.get()

        try:
            deals_category:int = int(self.category_input.get())
            number_deals:int = int(self.number_deals_input.get())
        except ValueError:
            return {"success": False, "response": "Please enter integers values for deals category and number of deals."}

        # check if all variables are not None.
        if not all([username, email, phone_number, deals_category, number_deals]):
            return {"success":False, "response":"required field empty"}

        return {email: {"username":username, "phone_number":phone_number, "category":deals_category, "number_deals":number_deals}}

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

        self.category_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                          foreground="gray20")
        self.category_input.place(x=400, y=390)

        self.number_deals_input = tkinter.Entry(self.window, background="snow", width=20, font=('arial', 30, 'bold'),
                                                foreground="gray20")
        self.number_deals_input.place(x=400, y=460)

    def exit(self):
        self.window.mainloop()


app = UI()
app.exit()