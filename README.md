# Movie Recommendation System

A collaborative filtering-based movie recommendation system that uses cosine similarity and matrix factorization techniques to provide personalized movie recommendations. The system features a modern web interface with movie posters and real-time search functionality.

## Features

- **Advanced Recommendation Engine**
  - Collaborative filtering using cosine similarity
  - Matrix factorization (SVD) for improved recommendations
  - Movie-movie similarity for more accurate suggestions
  - Handles missing ratings and edge cases

- **Interactive Web Interface**
  - Real-time movie search functionality
  - 5-star rating system
  - Dynamic movie recommendations
  - Responsive design for all devices

- **Movie Information**
  - Movie posters from OMDB API
  - Genre information
  - Title and release year
  - Predicted ratings for recommendations

## Tech Stack

- **Backend**
  - Python 3.12
  - Flask 3.0.2
  - Pandas 2.2.1
  - Scikit-learn 1.6.1
  - NumPy 1.26.4
  - SciPy 1.12.0

- **Frontend**
  - HTML5
  - CSS3 (with Flexbox and Grid)
  - Vanilla JavaScript
  - OMDB API for movie posters

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd movie-recommender
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the MovieLens dataset:
```bash
python download_data.py
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
movie-recommender/
├── app.py                 # Main Flask application
├── recommender.py         # Recommendation engine implementation
├── download_data.py       # Script to download MovieLens dataset
├── requirements.txt       # Python dependencies
├── static/               # Static files
│   ├── style.css         # CSS styles
│   └── placeholder.jpg   # Default movie poster
├── templates/            # HTML templates
│   └── index.html        # Main application template
└── data/                 # Movie dataset
    ├── movies.csv        # Movie information
    └── ratings.csv       # User ratings
```

## Usage

1. **Searching Movies**
   - Use the search bar at the top to find specific movies
   - Results update in real-time as you type
   - Click on a movie to see more details

2. **Rating Movies**
   - Browse through the movie grid
   - Click on the stars to rate movies (1-5 stars)
   - Your ratings are saved automatically

3. **Getting Recommendations**
   - Rate at least one movie to get recommendations
   - Recommendations appear in the bottom section
   - Each recommendation shows:
     - Movie poster
     - Title
     - Genres
     - Predicted rating

## API Endpoints

- `GET /`: Main application page
- `GET /api/movies`: Get all available movies
- `GET /api/search?q=<query>`: Search movies by title
- `POST /api/recommendations`: Get personalized recommendations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MovieLens dataset for providing the movie data
- OMDB API for movie posters
- Flask framework and its contributors
- All the open-source libraries used in this project 