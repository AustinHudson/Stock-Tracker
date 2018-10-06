import config
import requests
import json


################################################################################
# Makes a call to the alpha vantage 'Quote Endpoint' API to get the
# latest price and volume information for a security that is entered
# into the form.

# PARAMS : stock - the user entered stock symbol from the form.
################################################################################

def get_basic_info(stock):

    query_string = "function=GLOBAL_QUOTE&symbol=" + stock + "&apikey=" + config.api_key
    info = requests.get("https://www.alphavantage.co/query?" + query_string)
    json_info = json.loads(info.text)
    basic_stock_data = [];

    for section in json_info["Global Quote"]:
        section_text = section[4:]
        section_value = json_info["Global Quote"][section]
        basic_stock_data.append([section_text, section_value])
    return basic_stock_data



def calculate_score():
    current_score = 0


