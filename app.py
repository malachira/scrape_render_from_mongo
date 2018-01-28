from flask import Flask, render_template, jsonify, redirect
import scrape_mars
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def index():
    mars_news = mongo.db.mars_news.find_one()
    return render_template('index.html', mars_news=mars_news)

@app.route('/scrape')
def scrape():
    mars_news = mongo.db.mars_news
    data = scrape_mars.scrape()
    mars_news.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)