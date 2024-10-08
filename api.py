import os
import requests

from dotenv import load_dotenv

# load environment.
load_dotenv()

class API_FETCH:

    def __init__(self):

        self.whatsapp_url = os.getenv('whatsapp_url')
        self.whatsapp_key = os.getenv('whatsapp_api_key')
        self.whatsapp_host = os.getenv('whatsapp_api_host')

        self.amazon_url = os.getenv('amazon_url')
        self.amazon_key = os.getenv('amazon_api_key')
        self.amazon_host = os.getenv('amazon_api_host')

    def validate_whatsapp(self, number:int) -> dict:
        """
        This function takes number of the user and validate if user whatsapp number exist or not
        :param number: number of user with country code.
        :return: dict.
        """

        querystring= {"number":number}

        headers= {
            "x-rapidapi-key":self.whatsapp_key,
            "x-rapidapi-host":self.whatsapp_host,
        }

        try:
            response = requests.get(self.whatsapp_url, headers=headers, params=querystring)
            response.raise_for_status()

            return {"success":True, "response":response.json()}
        except requests.RequestException as e:
            return {"success":False, "response":f"error: {e}"}

    def fetch_deals(self, number_of_deals:int = 10) -> dict:
        """
        This function fetch real time data from amazon deals.
        :param number_of_deals: number of deals required, default - top 10.
        :return: dict object
        """

        headers = {
            "x-rapidapi-key":self.amazon_key,
            "x-rapidapi-host":self.amazon_host,
        }

        query_string = {
                        "country":"US",
                        "min_product_star_rating":"ALL",
                        "price_range":"ALL",
                        "discount_range":"ALL",
                       }

        try:
            deals_data = requests.get(url=self.amazon_url, headers=headers, params=query_string)
            deals_data.raise_for_status()
            return {"success":True, "response":deals_data.json()}

        except requests.RequestException as e:
            return {"success":False, "response":f"Error {e.response.status_code} - {e.response.text}"}

class SheetyUpdate:

    def __init__(self):

        self.end_point = os.getenv('sheety_url')
        self.bear_token = os.getenv('sheety_BEARER_TOKEN')

    def add_customer(self, email:str, username:str, phone_number:int, category:int, number_of_deals:int = 10) -> dict:

        # Check - all the values are not None.
        if not all([email, username, phone_number, category, number_of_deals]):
            return {"success":False, "response":"Please fill all the required values."}

        header = {
            "Authorization": f"Bearer {self.bear_token}"
        }

        customer_data = {
                        "customer" : {
                                        "email":email,
                                        "username":username,
                                        "phonenumber":phone_number,
                                        "category":category,
                                        "numberdeals":number_of_deals,
                                      }
                        }

        try:
            response = requests.post(url=self.end_point,json=customer_data, headers=header)
            response.raise_for_status()
            return {"success":True, "response":"Customer Added"}
        except requests.RequestException as e:
            return {"success": False, "response": f"error: {e}"}

    def check_customer(self, email:str, phone_number:int):
        """
        This function check if the given customer already exist in the database or not.
        :param email: email of the new customer
        :param phone_number: phone number of the new customer.
        :return: dictionary variable, response.
        """

        # check if username is not empty.
        if not all([email, phone_number]):
            return {"success": False, "response": "Please Enter email and phone number."}

        header = {
            "Authorization": f"Bearer {self.bear_token}"
        }

        try:
            response = requests.get(url=self.end_point, headers=header)
            response.raise_for_status()

            # check if the user exist.
            customers_data = response.json()['customer']

            # loop over each customer value and check if email and phone number exist.
            for customer in customers_data:
                customer_email = customer['email']
                customer_phone_number = customer['phonenumber']

                # check if the phone number or email already exist.
                if customer_email == email:
                    return {"success": False, "response": f"Customer email already register."}

                elif customer_phone_number == phone_number:
                    return {"success": False, "response": f"Customer phone number already register."}

            return {"success":True, "response":"Register Successfully."}

        except requests.RequestException as e:
            return {"success": False, "response": f"error: {e}"}


    def get_subscriber(self):
        """
        This function fetch the data of the subscriber and return it in a dictionary.
        :return: dictionary.
        """

        header = {
            "Authorization": f"Bearer {self.bear_token}"
        }

        try:
            response = requests.get(url=self.end_point, headers=header)
            response.raise_for_status()
            return {"success":True, "response":response.json()}

        except requests.RequestException as e:
            return {"success": False, "response": f"error: {e}"}

