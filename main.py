from datetime import datetime
from api import API_FETCH


# create a api_fetch object.
deals_fetch = API_FETCH()

deals_data = deals_fetch.fetch_deals(number_of_deals=10)['response']['data']['deals']

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



