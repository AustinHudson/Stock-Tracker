import csv


def get_nasdaq_stocks():
    nasdaq_stocks = []

    with open('/Users/austinhudson/PycharmProjects/Stock-Tracker/exchange_CSVs/NASDAQ_companylist.csv', 'r') as nasdaq:
        reader = csv.reader(nasdaq)
        for row in reader:
            nasdaq_stocks.append({'symbol': row[0], 'name': row[1], 'sector': row[6], 'industry': row[7]})
    return nasdaq_stocks

