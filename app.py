from flask import Flask, render_template, request, jsonify
from recommender import MovieRecommender
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Initialize the recommender system
recommender = MovieRecommender()

def get_movie_poster(title):
    # Search for movie poster using OMDB API
    try:
        # First try to get the year from the title
        year = None
        if '(' in title and ')' in title:
            year = title[title.find('(')+1:title.find(')')]
            title = title[:title.find('(')].strip()
        
        # Search OMDB API
        api_key = 'c34181b2'  # Your OMDB API key
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
        if year:
            url += f"&y={year}"
        
        response = requests.get(url)
        data = response.json()
        
        if data.get('Response') == 'True' and data.get('Poster') != 'N/A':
            return data['Poster']
    except:
        pass
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    user_ratings = data.get('ratings', {})
    
    # Get recommendations
    recommendations = recommender.get_recommendations(user_ratings)
    
    # Add poster URLs to recommendations
    for rec in recommendations:
        rec['poster_url'] = get_movie_poster(rec['title'])
    
    return jsonify(recommendations)

@app.route('/api/movies', methods=['GET'])
def get_movies():
    movies = recommender.get_all_movies()
    
    # Add poster URLs to movies
    for movie in movies:
        movie['poster_url'] = get_movie_poster(movie['title'])
    
    return jsonify(movies)

@app.route('/api/search', methods=['GET'])
def search_movies():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    movies = recommender.search_movies(query)
    
    # Add poster URLs to search results
    for movie in movies:
        movie['poster_url'] = get_movie_poster(movie['title'])
    
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True) 