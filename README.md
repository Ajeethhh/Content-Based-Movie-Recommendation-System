# Content-Based-Movie-Recommendation-System
<img width="1919" height="984" alt="streamlit_image" src="https://github.com/user-attachments/assets/69592109-6d3c-48ab-8c95-18da312310e1" />

# Movie Recommendation System

This repository contains a **content-based movie recommendation system** built using Python. The system suggests movies similar to a given movie based on genres, cast, crew, keywords, and overview using Natural Language Processing (NLP) techniques and cosine similarity.

---

## Dataset

The project uses the **TMDB 5000 Movies Dataset**, which consists of two CSV files:

1. **tmdb_5000_movies.csv** – Contains movie details such as title, genres, keywords, overview, tagline, etc.
2. **tmdb_5000_credits.csv** – Contains the cast and crew information for each movie.

## Features Used

The system utilizes the following features for recommendation:

- **Genres** – Type of movie (Action, Comedy, Drama, etc.)
- **Keywords** – Tags related to the movie
- **Cast** – Main actors (Top 3)
- **Crew** – Director(s) of the movie
- **Overview** – Short description of the movie

All these features are combined to create a single textual feature called **tags**, which is then vectorized for similarity computation.

---

## Steps in the Project

1. **Data Preprocessing**
   - Merging movies and credits datasets on `title`.
   - Selecting important columns: `id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
   - Handling missing values by dropping null rows.
   - Extracting relevant information from nested JSON-like strings using `ast.literal_eval`.
   - Keeping top 3 cast members and only directors from crew.
   - Removing spaces in names to avoid tokenization issues.
   - Combining all features into a single column `tags`.
   - Converting text to lowercase for uniformity.
   - Applying stemming using NLTK’s PorterStemmer to reduce words to their root form.

2. **Vectorization**
   - Using `CountVectorizer` with a maximum of 5000 features and removing English stop words.
   - Creating a matrix of vectors representing each movie's combined tags.

3. **Similarity Calculation**
   - Calculating cosine similarity between all movies using the vectorized tags.
   - The similarity matrix is used to recommend movies that are closest in content to a given movie.

4. **Recommendation Logic**
   - Find the index of the input movie.
   - Retrieve similarity scores for all movies.
   - Sort the movies by similarity score in descending order.
   - Recommend the top 10 most similar movies (excluding the input movie).

5. **Deployment**
   - A function `movie_recommend(movie_title)` is implemented to fetch recommended movies.
   - Pickle files are saved for deployment: `movies_df.pkl` and `similarity.pkl`.
