import pandas as pd
from sklearn import preprocessing
import pickle
from variables import *
import streamlit as st
from classes.extract import *


class Predict():
    '''
    This class can modify the entered data and apply the machine larning engineering
    '''
    genre_decode_dict = genre_decode_dict

    def __init__(self, song_name):

        self.song_name = song_name

        print(self.song_name)

        if len(self.song_name) > 0:
            object = Extract(self.song_name)
            self.track_data = object.track_data
            self.dict_to_df()
            self.feature_engineering()
            self.get_genre_prediction()
            self.show_predictions()


    def dict_to_df(self):
        '''
        This function takes the given dictionary and converts it into a dataframe
        '''
        self.track_data = pd.DataFrame.from_dict(self.track_data, orient='index')


    def feature_engineering(self):
        '''
        This function will modify the data from the dictionary in order to apply the ML model
        '''
        # Some of the names and albums of the tracks have extra information added after a '-' or in between '()'
        # Split will be used to remove it
        self.track_data['track_name'] = self.track_data['track_name'].str.split('-').str[0]
        self.track_data['track_name'] = self.track_data['track_name'].str.split('(').str[0]
        self.track_data['album'] = self.track_data['album'].str.split('(').str[0]
        self.track_data['album'] = self.track_data['album'].str.split('-').str[0]

        # Drop the columns that won't be used for the predictions
        self.track_data.drop(['album_cover', 'artist_genres'], axis=1, inplace=True)

        # The column containing the track_id will be renamed to track_id
        self.track_data.rename(columns={'Unnamed: 0' : 'track_id'}, inplace=True)

        # Encode the variables artist name and album
        le = preprocessing.LabelEncoder()
        self.track_data["artist_encoded"] = le.fit_transform(self.track_data["artist_name"])
        self.track_data["album_encoded"] = le.fit_transform(self.track_data["album"])


    def get_genre_prediction(self):
        '''
        This function will load the ML model and get the genre predictions from the given dataframe
        '''
        # Import the ML model as loaded_model and generate the predictions
        model_path = '../models/' + model
        with open(model_path, 'rb') as archivo_entrada:
            loaded_model = pickle.load(archivo_entrada)

        # Define the columns to use during the prediction and apply the model
        X_track = self.track_data[['track_popularity', 'artist_popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'artist_encoded', 'album_encoded']]
        genre_predictions = loaded_model.predict(X_track)

        # Add the predictions as an extra column in the dataframe, and decode them
        self.track_data['genre'] = genre_predictions
        self.track_data.genre = self.track_data.genre.map(genre_decode_dict)


    def show_predictions(self):
        '''
        This function will get the individual predictions and show them to the user
        '''
        # Create the variables with the information to return to the user
        track_name = self.track_data['track_name'].values[0]
        artist_name = self.track_data['artist_name'].values[0]
        track_genre = self.track_data['genre'].values[0]

        st.write('Track name: ', track_name)
        st.write('Artist name: ', artist_name)
        st.write('Track genre: ', track_genre)


