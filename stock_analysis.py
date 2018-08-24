import config
import requests

def get_basic_info(stock):
    query_string = "function=GLOBAL_QUOTE&symbol=" + stock + "&apikey=" + config.api_key
    info = requests.get("https://www.alphavantage.co/query?" + query_string)
    return info.text




def calculate_score():
    current_score = 0


