import streamlit as st
import pickle
import pandas as pd
import os
import requests
import bz2


file = '/Users/kushaljirawla/Desktop/Movie/movies_dict.pkl'

movie_list = pickle.load(open(file, 'rb'))
moviesd = pd.DataFrame(movie_list)
movies = moviesd['title'].values

similarity = bz2.BZ2File('similarity', 'rb')
similarity = pickle.load(similarity)

def fetchposter(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1e3b8dc76ab2d0a1747a5d918031a040&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recomm(movie):
    movie_index = moviesd[moviesd['title'] == movie].index[0]
    distance = similarity[movie_index]

    movies_list = sorted(list(enumerate(distance)),reverse=True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(moviesd.iloc[i[0]].title)
        recommended_movies_posters.append(fetchposter(moviesd.iloc[i[0]].movie_id))

    return recommended_movies, recommended_movies_posters
    

st.title('Movie Recommendor')

option = st.selectbox('Please choose a Movie',movies)

if st.button('Recommend'):
    recommendations, posters = recomm(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])



