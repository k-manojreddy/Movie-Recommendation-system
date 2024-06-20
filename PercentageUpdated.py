import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#loading data from csv file to pandas dataframe
movies_data = pd.read_csv('C:\\Users\\kmred\\OneDrive\\Desktop\\Movie Recommendation\\movies.csv')
#Selecting the relevant features for recommendation
selected_features=['genres','keywords','tagline','cast','director']
#Data Cleaning
for feature in selected_features:
  movies_data[feature]=movies_data[feature].fillna('')
combined_data= movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
#converting Categorical data to Numberic data (Feature Vectors)
feature_vectors=TfidfVectorizer().fit_transform(combined_data)
# getting the similarity scores using cosine similarity
similarity=cosine_similarity(feature_vectors)
movie_name='';
while True:
  #getting the movie name from user
  movie_name=input('Enter your movie name:')
  if movie_name=='q':
    break
  #creating a list with all the movies in the data set
  titles_list=movies_data['title'].tolist()
  find_close_matches=difflib.get_close_matches(movie_name,titles_list)
  if not find_close_matches:
    print('Movie Not found in our DataBase Try another')
  else:
    close_match=find_close_matches[0]
    #finding the index of movie with title
    movie_index=movies_data[movies_data.title==close_match]['index'].values[0]
    #getting a list of similar movies
    similarity_score=list(enumerate(similarity[movie_index]))
    #sorting the movies based on their similarity score
    sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
    #print the name of similar movies based on the index
    print('\n30 Movies Suggested for you:')
    print('{:<5} {:<50} {:<30}'.format('Rank', 'Movie Title', 'Similarity Percentage'))
    print('-' * 85)

    for i, (movie_index, similarity_percentage) in enumerate(sorted_similar_movies[:30], start=1):
        recommended_movie_title = movies_data.at[movie_index, 'title']
        print('{:<5} {:<50} {:<30}'.format(i, recommended_movie_title, f"{round(similarity_percentage * 100, 2)}%"))