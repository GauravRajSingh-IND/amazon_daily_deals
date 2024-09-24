from time import sleep

from api import API_FETCH, SheetyUpdate
from send_message import SendMessage

def fetch_deals():
    """
    This function fetch top 10 amazon deals and return a dict object
    :return: dict.
    """

    # create a dict of empty deals.
    deals = {}

    # create a api_fetch object.
    deals_fetch = API_FETCH()
    deals_data = deals_fetch.fetch_deals(number_of_deals=10)['response']['data']['deals']

    # check if deals is fetched or not.
    if deals_fetch.fetch_deals(number_of_deals=10)['success']:
        # loop over each deal.
        for i,deal in enumerate(deals_data):

            # top 10 deals.
            if deal['deal_state'] == 'AVAILABLE' and i <= 10:
                deal_title = deal['deal_title']
                deal_photo = deal['deal_photo']
                deal_url = deal['deal_url']
                deal_start_date_at = deal['deal_starts_at'].split('T')[0]
                deal_start_time_at = deal['deal_starts_at'].split('T')[1].split('.')[0]

                deal_end_date_at = deal['deal_ends_at'].split('T')[0]
                deals_end_time_at = deal['deal_ends_at'].split('T')[1].split('.')[0]

                discount = deal['deal_badge']
                product_asin = deal['product_asin']

                deals[product_asin] = {"deal_title":deal_title, "deal_photo":deal_photo, "deal_url":deal_url,
                                       "deal_start_date_at":deal_start_date_at, "deal_start_time_at":deal_start_time_at,
                                       "deal_end_date_at":deal_end_date_at, "deals_end_time_at":deals_end_time_at,
                                       "discount":discount}

        return {"success":True, "response":deals}

    else:
        return {"success": False, "response": "No Data"}

def create_message(deal:dict, number:int) ->dict:
    """
    This function create a caption by using deals data
    :param number: rank of deal from 1-10.
    :param deal: deal from amazon fetched data
    :return: dict object containing product url, product image, message.
    """

    deal_data = deal
    body = (f"{number+1}. 🛍️\n{deal_data['deal_title']}\n🛍️\n\n END_DATE: 🙅🏽{deal_data['deal_end_date_at']}🙅🏽\n\n Discount: 🤗{deal_data['discount']}🤗\n\n\n"
            f"🔗🔗\n\n{deal_data['deal_url']}\n\n🔗🔗")
    url = deal_data['deal_url']
    image = deal_data['deal_photo']
    return {"product_url":url, "product_image":image, "message":body}

# get amazon deals data.
deals = fetch_deals()

# get customer data.
customers_bd = SheetyUpdate()
customers = customers_bd.get_subscriber()

# create twilio object to send data.
twilio = SendMessage()

# loop over each customer and get customer id.
for customer in customers['response']['customer']:
    phone_number = f"+{customer['phonenumber']}"

    # loop over each deal fetched today.
    for number, key in enumerate(deals['response']):

        # get deal data.
        deal = deals['response'][key]
        message_body = create_message(deal=deal, number=number)

        # send messages.
        twilio.send_whatsapp_message(to_number=phone_number, media_url=message_body['product_image'], body=message_body['message'])




