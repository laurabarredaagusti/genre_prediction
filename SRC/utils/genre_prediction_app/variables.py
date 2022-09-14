# API credentials

# Client Id and Secret from Spotify API
CLIENT_ID = 'b3efc4982a5a4c7197f979d08087128d'
CLIENT_SECRET = '3cd6cc8bdf114d9a97be07ad12024683'

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# URL for authorisation
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Track features
track_features_list = ['name', 'popularity']

artist_features_list = ['genres', 'popularity']

audio_features_list = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
                  'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

# ML model
model = 'my_model'

# Decoding dictionary
genre_decode_dict = {1 : 'ambient',
                 2 : 'psytrance',
                 3 : 'dnb',
                 4 : 'hardstyle',
                 5 : 'trance',
                 6 : 'techno',
                 7 : 'pop',
                 8 : 'trap',
                 9 : 'synthwave'}
