from flask import Flask, render_template
from stock_data import get_nasdaq_stocks

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/testdata')
def getData():

    return render_template('test.html', nasdaq_stocks=get_nasdaq_stocks())


if __name__ == '__main__':
    app.run()
