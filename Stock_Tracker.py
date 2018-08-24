from flask import Flask, render_template, request
from stock_data import get_nasdaq_stocks
from stock_analysis import get_basic_info

app = Flask(__name__)


@app.route('/')
def getStock():

    return render_template('index.html', nasdaq_stocks=get_nasdaq_stocks())


@app.route('/showData', methods=['POST', 'GET'])
def show_data():
    if request.method == 'POST':
        stockName = request.form['stockName']
        return render_template("showData.html", stock_name=stockName, basic_info=get_basic_info(stockName))




if __name__ == '__main__':
    app.run()
