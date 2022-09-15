import pandas as pd
from sklearn import preprocessing
import pickle
from variables import *
import streamlit as st
from classes.extract_electronic import *
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class Predict_electronic():
    '''
    This class can modify the entered data and apply the machine larning engineering
    '''
    genre_decode_dict = genre_decode_dict

    def __init__(self, input):

        self.input = input

        if len(self.input) > 0:
            object = Extract(self.input)
            self.track_data = object.track_data
            self.dict_to_df()
            self.feature_engineering()
            self.scaling()
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
        self.track_data['artist_popularity'] = np.log1p(self.track_data.artist_popularity)
        self.track_data['track_popularity'] = np.log1p(self.track_data.track_popularity)
        self.track_data['tempo'] = np.log1p(self.track_data.tempo)
        self.track_data['duration_ms'] = np.log1p(self.track_data.duration_ms)

        # The column containing the track_id will be renamed to track_id
        self.track_data.rename(columns={'Unnamed: 0' : 'track_id'}, inplace=True)

    def scaling(self):
        # Define the columns to use during the prediction and apply the model

        scaler_path = '../../models/' + scaler
        with open(scaler_path, 'rb') as archivo_entrada:
            loaded_scaler = pickle.load(archivo_entrada)

        self.X_track = self.track_data[['track_popularity', 'artist_popularity', 'danceability', 'energy', 'loudness', 
                                   'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 
                                   'tempo', 'duration_ms']]
        
        self.X_track = pd.DataFrame(loaded_scaler.transform(self.X_track), columns = self.X_track.columns)


    def get_genre_prediction(self):
        '''
        This function will load the ML model and get the genre predictions from the given dataframe
        '''
        # Import the ML model as loaded_model and generate the predictions
        model_path = '../../models/' + model
        with open(model_path, 'rb') as archivo_entrada:
            loaded_model = pickle.load(archivo_entrada)

        # Define the columns to use during the prediction and apply the model
        genre_predictions = loaded_model.predict(self.X_track)

        print(self.track_data)

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


