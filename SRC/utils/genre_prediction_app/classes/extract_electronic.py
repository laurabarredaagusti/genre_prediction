import requests
from variables import *
from time import sleep
import streamlit as st

class Extract:
    '''
    This class contains the board and it's necessary elements to start the game.
    '''
    # Client Id and Secret from Spotify API
    CLIENT_ID = CLIENT_ID
    CLIENT_SECRET = CLIENT_SECRET

    # base URL of all Spotify API endpoints
    BASE_URL = BASE_URL

    # URL for authorisation
    AUTH_URL = AUTH_URL

    # List with the audio features to extract
    track_features_list = track_features_list
    artist_features_list = artist_features_list
    audio_features_list = audio_features_list


    def __init__(self, track_url):

        self.track_url = track_url

        if len(self.track_url) > 0:
            try:
                self.api_response()
                self.define_track_id()
                self.extract_all_features()
                self.dict_into_dict()
            except:
                st.write('Url not available, please try a different one')
                self.track_url = ''

    def api_response(self):
        '''
        This function will create the persinalised headers to get data from the API
        Needed personal variables: client_id, client_secret
        '''
        # create the response from the API
        auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials',
                                                'client_id': CLIENT_ID,
                                                'client_secret': CLIENT_SECRET,})

        # convert the response to JSON
        auth_response_data = auth_response.json()

        # save the access token
        access_token = auth_response_data['access_token']

        # The headers to be used are personalised with our token
        self.headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}


    def define_track_id(self):
        '''
        This function will modify the track name, call the api and return the id of the track
        '''
        self.track_id = self.track_url.split("/")[-1].split("?")[0] 


    def api_call(self, url_string, url_id):
        '''
        This function will do individual calls to the API
        '''
        track_info = requests.get(BASE_URL + url_string + '/' + url_id, headers=self.headers)
        self.track_info = track_info.json()
        self.api_call_completed = True


    def extract_track_main_features(self):
        '''
        This function will iterate over the main track features and extract them into a dictionary
        '''
        for feature in track_features_list:
            try:
                feature_data = self.track_info[feature]
                feature = 'track_' + feature
                self.all_track_features[feature] = feature_data
            except:
                self.all_track_features[feature] = None

        try:
            artist_name = self.track_info['artists'][0]['name']
            self.all_track_features['artist_name'] = artist_name
        except:
            self.all_track_features['artist_name'] = None

        # Album name
        try:
            album = self.track_info["album"]["name"]
            self.all_track_features['album'] = album
        except: 
            self.all_track_features['album'] = None 

        # Album cover
        try:
            album_cover = self.track_info["album"]["images"][0]['url']
            self.all_track_features['album_cover'] = album_cover
        except:
            self.all_track_features['album_cover'] = None

        self.artist_id = self.track_info["artists"][0]["uri"]
        self.artist_id = self.artist_id.replace('spotify:artist:', '')

        
    def extract_artist_features(self):
        '''
        This function will iterate over the main artist features and extract them into a dictionary
        '''
        for feature in artist_features_list:
            try:
                feature_data = self.track_info[feature]
                feature = 'artist_' + feature 
                self.all_track_features[feature] = feature_data
            except:
                self.all_track_features[feature] = None


    def extract_track_audio_features(self):
        '''
        This function will iterate over all the audio features and extract them into a dictionary
        '''
        for feature in audio_features_list:
            try:
                feature_data = self.track_info[feature]
                self.all_track_features[feature] = feature_data
            except:
                self.all_track_features[feature] = None

    
    def extract_all_features(self):
        '''
        This function will take all the necessary actions to extract all the audio features from the track
        '''
        self.all_track_features = {}
        self.track_data = {}

        # Extract track fatures
        self.api_call('tracks', self.track_id)
        self.extract_track_main_features()

        # Extract artist features
        self.api_call('artists', self.artist_id)
        self.extract_artist_features()

        # Extract audio features
        self.api_call('audio-features', self.track_id)
        self.extract_track_audio_features()


    def dict_into_dict(self):
        '''
        This function will add the audio features in a nested dictionary, under the track_id 
        '''
        print(self.all_track_features)
        self.track_data[self.track_id] = self.all_track_features
    