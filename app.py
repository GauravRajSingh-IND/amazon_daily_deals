import tkinter
from api import API_FETCH, SheetyUpdate


class UI:

    def __init__(self):

        self.api = API_FETCH()
        self.sheety = SheetyUpdate()

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
        """
        This function activates when user clicks on subscribe button. And get information from text field.
        This function also validate the whatsapp number entered by user.
        :return:
        """

        # assign all the values to variables.
        username = self.username_input.get()
        email = self.email_input.get()
        phone_number = int(self.number_input.get())

        # check if customer exist or not.
        is_new_customer= self.sheety.check_customer(email=email, phone_number=phone_number)['success']
        if not is_new_customer:
            self.canvas.itemconfig(self.success_message, text="Customer already registered")
            return {"success": False, "response": "Customer already exist."}

        # validate whatsapp number.
        on_whatsapp = self.api.validate_whatsapp(number=phone_number)

        if not on_whatsapp["success"]:
            self.canvas.itemconfig(self.success_message, text="Server Error Try Again")
            return {"success":False, "response":"Error while validating whatsapp account, Please try again"}

        if not on_whatsapp["response"]["valid"]:
            self.canvas.itemconfig(self.success_message, text="Whatsapp Number Not Found")
            return {"success": False, "response": "Whatsapp account not found, Please try again with valid whatsapp account."}

        try:
            deals_category:int = int(self.category_input.get())
            number_deals:int = int(self.number_deals_input.get())
        except ValueError:
            self.canvas.itemconfig(self.success_message, text="Error in required values")
            return {"success": False, "response": "Please enter integers values for deals category and number of deals."}

        # check if all variables are not None.
        if not all([username, email, phone_number, deals_category, number_deals]):
            return {"success":False, "response":"required field empty"}

        # add user data to google sheet.
        self.sheety.add_customer(email=email, username=username, phone_number=phone_number, category=deals_category,
                                 number_of_deals=number_deals)

        # add success message to canvas.
        self.canvas.itemconfig(self.success_message, text= "Subscribed")
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
        self.success_message = self.canvas.create_text(400, 700, text="", font=('arial', 30, 'bold'), fill="snow",
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
