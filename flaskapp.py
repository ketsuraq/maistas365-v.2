from flask import Flask, render_template
from scraper import scrape_data

flaskapp = Flask(__name__)


@flaskapp.route('/')
def index():
    title, about, price, discount = scrape_data()
    return render_template('index.html', title=title, about=about, price=price, discount=discount)


if __name__ == '__main__':
    flaskapp.run(debug=True)