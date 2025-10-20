import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds

class MovieRecommender:
    def __init__(self):
        # Load and preprocess the movie dataset
        self.movies_df = pd.read_csv('data/movies.csv')
        self.ratings_df = pd.read_csv('data/ratings.csv')
        
        # Create user-movie matrix
        self.ratings_matrix = self.ratings_df.pivot(
            index='userId',
            columns='movieId',
            values='rating'
        ).fillna(0)
        
        # Convert to numpy array for SVD
        self.ratings_array = self.ratings_matrix.to_numpy()
        
        # Store movie IDs for later use
        self.movie_ids = self.ratings_matrix.columns.tolist()
        
        # Compute cosine similarity matrix
        self.similarity_matrix = cosine_similarity(self.ratings_array.T)  # Transpose for movie-movie similarity
        
        # Perform matrix factorization
        U, sigma, Vt = svds(self.ratings_array.astype(float), k=min(50, min(self.ratings_array.shape)-1))
        sigma = np.diag(sigma)
        self.predicted_ratings = np.dot(np.dot(U, sigma), Vt)
        
    def get_recommendations(self, user_ratings):
        try:
            if not user_ratings:
                return []
            
            # Create a vector of user ratings aligned with movie_ids
            user_vector = np.zeros(len(self.movie_ids))
            for movie_id, rating in user_ratings.items():
                try:
                    movie_id = int(movie_id)
                    if movie_id in self.movie_ids:
                        idx = self.movie_ids.index(movie_id)
                        user_vector[idx] = float(rating)
                except (ValueError, TypeError):
                    continue
            
            # Get predicted ratings using movie-movie similarity
            user_predictions = np.dot(self.similarity_matrix, user_vector)
            
            # Get top recommendations (excluding already rated movies)
            rated_movies = [int(mid) for mid in user_ratings.keys() if str(mid).isdigit()]
            movie_scores = []
            
            for idx, score in enumerate(user_predictions):
                movie_id = self.movie_ids[idx]
                if movie_id not in rated_movies:
                    movie_scores.append((movie_id, score))
            
            # Sort by score and get top 10
            movie_scores.sort(key=lambda x: x[1], reverse=True)
            recommended_movies = []
            
            for movie_id, score in movie_scores[:10]:
                try:
                    movie_info = self.movies_df[self.movies_df['movieId'] == movie_id].iloc[0]
                    recommended_movies.append({
                        'id': int(movie_id),
                        'title': movie_info['title'],
                        'genres': movie_info['genres'],
                        'predicted_rating': float(score)
                    })
                except IndexError:
                    continue
            
            return recommended_movies
        except Exception as e:
            print(f"Error in get_recommendations: {str(e)}")
            return []
    
    def get_all_movies(self):
        # Return a list of all movies for the initial rating interface
        movies = []
        for _, movie in self.movies_df.iterrows():
            movies.append({
                'movieId': int(movie['movieId']),
                'title': movie['title'],
                'genres': movie['genres']
            })
        return movies
        
    def search_movies(self, query):
        # Search movies by title
        query = query.lower()
        movies = []
        for _, movie in self.movies_df.iterrows():
            if query in movie['title'].lower():
                movies.append({
                    'movieId': int(movie['movieId']),
                    'title': movie['title'],
                    'genres': movie['genres']
                })
        return movies 