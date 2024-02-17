from flask import Flask, render_template, request, jsonify
from scraper import scrape_data
from flask_cors import CORS

flaskapp = Flask(__name__)
CORS(flaskapp)

@flaskapp.route('/')
def index():
    return render_template('index.html')

@flaskapp.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data['url']
    title, about, price, discount = scrape_data(url)
    return jsonify({'title': title, 'about': about, 'price': price, 'discount': discount})

if __name__ == '__main__':
    flaskapp.run(debug=True)
