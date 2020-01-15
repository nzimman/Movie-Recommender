from flask import Flask, render_template, request
from postgres_data import get_movie_list, connect_to_db
from recommender_cosine import calculate_cosim
import random


db = connect_to_db()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    items = get_movie_list(db)
    it1 = random.sample(items,10)
    it2 = random.sample(items ,10)
    it3 = random.sample(items,10)
    
    return render_template('recommender.html',items1=it1,items2=it2,items3=it3)

@app.route('/results')
def results():
    user_input = request.args #some kind of dictionary-like object
    recommend_movies = calculate_cosim(db,user_input)
    return render_template('results.html',movies=recommend_movies)
