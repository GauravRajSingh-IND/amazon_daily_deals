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

            return {"success":True, "response":response.text}
        except requests.RequestException as e:
            return {"success":False, "response":f"error: {e}"}
