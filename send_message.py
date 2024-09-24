import os
from dotenv import load_dotenv
from twilio.rest import Client

# load environmental variable.
load_dotenv()

class SendMessage:

    def __init__(self):

        self.account_sid = os.getenv('twilio_account_sid')
        self.auth_token = os.getenv('twilio_auth_token')
        self.client = Client(self.account_sid, self.auth_token)

        self.from_whatsapp_number = os.getenv('twilio_my_number')

    def send_whatsapp_message(self, to_number:str, media_url:str, body:str) ->dict:
        """
        This function send whatsapp message to the number given.
        :param body: caption of the user.
        :param media_url: url of the image.
        :param to_number: number of the receiver.
        :return:
        """
        # convert number to whatsapp.
        to_number= f"whatsapp:{to_number}"
        try:
            self.client.messages.create(
                body= body,
                from_=self.from_whatsapp_number,
                to= to_number,
                media_url= [media_url]
            )

            return {"success":True, "response":"message queued."}
        except:
            return {"success": False, "response": "error while sending message."}

